
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, IntegerField, FileField
from wtforms.fields.core import RadioField, SelectField
from wtforms.validators import URL, InputRequired, Length, Email, EqualTo, NoneOf, NumberRange
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
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
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

class RestaurantForm(FlaskForm):
    restaurant_name = StringField("restaurant name", validators=[InputRequired()])
    street = StringField("street", validators=[InputRequired()])
    suburb = StringField("suburb", validators=[InputRequired()])

    cuisine_type = SelectField("cuisine type", choices=[(None, "select option"), ("modern australian", "modern australian"),("contemporary","contemporary"),
    ("french","french"),("italian","italian"),("japanese","japanese"),("middle eastern", "middle eastern"),("mediterranean","mediterranean"),
    ("asian", "asian"),("european","european")], validators=[InputRequired()])

    description = TextAreaField("description", validators=[InputRequired(), Length(min=10, max=200)])
    price = IntegerField("price per person", validators=[NumberRange(min=0)])
    num_courses = IntegerField("num. of courses", validators=[NumberRange(1, 20), InputRequired()])
    website = StringField("website", validators=[URL()])
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