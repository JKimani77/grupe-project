from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    name = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')

class RegForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(),Email()])
    name = StringField('Enter Your Username', validators=[Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("The Email has already been taken!")
    
    def validate_username(self, data_field):
        if User.query.filter_by(name = data_field.data).first():
            raise ValidationError("The username has already been taken")
