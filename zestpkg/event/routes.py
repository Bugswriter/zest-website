from flask import Blueprint, render_template, redirect, flash, request, abort, url_for
from flask_login import current_user, login_required
from zestpkg.event.forms import EventForm
from zestpkg import db
from zestpkg.models import Event, Profile, Team, Contestant
from zestpkg.event.utils import *

event = Blueprint('event', __name__)

@event.route('/events')
@event.route('/events/')
def all_events():
	events = Event.query.all()
	return render_template('all_events.html', events=events)


@event.route('/event/<int:eid>')
def event_page(eid):
	event = Event.query.get_or_404(eid)
	profile = Profile.query.filter_by(user_id=event.getOrganizer().id).first()
	return render_template('eventpage.html', event=event, user=profile)


@event.route('/event/my', methods=['GET', 'POST'])
@login_required
def my_events():
	return render_template('myevents.html', events=current_user.getEvents())


@event.route('/event/add', methods=['GET', 'POST'])
@login_required
def add_event():
	if not current_user.verified:
		abort(500)

	if current_user.getProfile() == None:
		flash('Create your profile first', category='info')
		return redirect(url_for('profile.create_profile'))

	form = EventForm()
	if form.validate_on_submit():
		if form.image.data:
			picture = save_picture(form.image.data)
		else:
			picture = "default.jpg"

		event = Event(title=form.title.data, image=picture, user_id=current_user.id, team_limit=form.num_of_member.data, detail_txt=form.about.data, price=form.price.data)
		db.session.add(event)
		db.session.commit()
		flash('Your Event Registered Successfully!', 'success')
		return redirect('/')

	return render_template('addevent.html', form=form, title='Register Event')


@event.route('/event/<int:eid>/update', methods=['GET', 'POST'])
@login_required
def update_event(eid):
	if current_user.getProfile() == None:
		flash('Create your profile first', category='info')
		return redirect('/create_profile')

	event = Event.query.get_or_404(eid)
	if current_user.id != event.user_id:
		abort(500)

	form = EventForm()
	if form.validate_on_submit():
		event.title = form.title.data
		if form.image.data:
			event.image = save_picture(form.image.data)
		
		event.team_limit = form.num_of_member.data
		event.detail_txt = form.about.data

		db.session.commit()
		flash('Your event is updated!', category='success')
		return redirect('/event')

	elif request.method == 'GET':
		form.title.data = event.title
		form.num_of_member.data = event.team_limit
		form.about.data = event.detail_txt

		return render_template('addevent.html', form=form, title='Update Event')



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