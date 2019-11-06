import getpass
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
	active = ['','','','']
	query = request.args.get('q')
	if query != None:
		title = "Search results for '" + query + "'"
		events = Event.query.filter(Event.title.like('%' + query + '%')).paginate(page=page, per_page=10)

	else:
		category = request.args.get('cat')
		subcat = request.args.get('subcat')
		events = Event.query.paginate(page=page, per_page=pagelimit)
		cat = ''
		title = 'All Zest Events'

		if category == 'aamod':
			active[3] = 'active'
			title = 'Aamod Events'
			cat = 'aamod'
			events = Event.query.filter_by(category='aamod').paginate(page=page, per_page=10)

		elif category == 'zestopen':
			active[1] = 'active'
			title = 'Zest Open'
			cat = 'zestopen'
			events = Event.query.filter_by(category='zestopen').paginate(page=page, per_page=10)
			
		elif category == 'zestclose':
			active[2] = 'active'
			title = 'Zest Close'
			cat = 'zestclose'
			events = Event.query.filter_by(category='zestclose').paginate(page=page, per_page=10)

		if subcat != None:
			title = subcat.capitalize() + ' Events'
			events = Event.query.filter_by(subcategory=subcat).paginate(page=page, per_page=10)

		if events == None:
			cat = ''
			flash('No events in your filter', category='info')
			title = 'All Zest Events'
			events = Event.query.paginate(page=page, per_page=pagelimit)

		if 'active' not in active:
			active[0] = 'active'

	last = ceil(events.total/pagelimit)
	
	return render_template('all_events.html', events=events, title=title, active=active, last_page=last, cat=cat)



@event.route('/event/<int:eid>')
def event_page(eid):
	event = Event.query.get_or_404(eid)
	title = event.title
	profile = Profile.query.filter_by(user_id=event.getOrganizer().id).first()
	notreg = True
	if current_user.is_authenticated:
		x = Contestant.query.filter_by(user_id=current_user.id, event_id=event.id).first()
		if x:
			notreg = False

	return render_template('eventpage.html', event=event, rules=event.rules, user=profile, notreg=notreg, title=title)


@event.route('/event/my', methods=['GET', 'POST'])
@login_required
def my_events():
	return render_template('myevents.html', participations=current_user.participations, title="My Events")



@event.route('/event/<string:eid>/participants')
@login_required
def participant_list(eid):
	event = Event.query.get_or_404(eid)
	if event.eventType() == 'Solo':
		contestants = event.getParticipants()
		return render_template('participants.html', contestants=contestants, event=event)
	else:
		teams = event.getParticipants()
		print(teams)
		return render_template('teamlist.html', teams=teams, event=event)



@event.route('/event/<string:eid>/generate_sheet')
@login_required
def generate_excel(eid):
	if current_user.verified != True:
		flash("Your account is not verified", category='warning')
		abort(500)


	event = Event.query.get_or_404(eid)
	if event.eventType() == 'Solo':
		fileName = "/home/"+ getpass.getuser() +"/zest-website/zestpkg/static/sheets/"+event.title.upper() + "-" + str(event.id) + ".csv"
		print(fileName)
		niggas = event.getParticipants()
		sheet = generate_sheet_solo(fileName, niggas)

	return redirect(url_for('static', filename='sheets/'+event.title.upper() + "-" + str(event.id) + ".xlsx"))

