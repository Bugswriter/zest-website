from flask import Blueprint, render_template, redirect, flash
from zestpkg import db
from zestpkg.models import User, Event, Contestant
from flask_login import login_required, current_user
from zestpkg.contestant.utils import checkProfile

contestant = Blueprint('contestant', __name__)

@contestant.route('/events/<int:eid>/participate')
@login_required
def participate(eid):
	checkProfile()
	event = Event.query.get_or_404(eid)
	contestant = Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first()
	if contestant == None:
		x = Contestant(user_id=current_user.id, event_id=eid)
		db.session.add(x)
		db.session.commit()
		contestant = Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first()
		flash(f'You are registered for {event.title} event', category='success')

	return redirect('/events')


@contestant.route('/events/<int:eid>/create_team', methods=['GET'])
@login_required
def createTeam(eid):
	checkProfile()
	event = Event.query.get_or_404(eid)
	if request.args.get('team_name'):
		team_name = request.args.get('team_name')
		code = create_team(team_name, eid)
	else:
		abort(500)



@contestant.route('/events/<int:eid>/withdraw')
@login_required
def withdraw(eid):
	checkProfile()
	event = Event.query.get_or_404(eid)
	participation =	Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first()
	print(participation)
	db.session.delete(participation)
	db.session.commit()
	
	flash(f'You are removed from {event.title} event', category='info')

	return redirect('/events')