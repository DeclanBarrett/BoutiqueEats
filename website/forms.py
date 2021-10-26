
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, IntegerField, FileField
from wtforms.fields.core import RadioField, SelectField
from wtforms.fields.html5 import URLField, DateTimeLocalField
from wtforms.validators import URL, InputRequired, Length, Email, EqualTo, NoneOf, NumberRange, ValidationError
from flask_wtf.file import FileRequired, FileField, FileAllowed
from datetime import datetime

ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}

def validate_date(form, field):
        if field.data < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("username", validators=[InputRequired('Enter user name')])
    password=PasswordField("password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("username", validators=[InputRequired()])
    email_id = StringField("email address", validators=[Email("Please enter a valid email")])
    
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field

    #linking two fields - password should be equal to data entered in confirm
    password = PasswordField("password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])

    image = FileField('profile picture',
                      validators=[
                          FileAllowed(ALLOWED_FILE,
                                      message='Only supports png,jpg,JPG,PNG')
                      ])

    confirm = PasswordField("confirm password")

    #submit button
    submit = SubmitField("register")

class RestaurantForm(FlaskForm):
    restaurant_name = StringField("restaurant name", validators=[InputRequired()])
    street = StringField("street", validators=[InputRequired()])
    suburb = StringField("suburb", validators=[InputRequired()])

    cuisine_type = SelectField("cuisine type", choices=[(None, "select option"), ("modern australian", "modern australian"),("contemporary","contemporary"),
    ("french","french"),("italian","italian"),("japanese","japanese"),("middle eastern", "middle eastern"),("mediterranean","mediterranean"),
    ("asian", "asian"),("european","european")], validators=[InputRequired()])

    caption = StringField('caption', validators=[InputRequired(), Length(max=200)])
    description = TextAreaField("description", validators=[InputRequired(), Length(min=10, max=400)])
    price = IntegerField("price per person", validators=[NumberRange(min=0)])
    num_courses = IntegerField("num. of courses", validators=[NumberRange(1, 20), InputRequired()])
    max_num_reservations = IntegerField("num. available spots", validators=[InputRequired()])
    website = URLField("website")
    image = FileField('restaurant image',
                      validators=[
                          FileRequired(message='Image cannot be empty'),
                          FileAllowed(ALLOWED_FILE,
                                      message='Only supports png,jpg,JPG,PNG')
                      ])
    status = RadioField("set status", choices=["upcoming", "inactive", "booked", "cancelled"])
    submit = SubmitField("post restaurant")



class RestaurantStatusForm(FlaskForm):
    status = RadioField("status", choices=["upcoming", "inactive", "booked", "cancelled"])
    submit = SubmitField("Set Status")

class ReservationForm(FlaskForm):
    quantity = IntegerField("quantity", validators=[InputRequired(), NumberRange(min=0)])
    time = DateTimeLocalField("reservation date", validators=[InputRequired(), validate_date])
    order = TextAreaField("order", validators=[InputRequired(), Length(max=300)])
    submit = SubmitField("reserve")

class CommentForm(FlaskForm):
    text = TextAreaField("comment", validators=[InputRequired(), Length(max=400)])
    user_rating = IntegerField("rating /5", validators=[InputRequired(), NumberRange(min=0, max=5)])
    submit = SubmitField("post comment")

    
