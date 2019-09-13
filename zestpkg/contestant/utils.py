from flask_login import current_user
from zestpkg import db
from zestpkg.models import Team, Contestant


def verify_team_code(code):
	team =	Team.query.filter_by(team_code=code).first()
	if team == None:
		# Team with given code doesn't exist
		return None
	else:
		# Team with given code does exist
		return team



def participate(eid, code=None):
	team = verify_team_code(code)
	if code == None:
		# Solo
		p = Participants(user_id=current_user.id, event_id=eid)
	else:
		# Team
		team = verify_team_code(code)
		if team == None:
			flash("Invalid Team code", category='danger')
			abort(403)

		p = Participants(user_id=current_user.id, event_id=eid, team_id=team.id)
		
	db.session.add(p)
	db.session.commit()
	return Participants.query.filter_by(user_id=current_user.id ,event_id=eid).first()

	
	


def withDraw(eid):
	x = Participants.query.filter_by(user_id=current_user.id, event_id=eid).first()
	if x != None:
		db.session.delete(x)
	


def createTeam(team_name, eid):
	'''
	argument - Team Name and Event ID
	return - team code or None (if team already exist with given name)
	purpose create Team in database
	'''
	if Team.query.filter_by(name=team_name).first() == None:
		#Creating Team
		team = Team(name=team_name, event_id=eid)
		db.session.add(team)
		db.session.commit()
		team = Team.query.filter_by(name=team_name).first()
		participate(eid, team.id)
		#team creator Joining team
		participate(eid, team.team_code)
		return team.team_code
	else:
		flash('Team already exist with this name!')
		abort(403)