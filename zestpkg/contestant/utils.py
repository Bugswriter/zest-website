from flask import flash, abort, redirect
from flask_login import current_user
from zestpkg import db
from zestpkg.models import Team, Contestant, Event


def verify_team_code(code):
	team =	Team.query.filter_by(team_code=code).first()
	if team == None:
		return None
	else:
		return team



def take_participation(eid, code=None):
	event = Event.query.get_or_404(eid) #checking event exist or not
	if code == None: 
		p = Contestant(user_id=current_user.id, event_id=eid)
	else:
		team = verify_team_code(code)
		if team == None:
			flash("Invalid Team code", category='danger')
			abort(403)

		p = Contestant(user_id=current_user.id, event_id=eid, team_id=team.id)
		
	db.session.add(p)
	db.session.commit()

	return Contestant.query.filter_by(user_id=current_user.id ,event_id=eid).first()

	
	


def with_draw(eid):
	x = Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first()
	if x != None:
		db.session.delete(x)
	


def create_team(team_name, eid):
	if Team.query.filter_by(name=team_name).first() == None:
		#Creating Team
		team = Team(name=team_name, event_id=eid)
		db.session.add(team)
		db.session.commit()
		team = Team.query.filter_by(name=team_name).first()
		take_participation(eid, team.team_code) #jo team bana raha hai wo khud ko register kar lega
		return team
	else:
		flash('Team already exist with this name!', category='warning')
		abort(403)

