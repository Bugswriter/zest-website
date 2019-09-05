from flask import Blueprint, render_template, redirect, flash, request, abort
from flask_login import current_user, login_required
from zestpkg.event.forms import EventForm
from zestpkg import db
from zestpkg.models import Event, Profile, Team, Participants
from zestpkg.event.utils import save_picture, getProfile

event = Blueprint('event', __name__)

@event.route('/events')
def show_event():
	events = Event.query.all()
	return render_template('events.html', events=events)


@event.route('/events/<int:eid>')
def eventpage(eid):
	event = Event.query.get_or_404(eid)
	profile = Profile.query.filter_by(user_id=event.getOrganizer().id).first()
	return render_template('eventpage.html', event=event, user=profile)


@event.route('/addevent', methods=['GET', 'POST'])
@login_required
def add_event():
	#if current_user.verified:
	form = EventForm()
	if form.validate_on_submit():
		if form.image.data:
			event.image = save_picture(form.image.data)
		else:
			event.image = "default.png"

		event = Event(title=form.title.data, image=picture, user_id=current_user.id, team_limit=form.num_of_member.data, detail_txt=form.about.data)
		db.session.add(event)
		db.session.commit()
		flash('Your Event Registered Successfully!', 'success')
		return redirect('/')

	return render_template('addevent.html', form=form, title='Register Event')


@event.route('/events/<int:eid>/update', methods=['GET', 'POST'])
@login_required
def update_event(eid):
	event = Event.query.get_or_404(eid)
	if current_user.id != event.user_id:
		abort(403)

	form = EventForm()
	if form.validate_on_submit():
		event.title = form.title.data
		if form.image.data:
			event.image = save_picture(form.image.data)
		else:
			event.image = "default.png"
		
		event.team_limit = form.num_of_member.data
		event.detail_txt = form.about.data

		db.session.commit()
		flash('Your event is updated!', category='success')
		return redirect('/events')

	elif request.method == 'GET':
		form.title.data = event.title
		form.num_of_member.data = event.team_limit
		form.about.data = event.detail_txt

		return render_template('addevent.html', form=form, title='Update Event')


@event.route('/events/<int:eid>/create_team')
@login_required
def create_team(eid):
	event = Event.query.get_or_404(eid)
	team_name = request.args.get('team_name')
	if team_name == None or event.team_limit == 1:
		abort(403)
	

	team = Team.query.filter_by(name=team_name).first()
	if team == None:
		team = Team(name=team_name, event_id=eid)
		db.session.add(team)
		db.session.commit()
		team = Team.query.filter_by(name=team_name).first()
		x = Participants(user_id=current_user.id, event_id=eid, team_id=team.id)
		db.session.add(x)
		db.session.commit()
		success = {}
		success['heading'] = "Your team is registered"
		success['message'] = "Your team's secret code is: "+ team.team_code

		return render_template('success.html', **success)

	else:
		flash('Team with this name already exist', 'danger')
		return redirect('/events/'+str(eid))




@event.route('/events/<int:eid>/join_team')
@login_required
def join_team(eid):
	event = Event.query.get_or_404(eid)
	if event.team_limit == 1:
		abort(403)
	code = request.args.get('team_code')
	team = Team.query.filter_by(team_code=code).first_or_404()

	if code == None or team.event_id != eid:
		abort(403)
	
	
	x = Participants(user_id=current_user.id, event_id=eid, team_id=team.id)
	db.session.add(x)
	db.session.commit()
	success = {}
	success['heading'] = "Your team is registered"
	success['message'] = "<h3>Your team's secret code is: "+ team.team_code +"</h3>"

	return render_template('success.html', )






