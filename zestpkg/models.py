from zestpkg import db
from flask_login import UserMixin
from zestpkg import login_manager

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	profile = db.relationship('Profile', backref='account', lazy=True)
	verified = db.Column(db.Boolean, nullable=False, default=False)

	def __repr__(self):
		return "User({}, {})".format(self.username, self.email)



class Profile(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	image = db.Column(db.String(60), nullable=False, default='default.jpg')
	course = db.Column(db.String(40), nullable=False)
	branch = db.Column(db.String(40), nullable=True)
	roll_number = db.Column(db.String(40), nullable=False)
	phone = db.Column(db.String(15), nullable=False)
	college = db.Column(db.String(150), nullable=False)
	gender = db.Column(db.String(1), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return "Profile({}, {}, {})".format(self.name, self.phone, self.course)
