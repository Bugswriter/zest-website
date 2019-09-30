from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from zestpkg.profile.forms import ProfileForm
from flask_login import current_user, login_required
from zestpkg import db
from zestpkg.models import Profile, User, Team 


team = Blueprint('team', __name__)

@team.route('/team/<int:tid>')
@login_required
def team_card(tid):
	team = Team.query.get_or_404(tid)
	members = team.getMember()
	if current_user in members:
		return render_template('team.html', team=team, members=members ,title=team.name)
	else:
		flash('You are not in this team! So access denied', category='warning')
		abort(500)