from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from zestpkg.models import User


class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Regexp('^[A-Za-z][A-Za-z0-9]{3,15}$', message="Username must start with alphabet with no special characters") ,Length(min=3, max=15)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Password must be of minimum 6 characters")])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')


	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("That Username already exist")

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("That Email already exist")



class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class RequestResetForm(FlaskForm):
	email=StringField('Email', 
						validators=[DataRequired(), Email()])
	submit=SubmitField('Request Passwrod Reset')
	
	def validate_email(self, email):
		user=User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('Their is no account with that email.')


class ResetPasswordForm(FlaskForm):
	password=PasswordField('Password', 
						validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password', 
						validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField('Reset Passwrod')


class ChangePassword(FlaskForm):
	current_password = PasswordField('Current Password', validators=[DataRequired()])
	new_password = PasswordField('New Password', validators=[DataRequired()])
	confirm_new_password = PasswordField('Confirm new password', validators=[DataRequired(), EqualTo('new_password')])
	submit = SubmitField('Update Passoword')