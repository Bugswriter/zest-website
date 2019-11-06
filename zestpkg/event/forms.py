from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_wtf.file import FileField, FileAllowed
from zestpkg.models import Event, User
from wtforms.widgets import TextArea

class EventForm(FlaskForm):
	title = StringField('Event Title', validators=[DataRequired()])	
	orguname = StringField('Organizer Username', validators=[DataRequired()])
	category = SelectField('Category', validators=[DataRequired(), Optional()], choices=[('zestopen', 'Zest Open'), ('zestclose', 'Zest Close'),('aamod', 'Aamod')])
	subcategory = SelectField('Sub Category', validators=[DataRequired(),Optional()], choices=[('sports', 'Sports'), ('atheletics', 'Atheletics'),('dance', 'Dance'),('drama','Drama'),('music','Music'),('informals','Informals'),('deco', 'Decoration'),('fine arts', 'Fine Arts'), ('literary','Literary'), ('renaissance','Renaissance')])
	image = FileField('Cover Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
	num_of_member = IntegerField('Number of member',validators=[DataRequired()])
	time = StringField('Event Time')
	about = StringField('Event Details', widget=TextArea())
	status = SelectField('Status', validators=[DataRequired(), Optional()], choices=[('T', 'Online'), ('F', 'Offline')])
	submit = SubmitField('Register Event')

	def validate_orguname(self, orguname):
		user = User.query.filter_by(username=orguname.data).first()
		if user is None:
			raise ValidationError("No account with this username")	




