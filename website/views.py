from flask import Blueprint, render_template
from flask_login.utils import login_required

from website.models import Restaurant

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

@login_required
@bp.route('/createrestaurant')
def createrestaurant():
    return render_template("postform.html")