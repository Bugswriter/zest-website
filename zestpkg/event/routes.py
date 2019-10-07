from flask import Blueprint, render_template, redirect, flash, request, abort, url_for
from flask_login import current_user, login_required
from zestpkg.event.forms import EventForm
from zestpkg import db
from zestpkg.models import Event, Profile, Team, Contestant
from zestpkg.event.utils import *

event = Blueprint('event', __name__)

@event.route('/events/', methods=['GET'])
def all_events():
	page = request.args.get('page', 1, type=int)
	category = request.args.get('cat')
	subcat = request.args.get('subcat')
	events = Event.query.paginate(page=page, per_page=10)
	events = events.items
	active = ['','','','']
	title = 'All Zest Events'

	if category == 'aamod':
		active[3] = 'active'
		title = 'Aamod Events'
		events = Event.query.filter_by(category='aamod')

	elif category == 'zestopen':
		active[1] = 'active'
		title = 'Zest Open'
		events = Event.query.filter_by(category='zestopen')
		
	elif category == 'zestclose':
		active[2] = 'active'
		title = 'Zest Close'
		events = Event.query.filter_by(category='zestclose')

	if subcat != None:
		title = subcat.capitalize() + ' Events'
		events = Event.query.filter_by(subcategory=subcat)

	if events == None:
		flash('No events in your filter', category='info')
		title = 'All Zest Events'
		events = Event.query.all()

	if 'active' not in active:
		active[0] = 'active'

	if current_user.is_authenticated:
		events = [event for event in events if event.gender == None or event.gender == current_user.profile.gender] 

	
	return render_template('all_events.html', events=events, title=title, active=active)



@event.route('/event/<int:eid>')
def event_page(eid):
	event = Event.query.get_or_404(eid)
	profile = Profile.query.filter_by(user_id=event.getOrganizer().id).first()
	return render_template('eventpage.html', event=event, user=profile)


@event.route('/event/my', methods=['GET', 'POST'])
@login_required
def my_events():
	return render_template('myevents.html', events=current_user.getEvents(), title="My Events")



@event.route('/event/<string:eid>/participants')
@login_required
def participant_list(eid):
	event = Event.query.get_or_404(eid)
	if event.eventType() == 'Solo':
		contestants = event.getParticipants()
		return render_template('participants.html', contestants=contestants)
	else:
		teams = event.getParticipants()
		return render_template('teamlist.html', teams=teams)



@event.route('/event/<int:eid>/delete')
@login_required
def delete_event(eid):
	event = Event.query.get_or_404(eid)
	db.session.delete(event)
	db.session.commit()
	flash('Your event has been deleted', category='success')
	return redirect(url_for('event.eventpage'))