from flask import Blueprint, render_template, redirect, flash, request, redirect, url_for
from zestpkg import db
from zestpkg.contestant.utils import *
from zestpkg.models import User, Event, Contestant
from flask_login import login_required, current_user

contestant = Blueprint('contestant', __name__)

@contestant.route('/event/<int:eid>/participate')
@login_required
def participate(eid):
	if current_user.profile == None:
		flash('You need to create your Profile Card first!', category='warning')
		return redirect(url_for('profile.create_profile'))

	event = Event.query.get_or_404(eid)
	if event.status == False:
		flash("Registeration for this event is closed right now.", category='warning')
		return redirect(url_for('event.event_page', eid=eid))

	user_gender = current_user.profile.gender
	if event.gender != None and event.gender != user_gender:
		if event.gender == "M":
			flash('This event is only for Boys, check your profile', category="info")
		else:
			flash('This event is only for Girls, check your profile', category="info")
			
		return redirect(url_for('event.event_page', eid=event.id))

	
	contestant = Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first()
	if contestant == None:
		joinParty(eid)
		flash(f'You are registered for {event.title} event', category='success')
	else:
		flash(f'You are already regsitered for {event.title} event', category='info')

	return redirect(url_for('event.my_events'))




@contestant.route('/events/<int:eid>/withdraw')
@login_required
def withdraw(eid):
	if current_user.getProfile() == None:
		flash('You need to create your Profile Card first!', category='info')
		return redirect(url_for('profile.create_profile'))

	event = Event.query.get_or_404(eid)
	if event.status == False:
		flash("You can't withdraw now! This event is offline right now.", category='warning')
		return redirect(url_for('event.event_page', eid=eid))
	
	x = Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first()
	if x != None:
		db.session.delete(x)
		db.session.commit()

	flash(f'You are removed from {event.title} event', category='info')

	return redirect('/events')