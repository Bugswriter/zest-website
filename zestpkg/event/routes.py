from flask import Blueprint, render_template, redirect, flash
from flask_login import current_user
from zestpkg.event.forms import EventForm
from zestpkg.models import Event

event = Blueprint('event', __name__)

@event.route('/events')
def show_event():
	events = Event.query.all()
	return render_template('events.html', events=events)


@event.route('/addevent', methods=['GET', 'POST'])
def add_event():
	#if current_user.verified:
	form = EventForm()
	if form.validate_on_submit():
		event = Event(title=form.title.data, image='default.jpg', user_id=current_user.id, team_limit=form.num_of_member.data)
		flash('Your Event Registered Successfully!', 'success')
		return redirect('/')

	return render_template('addevent.html', form=form, title='Register Event')


