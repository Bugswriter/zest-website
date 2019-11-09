from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_wtf.file import FileField, FileAllowed
from zestpkg.models import *


class PIDSearch(FlaskForm):
	pid = IntegerField('PID Number', validators=[DataRequired()])
	submit = SubmitField('Search')

	def validate_pid(self, pid):
		user = User.query.get(pid.data)
		if user == None:
			raise ValidationError("PID doesn't Exist!")
		elif user.profile == None:
			raise ValidationError("Profile doesn't exist!")
		else:
			pass

