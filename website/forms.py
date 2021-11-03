
from flask_wtf import FlaskForm
from wtforms import Form
from wtforms.validators import Optional
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, IntegerField, FileField, FieldList, FormField
from wtforms.fields.core import BooleanField, RadioField, SelectField
from wtforms.fields.html5 import TimeField, URLField, DateTimeLocalField
from wtforms.fields.simple import HiddenField
from wtforms.validators import URL, InputRequired, Length, Email, EqualTo, NoneOf, NumberRange, ValidationError
from flask_wtf.file import FileRequired, FileField, FileAllowed
from datetime import date

ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}

def validate_date(form, field):
    print(field.data)
    if field.data.date() < date.today():
        raise ValidationError("The date cannot be in the past!")
    print("Valid Date")

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("Username", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field


    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])

    image = FileField('profile picture',
                      validators=[
                          FileAllowed(ALLOWED_FILE,
                                      message='Only supports png,jpg,JPG,PNG')
                      ])

    confirm = PasswordField("Confirm Password")



    #submit button
    submit = SubmitField("Register")

def validate_both_fields(form, field):
    print("Check 1")
    for day_tuple in form.opening_hours:
        print("Check 2: " + day_tuple.start.data.strftime("%H:%M") + " to " + day_tuple.end.data.strftime("%H:%M"))
        if (day_tuple.start.data and (not day_tuple.end.data)) or (day_tuple.end.data and (not day_tuple.start.data)):
            print("Valid Both Fields")
            raise ValidationError("Must have a start and end date, or neither") 
    
def validate_enddate_field(form, field):
    print("Check 3")
    for day_tuple in form.opening_hours:
        print("Check 4")
        if day_tuple.start.data and day_tuple.end.data and (day_tuple.start.data > day_tuple.end.data):
            print("Valid Endate Fields")
            raise ValidationError("End date must not be earlier than start date.")   

class DayHoursForm(Form):
    day = HiddenField()
    start = TimeField('start', validators=[Optional()])
    end = TimeField('end', validators=[Optional()])

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
    status = RadioField("set status", choices=[("upcoming", "upcoming"), ("inactive", "inactive"), ("booked","booked"), ("cancelled", "cancelled")])

    opening_hours = FieldList(FormField(DayHoursForm), min_entries=7) #validators=[validate_both_fields, validate_enddate_field]
    
    submit = SubmitField("post restaurant")


class RestaurantStatusForm(FlaskForm):
    status = RadioField("status", choices=["upcoming", "inactive", "booked", "cancelled"])
    submit = SubmitField("Set Status")

class ReservationForm(FlaskForm):
    quantity = IntegerField("quantity", validators=[InputRequired(), NumberRange(min=0)])
    time = DateTimeLocalField("reservation date", format='%Y-%m-%dT%H:%M', validators=[InputRequired(), validate_date])
    order = TextAreaField("order", validators=[Length(max=300)])
    submit = SubmitField("reserve")

class CommentForm(FlaskForm):
    text = TextAreaField("comment", validators=[InputRequired(), Length(max=400)])
    user_rating = IntegerField("rating /5", validators=[InputRequired(), NumberRange(min=0, max=5)])
    submit = SubmitField("post comment")

class FilterRestaurantsForm(FlaskForm):
    name = StringField("restaurant name", default="", validators=[Optional()])
    cuisine_type = SelectField("cuisine type", choices=[("", "all"), ("modern australian", "modern australian"),("contemporary","contemporary"),
    ("french","french"),("italian","italian"),("japanese","japanese"),("middle eastern", "middle eastern"),("mediterranean","mediterranean"),
    ("asian", "asian"),("european","european")], validators=[Optional()])
    rating = RadioField("ratings", choices=[(0, "Any"),(3,"3+"),(4,"4+"),(4.5,"4.5+")], default=0, validators=[Optional()], coerce=float)
    minimum_price = IntegerField("minimum price", default=0, validators=[Optional()])
    maximum_price = IntegerField("maximum price", default=1000, validators=[Optional()])
    courses = IntegerField("courses", default=0, validators=[Optional()])
    submit = SubmitField("submit")


