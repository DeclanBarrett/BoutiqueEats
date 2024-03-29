from sqlalchemy.orm import backref
from . import db
from datetime import datetime
from flask_login import UserMixin

# User created on account creation
class User(db.Model, UserMixin):
    __tablename__ = 'users'  # good practice to specify table name
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    phone_number = db.Column(db.String(10), nullable=True)
    image = db.Column(db.String(400), nullable=False, default="/static/image/account.png")

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')
    reservations = db.relationship('Reservation', backref='user')
    restaurants = db.relationship('Restaurant', backref='user')

# Comments on restaurants
class Comment(db.Model):
    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    post_date = db.Column(db.DateTime, default=datetime.now())
    user_rating = db.Column(db.Integer, nullable=False)
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'))

    def __repr__(self):
        return "<Comment: {}>".format(self.text)

# Restaurants to visit
class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    __table_args__ = {'extend_existing': True}

    restaurant_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(150), nullable=False)
    suburb = db.Column(db.String(50), nullable=False)
    max_reservations = db.Column(db.Integer)

    caption = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(400), nullable=False)

    price = db.Column(db.Integer)

    cuisine_type = db.Column(db.String(30), nullable=False)

    num_courses = db.Column(db.Integer, nullable=False)

    website = db.Column(db.String(400))

    image = db.Column(db.String(400), nullable=False)

    # ... Create the Comments db.relationship
    # relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='restaurant', cascade="all, delete-orphan")
    statuses = db.relationship('RestaurantStatus', backref='restaurant', cascade="all, delete-orphan" )
    opening_hours = db.relationship('RestaurantOpeningHours', backref='restaurant', cascade="all, delete-orphan")
    reservations = db.relationship('Reservation', backref='restaurant', cascade="all, delete-orphan")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):  #string print method
        return "<Name: {}>".format(self.name)

class RestaurantOpeningHours(db.Model):
    __tablename__ = 'restaurantopeninghours'
    __table_args__ = {'extend_existing': True}

    restaurant_opening_hours_id = db.Column(db.Integer, primary_key=True)
    day_of_the_week = db.Column(db.String, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'))

# Restaurants to visit
class RestaurantStatus(db.Model):
    __tablename__ = 'restaurantstatuses'
    __table_args__ = {'extend_existing': True}

    restaurant_status_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100), nullable=False)
    at_time = db.Column(db.DateTime, default=datetime.now())

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'))

# Reservation to a specific restaturant for a user
class Reservation(db.Model):
    __tablename__ = 'reservations'
    __table_args__ = {'extend_existing': True}

    reservation_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    reservation_time = db.Column(db.DateTime, default=datetime.now())
    reservation_created = db.Column(db.DateTime, default=datetime.now())

    user_order = db.Column(db.String(300))
    reservation_status = db.Column(db.String(100))

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'))
    id = db.Column(db.Integer, db.ForeignKey('users.id'))
