from flask import Blueprint, render_template, url_for
from flask_login.utils import login_required, current_user
from website.forms import CommentForm, RestaurantForm, ReservationForm
from website.models import Restaurant, RestaurantStatus, Comment
from . import db
import os
from werkzeug.utils import redirect, secure_filename
from website.file_checker import check_upload_file
from sqlalchemy import desc

bp = Blueprint('main', __name__)

restaurant_bp = Blueprint('restaurants', __name__, url_prefix="/restaurants" )

@bp.route('/')
def index():
    restaurants = Restaurant.query.all()
    statuses = []
    for restaurant in restaurants:
        statuses.append(RestaurantStatus.query.filter_by(restaurant=restaurant).order_by(desc(RestaurantStatus.at_time)).first())
    return render_template("index.html", restaurants=restaurants, restaurant_statuses=statuses)

@bp.route('/bookings')
@login_required
def bookings():
    return render_template("bookings.html")

@bp.route('/createrestaurant', methods=["GET", "POST"])
@login_required 
def createrestaurant():
    form_restaurant = RestaurantForm()
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
        db.session.add(restaurant)
        db.session.add(restaurant_status)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    return render_template("postform.html",form_restaurant=form_restaurant)

@restaurant_bp.route('/<id>')
def restaurant(id):
    comment_form = CommentForm()
    reservation_form = ReservationForm()
    restaurant = Restaurant.query.filter_by(restaurant_id = id).first()
    return render_template("restaurant.html", restaurant=restaurant, comment_form=comment_form, reservation_form=reservation_form)

<<<<<<< Updated upstream
=======

@restaurant_bp.route('/<restaurant>/reservation', methods=["GET", "POST"])
@login_required
def reservation(restaurant):
    reservation_form = ReservationForm()
    restaurant_obj = Restaurant.query.filter_by(restaurant_id=restaurant).first()
    if reservation_form.validate_on_submit():
        print("reservation valid")
        reservation = Reservation(
            quantity = reservation_form.quantity.data,
            reservation_time = reservation_form.time.data,
            user_order = reservation_form.order.data,
            restaurant = restaurant_obj,
            user = current_user
        )

        should_commit = False
                
        for day_tuple in restaurant_obj.opening_hours:
            if (day_tuple.day_of_the_week.lower() == reservation_form.time.data.strftime("%A").lower()):
                if (day_tuple.start_time <= reservation_form.time.data.time() and day_tuple.end_time >= reservation_form.time.data.time()):
                    should_commit = True

        if (should_commit):
            db.session.add(reservation)
            db.session.commit()
            return redirect(url_for("main.bookings", show_modal=True))
        
        flash("Booking was outside of opening hours!", 'danger')
    
    return redirect(url_for("restaurants.restaurant", id=restaurant))

>>>>>>> Stashed changes
@restaurant_bp.route('/<restaurant>/comment', methods=["GET", "POST"])
def comment(restaurant):
    comment_form = CommentForm()
    restaurant_obj = Restaurant.query.filter_by(restaurant_id=restaurant).first()
    print("WHO IS THEY")
    if comment_form.validate_on_submit():
        print("Its validated")
        comment = Comment(
            text=comment_form.text.data,
            user_rating = comment_form.user_rating.data,
            restaurant=restaurant_obj,
            user=current_user
        )

        db.session.add(comment)
        db.session.commit()
    return redirect(url_for("restaurants.restaurant", id=restaurant))

