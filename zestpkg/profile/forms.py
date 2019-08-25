from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_wtf.file import FileField, FileAllowed
from zestpkg.models import Profile

class ProfileForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
	last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
	image = FileField('Food Picture', validators=[FileAllowed(['jpg', 'png'])])
	course = SelectField('Course', validators=[DataRequired(), Optional()], choices=[('B.Tech','B.Tech'), ('B.Pharm', 'B.Pharm'), ('MBA', 'MBA')])
	branch = SelectField('Branch', validators=[Optional()], choices=[('CS', 'Computer Science'), ('ME', 'Mechanical Eng.'), ('EC', 'Electronics'), ('IT', 'Information Technology')])
	roll_num = IntegerField('Roll Number', validators=[DataRequired()])
	phone = StringField('Contact Number', validators=[DataRequired()])
	college = SelectField('College', validators=[DataRequired(), Optional()], choices=[('SRMS CET Bareilly', 'SRMS CET' ), ('Other', 'Other')])
	gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
	submit = SubmitField('Submit Profile')



