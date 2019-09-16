from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_wtf.file import FileField, FileAllowed
from zestpkg.models import Event
from wtforms.widgets import TextArea

class EventForm(FlaskForm):
	title = StringField('Event Title', validators=[DataRequired()])
	event_type = SelectField('Course', validators=[DataRequired(), Optional()], choices=[('Team','Team Event'), ('Solo', 'Solo Event')])
	image = FileField('Cover Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
	num_of_member = IntegerField('Number of member', validators=[DataRequired()])
	about = StringField('Event Details', widget=TextArea())
	price =IntegerField('Price', validators=[])
	submit = SubmitField('Register Event')	





