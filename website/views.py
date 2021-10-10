from flask import Blueprint, render_template, url_for
from flask_login.utils import login_required
from website.forms import RestaurantForm
from website.models import Restaurant
from . import db
import os
from werkzeug.utils import redirect, secure_filename

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    restaurants = Restaurant.query.all()
    return render_template("index.html", restaurants=restaurants)

@bp.route('/restaurant')
def restaurant():
    return render_template("restaurant.html")

@bp.route('/bookings')
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
                                description=form_restaurant.description.data,
                                price=form_restaurant.price.data,
                                cuisine_type=form_restaurant.cuisine_type.data,
                                num_courses=form_restaurant.num_courses.data,
                                website=form_restaurant.website.data,
                                image=db_file_path)
        db.session.add(restaurant)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template("postform.html",form_restaurant=form_restaurant)

def check_upload_file(form):
    #get file data from form
    fp = form.image.data
    filename = fp.filename
    #get the current path of the module file… store image file relative to this path
    BASE_PATH = os.path.dirname(__file__)
    #upload file location – directory of this file/static/image
    upload_path = os.path.join(BASE_PATH, 'static/image',
                               secure_filename(filename))
    #store relative path in DB as image location in HTML is relative
    db_upload_path = '/static/image/' + secure_filename(filename)
    #save the file and return the db upload path
    fp.save(upload_path)
    return db_upload_path