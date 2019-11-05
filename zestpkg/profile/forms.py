from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_wtf.file import FileField, FileAllowed
from zestpkg.models import Profile

colleges = [('SRMS CET', 'SRMS College of Engg. & Tech. Bareilly' ),
		   ('SRMS CETR', 'SRMS College Of Engg. Tech & Research Bareilly'),
		   ('SRMS CET (BP)','SRMS College of Pharmacy, Bareilly'),
		   ('SRMS IMS', 'SRMS Institute Of Medical Sciences, Bareilly'),
		   ('SRMS NURSING','SRMS College of Nursing, Bareilly'),
		   ('SRMS IPS','SRMS Institute Of Paramedical Sciences, Bareilly'),
		   ('SRMS IBS','SRMS International Business School, Lucknow'),
		   ('SRMS CET Unnao','SRMS College of Engg. & Tech, Unnao'),
		   ('SRMS Law','SRMS College of Law, Bareilly'),
		   ('Invertis University','Invertis University, Bareilly'), 
		   ('MJPRU Bareilly','Mahatma Jyotiba Phule Rohilkhand University, Bareilly'),
		   ('Bareilly College','Bareilly College'),
		   ('KCMT College','Khandelwal College of Management Science and Technology, Bareilly'),
		   ('RBMI College','Rakshpal Bahadur Management Institute, Bareilly'),
		   ('IVRI Bareilly','Indian Veterinary Research Institute, Bareilly'),
		   ('Regional College','Regional College Of Professional Studies & Research, Bareilly'),
		   ('MIT Moradabad','MIT College of Management, Moradabad'),
		   ('Lotus Institute','Lotus Institute of Managment, Bareilly'),
		   ('MIET Meerut','Meerut Institute of Engineering and Technology'),
		   ('Rajshree MRI','Rajshree Medical Research Institute & Hospital Bareilly'),
		   ('SRMS CNPS Unnao', 'SRMS College Of Nursing & Paramedical Sciences, Unnao'),
		   ('JSS Academy','J.S.S. Academy of Technical Education, Noida'),
		   ('GLBITM Institute','G.L. Bajaj Institute of Technology & Management'),
		   ('Galgotia University','Galgotia University, Noida'),
		   ('GLA University','GLA University, Mathura'),
		   ('BBDNIT College','Babu Banarasi Das National Institute of Technology & Management'),
		   ('PSIT Kanpur','Pranveer Singh Institute Of Technology, Kanpur'),
		   ('NIET Noida', 'Noida Institute of Engineering and Technology'),
		   ('MMM University','Madan Mohan Malaviya University Of Technology'),
		   ('RKGIT College','Raj Kumar Goel Institute Of Technology, Ghaziabad'),
		   ('Graphics Era','Graphic Era Deemed to be University'),
		   ('Indraprasth College','Inderprastha Engineering College'),
		   ('KIET Ghaziabad','KIET Group of Institutions'),
		   ('GD Goenka','GD Goenka Institute'),
		   ('United College','United College'),
		   ('Gangasheel Bareilly','Gangasheel School of Nursing, Bareilly'),
		   ('SRM College','SRM College'),
		   ('Other', 'Other')]


class ProfileForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
	last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
	course = SelectField('Course', validators=[DataRequired(), Optional()], choices=[('B.Tech','B.Tech'), ('B.Pharm', 'B.Pharm'), ('MBA', 'MBA'), ('MCA', 'MCA'), ('M.Tech', 'M.Tech'),('B.Com','B.Com'), ('BCA', 'BCA'), ('LL.B','LL.B'), ('BA LL.B', 'BA LL.B'), ('BA','BA') , ('MBBS', 'MBBS'), ('B.Sc', 'B.Sc'), ('M.Sc','M.Sc') ,('Other', 'Other')])
	branch = SelectField('Branch', validators=[Optional()], choices=[('CS', 'Computer Science & Engineering'), ('ME', 'Mechanical Engineering'), ('EC', 'Electronics & Communications'), ('IT', 'Information Technology'), ('EN', 'Electrical & Electronics Engineering'), ('CE', 'Civil Engineering'), ('Other', 'Other')])
	roll_num = StringField('Roll Number', validators=[DataRequired()])
	phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10, message='Invalid Phone Number')])
	college = SelectField('College', validators=[DataRequired(), Optional()], choices=colleges)
	gender = SelectField('Gender', validators=[DataRequired(), Optional()], choices = [('M','Male'),('F','Female')])
	submit = SubmitField('Submit Profile Info')

	


