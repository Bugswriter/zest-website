from datetime import datetime
from flask import Blueprint, render_template, jsonify, request
from shutil import copy
from zestpkg import db
from zestpkg.models import *
from flask_login import login_required
from zestpkg.main.forms import PIDSearch

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
	return render_template('home.html', title='home')


@main.route('/stats', methods=['GET', 'POST'])
def stats():
	return render_template('stats.html', title='Statistics')

@main.route('/faq')
def faq():
	return render_template('faq.html', title='FAQ')


@main.route('/backup')
@login_required
def backup():
	copy('zestpkg/site.db','zestpkg/static/backup')
	return "<h2>Last backup: " + str(datetime.now()) + "</h2>"


@main.route('/account/<int:pid>')
def pid_detail(pid):
	user = User.query.get(pid)
	if user==None:
		return "<h1>No PID found</h1>"

	return render_template('pid_pass.html',user=user, contestants=user.participations, title='PID Pass')


@main.route('/getinfo', methods=['POST', 'GET'])
def getinfo():
	form = PIDSearch()
	pid = None
	if form.validate_on_submit():
		pid = form.pid.data
		user = User.query.get(pid)
		if user == None:
			flash('Form Validation for PID failed, call admin now!', category='danger')
			abort(403)

	return render_template('getinfo.html', title='PID Pass', form=form, pid=pid)