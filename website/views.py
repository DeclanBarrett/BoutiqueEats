from flask import Blueprint, render_template, url_for, request
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

@bp.route('/')
def index():
    filtered_form = FilterRestaurantsForm()
    restaurants = Restaurant.query.all()
    statuses = []
    for restaurant in restaurants:
        statuses.append(RestaurantStatus.query.filter_by(restaurant=restaurant).order_by(desc(RestaurantStatus.at_time)).first())
    return render_template("index.html", restaurants=restaurants, restaurant_statuses=statuses, filter_form = filtered_form)

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
            print(err)
    statuses = []
    for restaurant in restaurants:
        statuses.append(RestaurantStatus.query.filter_by(restaurant=restaurant).order_by(desc(RestaurantStatus.at_time)).first())
    return render_template("index.html", restaurants=restaurants, restaurant_statuses=statuses, filter_form = filter_form)

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
    return render_template("restaurant.html", restaurant=restaurant, comment_form=comment_form, reservation_form=reservation_form)

@restaurant_bp.route('/<restaurant>/reservation', methods=["GET", "POST"])
def reservation(restaurant):
    reservation_form = ReservationForm()
    restaurant_obj = Restaurant.query.filter_by(restaurant_id=restaurant).first()
    if reservation_form.validate_on_submit():
        print("reservation valid")
        reservation = Reservation(
            quantity = reservation_form.quantity.data,
            reservation_time = reservation_form.time.data,
            order = reservation_form.order.data,
            restaurant = restaurant_obj,
            user = current_user
        )
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for("main.bookings", show_modal=True))
    print("reservation invalid")
    
    return redirect(url_for("restaurants.restaurant", id=restaurant))

@restaurant_bp.route('/<restaurant>/comment', methods=["GET", "POST"])
def comment(restaurant):
    comment_form = CommentForm()
    restaurant_obj = Restaurant.query.filter_by(restaurant_id=restaurant).first()
    if comment_form.validate_on_submit():
        print("comment valid")
        comment = Comment(
            text=comment_form.text.data,
            user_rating = comment_form.user_rating.data,
            restaurant=restaurant_obj,
            user=current_user
        )

        db.session.add(comment)
        db.session.commit()
    print("Should see this after a valid comment")
    return redirect(url_for("restaurants.restaurant", id=restaurant))

