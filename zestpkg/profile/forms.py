from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_wtf.file import FileField, FileAllowed
from zestpkg.models import Profile

class ProfileForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
	last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
	course = SelectField('Course', validators=[DataRequired(), Optional()], choices=[('B.Tech','B.Tech'), ('B.Pharm', 'B.Pharm'), ('MBA', 'MBA')])
	branch = SelectField('Branch', validators=[Optional()], choices=[('CS', 'Computer Science'), ('ME', 'Mechanical Eng.'), ('EC', 'Electronics'), ('IT', 'Information Technology')])
	roll_num = StringField('Registeration Number', validators=[DataRequired()])
	phone = StringField('Contact Number', validators=[DataRequired()])
	college = SelectField('College', validators=[DataRequired(), Optional()], choices=[('SRMS CET', 'SRMS CET' ), ('SRMS College Of Pharmacy, Bareilly' ,'SRMS College Of Pharmacy, Bareilly'), ('SRMS Institute Of Medical Sciences Hospital, Bareilly', 'SRMS Institute Of Medical Sciences Hospital, Bareilly'), ('SRMS Institute Of Medical Sciences, Bareilly', 'SRMS Institute Of Medical Sciences, Bareilly'),('SRMS School Of Nursing, Bareilly','SRMS School Of Nursing, Bareilly'), ('SRMS College Of Engg. Tech & Research Bareilly', 'SRMS College Of Engg. Tech & Research Bareilly'), ('R.R. Cancer & Research Centre, Bareilly', 'R.R. Cancer & Research Centre, Bareilly'), ('SRMS Institute Of Paramedical Sciences, Bareilly','SRMS Institute Of Paramedical Sciences, Bareilly'), ('SRMS International Business School, Lucknow','SRMS International Business School, Lucknow'), ('SRMS CollegeOf Engg. & Tech, Unnao','SRMS CollegeOf Engg. & Tech, Unnao'), ('SRMS Charitable School, Lucknow', 'SRMS Charitable School, Lucknow'), ('SRMS Charitable School, Lucknow', 'SRMS Charitable School, Lucknow'), ('SRMS Functional Imaging & Medical Centre, Lucknow', 'SRMS Functional Imaging & Medical Centre, Lucknow'), ('SRMS College Of Nursing, Bareilly', 'SRMS College Of Nursing, Bareilly'), ('SRMS Goodlife (A Wellness Centre), Bareilly','SRMS Goodlife (A Wellness Centre), Bareilly'), ('SRMS Hospital, Unnao', 'SRMS Hospital, Unnao'), ('SRMS College Of Law, Bareilly', 'SRMS College Of Law, Bareilly'), ('SRMS College Of Nursing & Paramedical Sciences, Unnao', 'SRMS College Of Nursing & Paramedical Sciences, Unnao'), ('SRMS Step2life (A Rehabilitation & Physiotherapy Centre), Lucknow', 'SRMS Step2life (A Rehabilitation & Physiotherapy Centre), Lucknow') ,('Other', 'Other')])
	gender = SelectField('Gender', validators=[DataRequired(), Optional()], choices = [('M','Male'),('F','Female')])
	submit = SubmitField('Submit Profile Info')

	


