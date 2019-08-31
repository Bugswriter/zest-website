from flask import Blueprint, render_template, redirect, flash, request
from flask_login import current_user, login_required
from zestpkg.event.forms import EventForm
from zestpkg import db
from zestpkg.models import Event
from zestpkg.event.utils import save_picture, getProfile

event = Blueprint('event', __name__)

@event.route('/events')
def show_event():
	events = Event.query.all()
	return render_template('events.html', events=events)


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


@event.route('/<int:eid>/update', methods=['GET', 'POST'])
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

