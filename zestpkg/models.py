import string
import random
from zestpkg import db
from flask_login import UserMixin
from zestpkg import login_manager
from flask import url_for, current_app, redirect
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


def generate_team_code():
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	profile = db.relationship('Profile', backref='account', lazy=True)
	verified = db.Column(db.Boolean, nullable=False, default=False)

	def getTeam(self):
		return Team.query.filter_by(user_id=self.id)

	def getProfile(self):
		try:
			return self.profile[0]
		except:
			return None

	def getEvents(self):
		party = Contestant.query.filter_by(user_id=self.id)
		events = []
		for i in party:
			event = Event.query.get_or_404(i.event_id)
			events.append(event)

		return list(set(events))



	def get_reset_token(self, expires_secs=300):
		s=Serializer(current_app.config['SECRET_KEY'], expires_secs)
		return s.dumps({'user_id': self.id}).decode('utf-8')


	@staticmethod
	def verify_reset_token(token):
		s=Serializer(current_app.config['SECRET_KEY'])
		try:
			user_id=s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)	

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


class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), nullable=False)
	image = db.Column(db.String(60), nullable=False, default='default.jpg')
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	participants = db.relationship('Contestant', backref='event', lazy=True)
	team_limit = db.Column(db.Integer, nullable=False, default=1)
	time = db.Column(db.String(15), nullable=True)
	price = db.Column(db.String(30), nullable=True)
	detail_txt = db.Column(db.Text(60), nullable=True)

	def eventType(self):
		if self.team_limit == 1:
			return "Solo"
		else:
			return "Team"

	def getOrganizer(self):
		user = User.query.get(self.user_id)
		return user
		
	def getParticipants(self):
		if self.team_limit == 1:
			party = self.participants
			participants = []
			for member in party: 
				user = User.query.get_or_404(member.user_id)
				participants.append(user)

			return participants
		else:
			party = self.participants
			teams = []
			for member in party:
				team = Team.query.get_or_404(member.team_id)
				teams.append(team)

			return list(set(teams))

	def __repr__(self):
		return "Event({}, {})".format(self.title, self.eventType())


class Contestant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)	
	event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
	team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
	paid = db.Column(db.Boolean, nullable=True, default=False)

	def __repr__(self):
		user = User.query.get(self.user_id)
		event = Event.query.get(self.event_id)

		return "Contestant({}, {})".format(user.username, event.title)



class Team(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	members = db.relationship('Contestant', backref='team', lazy=True)
	event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False )
	team_code = db.Column(db.String(10), nullable=False, default=generate_team_code())

	def getMember(self):
		party = self.members
		members = []
		for x in party:
			user = User.query.get_or_404(x.user_id)
			members.append(user)

		return members


	def __repr__(self):
		return "Team({}, {})".format(self.name, self.team_code)





