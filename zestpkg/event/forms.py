from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_wtf.file import FileField, FileAllowed
from zestpkg.models import Event
from wtforms.widgets import TextArea

class EventForm(FlaskForm):
	title = StringField('Event Title', validators=[DataRequired()])
	event_type = SelectField('Course', validators=[DataRequired(), Optional()], choices=[('Team','Team Event'), ('Solo', 'Solo Event')])
	num_of_member = IntegerField('Number of member', validators=[DataRequired()])
	detail = StringField('Event Details', widget=TextArea())
	submit = SubmitField('Register Event')	


