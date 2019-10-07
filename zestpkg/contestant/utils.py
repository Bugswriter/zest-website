from flask import flash, abort, redirect
from flask_login import current_user
from zestpkg import db
from zestpkg.models import Team, Contestant, Event



def joinParty(eid, code=None):
	event = Event.query.get_or_404(eid) #checking event exist or not
	user_gender = current_user.getProfile().gender
	if event.gender != 'MF':
		if event.gender != user_gender:
			if event.gender == "M":
				flash('This event is only for Boys, check your profile', category="info")
			else:
				flash('This event is only for Boys, check your profile', category="info")
			
			abort(500)

	if code == None: 
		p = Contestant(user_id=current_user.id, event_id=eid)
	else:
		team =	Team.query.filter_by(team_code=code).first()
		if team == None:
			flash("Server Error", category='danger')
			abort(403)

		p = Contestant(user_id=current_user.id, event_id=eid, team_id=team.id)
		
	db.session.add(p)
	db.session.commit()	
	


def with_draw(eid):
	x = Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first()
	if x != None:
		db.session.delete(x)
	