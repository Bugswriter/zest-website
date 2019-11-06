from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from zestpkg.profile.forms import ProfileForm
from flask_login import current_user, login_required
from zestpkg import db
from zestpkg.models import Profile, User, Team, Event, Contestant
import string
import random

team = Blueprint('team', __name__)

@team.route('/team/<int:tid>')
@login_required
def team_card(tid):
	team = Team.query.get_or_404(tid)
	members = team.getMember()
	event = Event.query.get_or_404(team.event_id)
	if current_user in members or current_user.username == 'admin':
		return render_template('team.html', team=team, event=event, members=members ,title=team.name)
	else:
		flash('You are not in this team! So access denied', category='warning')
		abort(500)


@team.route('/team/create_team', methods=['POST', 'GET'])
@login_required
def createTeam():
	if current_user.profile == None:
		# Checking profile
		flash('You need to create your Profile Card first!', category='info')
		return redirect(url_for('profile.create_profile'))

	if request.method == 'POST':
		# Checking request method is POST 
		tname = request.form.get('team_name')
		eid = request.form.get('event_id')
		
		if tname == None or eid == None:
			# Checking form data exist
			flash('Wrong form data for creating team', category='danger')
			abort(500)
		

		# Checking event exist
		event = Event.query.get_or_404(eid)

		if len(current_user.participations) > 4:
			flash("Limit Reached - You are already in 5 events, can't register for more!", category='info')
			return redirect(url_for('event.my_events'))

		if event.eventType() == 'Solo':
			# checking event is not solo
			flash('You cannot create team in solo event', category='warning')
			abort(500)


		user_gender = current_user.profile.gender
		if event.gender != None and event.gender != user_gender:
			if event.gender == "M":
				flash('This event is only for Boys, check your profile', category="info")
			else:
				flash('This event is only for Girls, check your profile', category="info")
			
			return redirect(url_for('event.event_page', eid=event.id))
	

		contestant = Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first()	
		if contestant != None:
			# checking if user already in another team
			flash(f'You are already in a team of {event.title}!', category='warning')
			return redirect(url_for('team.team_card', tid=contestant.team_id))

		
		if Team.query.filter_by(name=tname).first() == None:
			# Checking if team already exist
			try:
				# Creating team
				teamsecret = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
				team = Team(name=tname, event_id=eid, team_code=teamsecret)
				db.session.add(team)
				db.session.commit()
				temp = Team.query.filter_by(name=tname, event_id=eid).first()
				code = temp.team_code
				contestant = Contestant(user_id=current_user.id, event_id=eid, team_id=team.id)
				db.session.add(contestant)
				db.session.commit()

				flash(f'Your team is added for {event.title} event successffully', category='success')
				return redirect(url_for('team.team_card', tid=team.id))

			except:
				flash('Database Error in creating team', category='danger')
				abort(403)
		else:
			flash(f'{tname} is taken, try any different team name', category='warning')
			return redirect(url_for('event.event_page', eid=eid))
	
	else:
		flash('Wrong method for accessing this page', category='warning')
		abort(403)




@team.route('/team/join_team', methods=['POST', 'GET'])
@login_required
def joinTeam():
	if current_user.getProfile() == None:
		# Checking Profile
		flash('You need to create your Profile Card first!', category='info')
		return redirect(url_for('profile.create_profile'))

	if request.method == 'POST':
		# Checking methos is post
		tcode = request.form.get('team_code')
		eid = request.form.get('event_id')
		if tcode == None or eid == None:
			# Checking if post data exist
			flash('Wrong form data for joining team', category='danger')
			abort(500)
	
		event = Event.query.get_or_404(eid)

		if len(current_user.participations) > 4:
			flash("Limit Reached - You are already in 5 events, can't register for more!", category='info')
			return redirect(url_for('event.my_events'))

		if event.eventType() == 'Solo':
			# if event is Solo
			flash('You are trying to join a team in Solo event', category='danger')
			abort(500)

		user_gender = current_user.profile.gender
		if event.gender != None and event.gender != user_gender:
			if event.gender == "M":
				flash('This event is only for Boys, check your profile', category="info")
			else:
				flash('This event is only for Girls, check your profile', category="info")

			return redirect(url_for('event.event_page', eid=event.id))

		
		team =	Team.query.filter_by(team_code=tcode).first()

		if team == None:
			# Team code validation check
			flash('Your Team Code is wrong check twice!', category='danger')
			return redirect(url_for('event.event_page', eid=event.id))

		if team.event_id != event.id:
			flash(f"Incorrect code! This code is not of {event.title} event's team.!", category="danger")
			return redirect(url_for('event.event_page', eid=event.id))

		if len(team.members) == event.team_limit:
			flash('This Team is full no space left for you!', category='info')
			return redirect(url_for('event.event_page', eid=event.id))

		uparty = Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first()
		if uparty == None:
			try:
				p = Contestant(user_id=current_user.id, event_id=eid, team_id=team.id)
				db.session.add(p)
				db.session.commit()
				flash(f'You successfully join the team {team.name}', category='success')

				return redirect(url_for('team.team_card', tid=team.id))
			except:
				flash('Database error something wrong try later!', category='danger')
				abort(403)
		else:
			if uparty.team_id == team.id:
				flash('You are already a member of this team!', category='success')
				return redirect(url_for('team.team_card', tid=team.id))
			else:
				flash(f'You are already a member of team <b>{team.name}</b> of <b>{event.title}</b> event!', category='info')
				return redirect(url_for('team.team_card', tid=uparty.team_id))

	else:
		flash('No data for joining team', category='warning')
		abort(500)


		
