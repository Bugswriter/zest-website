from flask import flash, abort, redirect
from flask_login import current_user
from zestpkg import db
from zestpkg.models import Team, Contestant, Event



def joinParty(eid, code=None):
	event = Event.query.get_or_404(eid) #checking event exist or not again

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
	


	