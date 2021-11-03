from flask import Blueprint, render_template, url_for, request, flash
from flask_login.utils import login_required, current_user
from wtforms import form
from website.forms import CommentForm, FilterRestaurantsForm, RestaurantForm, ReservationForm
from website.models import Reservation, Restaurant, RestaurantOpeningHours, RestaurantStatus, Comment
from . import db
import os
from werkzeug.utils import redirect, secure_filename
from website.file_checker import check_upload_file
from sqlalchemy import desc
from datetime import time, date
from collections import namedtuple

bp = Blueprint('main', __name__)

restaurant_bp = Blueprint('restaurants', __name__, url_prefix="/restaurants" )

#check restaurant space on day
def restaurant_space(restaurant, space_on_date):
    current_booking_quantity = 0
    for reservation in restaurant.reservations:
        if (reservation.reservation_time.date() == space_on_date):
            current_booking_quantity += reservation.quantity
    return restaurant.max_reservations - current_booking_quantity

#update todays status if not already updated
def set_todays_status(restaurant):
    if restaurant.statuses[-1].status != "inactive":
        if restaurant.statuses[-1].at_time.date() != date.today():
            restaurant_status = RestaurantStatus(status="upcoming",
                                            restaurant=restaurant)
            db.session.add(restaurant_status)
            db.session.commit()

#checks if the restaurant is open at a specific time
def check_opening_times(restaurant, time_to_check):
    for day_tuple in restaurant.opening_hours:
            if (day_tuple.day_of_the_week.lower() == time_to_check.strftime("%A").lower()):
                if (day_tuple.start_time <= time_to_check.time() and day_tuple.end_time >= time_to_check.time()):
                    return True
    return False

#checks if the restaurant is open on that day in general
def check_open_today(restaurant, time_to_check):
    for day_tuple in restaurant.opening_hours:
        if (day_tuple.day_of_the_week.lower() == time_to_check.strftime("%A").lower()):
            return True
    return False

@bp.route('/')
def index():
    filtered_form = FilterRestaurantsForm()
    restaurants = Restaurant.query.all()
    booking_space = []
    is_open_today = []
    for restaurant in restaurants:
        set_todays_status(restaurant)
        booking_space.append(restaurant_space(restaurant, date.today()))
        is_open_today.append(check_open_today(restaurant, date.today()))
    return render_template("index.html", restaurants=restaurants, filter_form = filtered_form, booking_space = booking_space, today=date.today(), is_open_today = is_open_today)

@bp.route('/filters', methods=["GET", "POST"])
def filtered_index():
    filter_form = FilterRestaurantsForm()
    if filter_form.validate_on_submit():
        
        name = filter_form.name.data
        cuisine = filter_form.cuisine_type.data
        num_courses = filter_form.courses.data 

        initial_restaurants = Restaurant.query.filter(
            Restaurant.name.like("%" + name + "%"),
            Restaurant.cuisine_type.like("%" + cuisine + "%"),
            Restaurant.price >= filter_form.minimum_price.data,
            Restaurant.price <= filter_form.maximum_price.data,
            Restaurant.num_courses >= num_courses
        ).all()

        restaurants = []
        for restaurant in initial_restaurants:
            rating = 3.0
            average = []
            for comment in restaurant.comments:
                average.append(comment.user_rating)
            if (len(average) > 0):
                rating = sum(average) / len(average)
            if (rating >= float(filter_form.rating.data)):
                restaurants.append(restaurant)
                
    else:
        print("invalid filtering")
        restaurants = Restaurant.query.all()
    for fieldName, errorMessages in filter_form.errors.items():
        for err in errorMessages:
            print(fieldName + " " + err)
    booking_space = []
    is_open_today = []
    for restaurant in restaurants:
        booking_space.append(restaurant_space(restaurant, date.today()))
        is_open_today.append(check_open_today(restaurant, date.today()))
    return render_template("index.html", restaurants=restaurants, filter_form = filter_form, booking_space = booking_space, today=date.today(), is_open_today = is_open_today)

@bp.route('/bookings')
@login_required
def bookings():
    bookings = Reservation.query.filter_by(user=current_user).all()
    return render_template("bookings.html", show_modal=request.args.get('show_modal'), bookings = bookings)

@bp.route('/createrestaurant', methods=["GET", "POST"])
@login_required 
def createrestaurant():

    dayhours = namedtuple('DayHours', ['day', 'start', 'end'])
    
    data = {'opening_hours' : [
        dayhours("Monday", None, None),
        dayhours("Tuesday",None, None),
        dayhours("Wednesday", None, None),
        dayhours("Thursday", None,None),
        dayhours("Friday", None, None),
        dayhours("Saturday", None, None),
        dayhours("Sunday", None, None),
    ]
    }

    print("They were all in it")

    form_restaurant = RestaurantForm(data = data)
    if form_restaurant.validate_on_submit():
        print('form was validated', 'success')
        db_file_path = check_upload_file(form_restaurant)
        restaurant = Restaurant(name=form_restaurant.restaurant_name.data,
                                street=form_restaurant.street.data,
                                suburb=form_restaurant.suburb.data,
                                caption=form_restaurant.caption.data,
                                description=form_restaurant.description.data,
                                price=form_restaurant.price.data,
                                cuisine_type=form_restaurant.cuisine_type.data,
                                max_reservations=form_restaurant.max_num_reservations.data,
                                num_courses=form_restaurant.num_courses.data,
                                website=form_restaurant.website.data,
                                image=db_file_path)
    
        restaurant_status = RestaurantStatus(status=form_restaurant.status.data,
                                            restaurant=restaurant)

        print("Got through regular creation")
        for day_tuple in form_restaurant.opening_hours:
            print("this is another tuple")
            if (day_tuple.start.data and day_tuple.end.data):
                print("Start Data and End Data")
                restaurant_opening_day = RestaurantOpeningHours(
                   day_of_the_week = day_tuple.day.data,
                   start_time = day_tuple.start.data,
                   end_time = day_tuple.end.data,

                   restaurant = restaurant
                )
                db.session.add(restaurant_opening_day)

        db.session.add(restaurant)
        db.session.add(restaurant_status)
        db.session.commit()
        print("Committed new restaurant to the database")
        
        return redirect(url_for('main.index'))
    return render_template("postform.html",form_restaurant=form_restaurant)

@restaurant_bp.route('/<id>')
def restaurant(id):
    comment_form = CommentForm()
    reservation_form = ReservationForm()
    restaurant = Restaurant.query.filter_by(restaurant_id = id).first()
    space = restaurant_space(restaurant, date.today())
    return render_template("restaurant.html", restaurant=restaurant, comment_form=comment_form, reservation_form=reservation_form, space=space, open_today = check_open_today(restaurant, date.today()))


@restaurant_bp.route('/<restaurant>/reservation', methods=["GET", "POST"])
@login_required
def reservation(restaurant):
    reservation_form = ReservationForm()
    restaurant_obj = Restaurant.query.filter_by(restaurant_id=restaurant).first()
    if reservation_form.validate_on_submit():
        
        #checking whether the reservation is within opening hours
        should_commit = check_opening_times(restaurant_obj, reservation_form.time.data)
        
        #checking the current status on the day
        appropriate_status = False
        statuses = []
        for status in restaurant_obj.statuses:
            if status.at_time.date() == reservation_form.time.data.date():
                statuses.append(status)

        current_status = "unavailable"
        if (len(statuses) > 0):
            current_status = statuses[-1].status
            if (statuses[-1].status == "upcoming"):
                appropriate_status = True
        elif (restaurant_obj.statuses[-1].status != "inactive"):
            appropriate_status = True
        else:
            current_status = statuses[-1].status
        
        enough_space = False
        if (restaurant_space(restaurant_obj, reservation_form.time.data.date()) - reservation_form.quantity.data >= 0):
            enough_space = True

        if (restaurant_space(restaurant_obj, reservation_form.time.data.date()) - reservation_form.quantity.data <= 0):
            restaurant_status = RestaurantStatus(status="booked",
                                                restaurant=restaurant_obj)
        else:
            restaurant_status = RestaurantStatus(status="upcoming",
                                                restaurant=restaurant_obj)
            

        reservation = Reservation(
            quantity = reservation_form.quantity.data,
            reservation_time = reservation_form.time.data,
            user_order = reservation_form.order.data,
            restaurant = restaurant_obj,
            user = current_user
        )

        if (should_commit and appropriate_status and enough_space):
            db.session.add(reservation)
            db.session.add(restaurant_status)
            db.session.commit()
            return redirect(url_for("main.bookings", show_modal=True))
        elif (should_commit == False):
            flash("Reservation is outside of opening hours", 'warning')
        elif (appropriate_status == False):
            flash("Reservation at " + restaurant_obj.name + " cannot be created since the restaurant is " + current_status, 'warning')
    
    return redirect(url_for("restaurants.restaurant", id=restaurant))

@restaurant_bp.route('/<restaurant>/comment', methods=["GET", "POST"])
def comment(restaurant):
    comment_form = CommentForm()
    restaurant_obj = Restaurant.query.filter_by(restaurant_id=restaurant).first()
    if comment_form.validate_on_submit():
        comment = Comment(
            text=comment_form.text.data,
            user_rating = comment_form.user_rating.data,
            restaurant=restaurant_obj,
            user=current_user
        )

        db.session.add(comment)
        db.session.commit()
        flash("Your comment has been posted", 'success')
    return redirect(url_for("restaurants.restaurant", id=restaurant))