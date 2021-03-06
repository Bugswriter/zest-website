from flask import Blueprint, render_template, redirect, flash, request, redirect, url_for
from zestpkg import db
from zestpkg.contestant.utils import *
from zestpkg.models import User, Event, Contestant
from flask_login import login_required, current_user

@contestant.route('/event/<int:eid>/create_team', methods=['GET'])
@login_required
def createTeam(eid):
	if current_user.getProfile() == None:
		flash('You need to create your Profile Card first!', category='info')
		return redirect(url_for('profile.create_profile'))

	event = Event.query.get_or_404(eid)
	if event.eventType() == 'Solo':
		flash('You cannot create team in a solo event', category='info')
		abort(500)
		
	if request.args.get('team_name'):
		team_name = request.args.get('team_name')
		code = create_team(team_name, eid)
		flash(f'You and your team is registered for {event.title} event', category='success')
	else:
		flash('No team name is given by user', category='warning')
		abort(500)

	return redirect('/myevents')


@contestant.route('/event/<int:eid>/join_team')
@login_required
def joinTeam(eid):
	if current_user.getProfile() == None:
		flash('You need to create your Profile Card first!', category='info')
		return redirect(url_for('profile.create_profile'))
	
	event = Event.query.get_or_404(eid)
	if event.eventType() == 'Solo':
		flash('No teams in 	Solo events', category='warning')
		abort(500)

	if request.args.get('team_code'):
		team = verify_team_code(request.args.get('team_code'))
		take_participation(eid, request.args.get('team_code'))
		flash(f'You are registered in team {team.name}', category='success')

	return redirect('/myevents')
