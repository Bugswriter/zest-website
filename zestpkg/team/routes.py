from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from zestpkg.profile.forms import ProfileForm
from flask_login import current_user, login_required
from zestpkg import db
from zestpkg.models import Profile, User, Team, Event, Contestant
from zestpkg.contestant.utils import joinParty


team = Blueprint('team', __name__)

@team.route('/team/<int:tid>')
@login_required
def team_card(tid):
	team = Team.query.get_or_404(tid)
	members = team.getMember()
	event = Event.query.get_or_404(team.event_id)
	if current_user in members:
		return render_template('team.html', team=team, event=event, members=members ,title=team.name)
	else:
		flash('You are not in this team! So access denied', category='warning')
		abort(500)


@team.route('/team/create_team', methods=['POST', 'GET'])
@login_required
def createTeam():
	if current_user.getProfile() == None:
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
		else:
			# Checking event exist
			event = Event.query.get_or_404(eid)
			if event.eventType() == 'Solo':
				# checking event is not solo
				flash('You cannot create team in solo event', category='warning')
				abort(500)
			else:
				contestant = Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first()	
				if contestant == None:
					# checking if user already in another team
					if Team.query.filter_by(name=tname).first() == None:
						# Checking if team already exist
						try:
							# Creating team
							team = Team(name=tname, event_id=eid)
							db.session.add(team)
							db.session.commit()
							team = Team.query.filter_by(name=tname).first()
							joinParty(eid, team.team_code)
							flash(f'Your team is added for {event.title} event successffully', category='success')
							
							return redirect(url_for('team.team_card', tid=team.id))

						except:
							flash('Database Error in creating team', category='danger')
							abort(403)
				else:
					flash(f'You are already in a team of {event.title}!', category='warning')
					return redirect(url_for('team.team_card', tid=contestant.team_id))

	
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
		else:
			event = Event.query.get_or_404(eid)
			if event.eventType() == 'Solo':
				# if event is Solo
				flash('You are trying to join a team in Solo event?? wtf', category='danger')
				abort(500)
			else:
				team =	Team.query.filter_by(team_code=tcode).first()
				if team == None:
					# Team code validation check
					flash('You Team Code is wrong check twice!', category='danger')
					return redirect(url_for('event.event_page', eid=event.id))
				else:
					if Contestant.query.filter_by(user_id=current_user.id, event_id=eid).first() == None:
						try:
							# Making a contestant in that team
							joinParty(event.id, tcode)
							flash('Successfully Join the team', category='success')

							return redirect(url_for('team.team_card', tid=team.id))
						except:
							flash('Database error something wrong try later!', category='danger')
							abort(403)
					else:
						flash('You are already a member of this team!', category='success')

						return redirect(url_for('team.team_card', tid=team.id))

	else:
		flash('No data for joining team', category='warning')
		abort(500)


		