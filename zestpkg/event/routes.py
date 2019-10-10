from flask import Blueprint, render_template, redirect, flash, request, abort, url_for
from flask_login import current_user, login_required
from zestpkg.event.forms import EventForm
from zestpkg import db
from zestpkg.models import Event, Profile, Team, Contestant
from zestpkg.event.utils import *
from math import ceil

event = Blueprint('event', __name__)

@event.route('/events/', methods=['GET'])
def all_events():
	page = request.args.get('page', 1, type=int)
	pagelimit = 10
	category = request.args.get('cat')
	subcat = request.args.get('subcat')
	events = Event.query.paginate(page=page, per_page=pagelimit)
	active = ['','','','']
	title = 'All Zest Events'

	if category == 'aamod':
		active[3] = 'active'
		title = 'Aamod Events'
		events = Event.query.filter_by(category='aamod').paginate(page=page, per_page=10)

	elif category == 'zestopen':
		active[1] = 'active'
		title = 'Zest Open'
		events = Event.query.filter_by(category='zestopen').paginate(page=page, per_page=10)
		
	elif category == 'zestclose':
		active[2] = 'active'
		title = 'Zest Close'
		events = Event.query.filter_by(category='zestclose').paginate(page=page, per_page=10)

	if subcat != None:
		title = subcat.capitalize() + ' Events'
		events = Event.query.filter_by(subcategory=subcat).paginate(page=page, per_page=10)

	if events == None:
		flash('No events in your filter', category='info')
		title = 'All Zest Events'
		events = Event.query.all()

	if 'active' not in active:
		active[0] = 'active'

	last = ceil(events.total/pagelimit)

	
	return render_template('all_events.html', events=events, title=title, active=active, last_page=last)



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
