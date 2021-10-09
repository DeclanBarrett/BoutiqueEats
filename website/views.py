from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/restaurant')
def restaurant():
    return render_template("restaurant.html")

@bp.route('/bookings')
def bookings():
    return render_template("bookings.html")

@bp.route('/createrestaurant')
def user():
    return render_template("postform.html")