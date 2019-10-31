from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app, abort
from zestpkg.users.forms import LoginForm, RequestResetForm, ResetPasswordForm
from flask_login import current_user, login_user, logout_user, login_required
from zestpkg import bcrypt, db
from zestpkg.models import *
from zestpkg.event.utils import *
from zestpkg.admin.utils import AdminCheck
from zestpkg.users.forms import RegisterForm
from zestpkg.event.forms import EventForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from math import ceil


admin = Blueprint('admin', __name__)

#only admin related

@admin.route('/admin', methods=['GET', 'POST'])
@admin.route('/admin/', methods=['GET', 'POST'])
@login_required
def AdminPannel():
	AdminCheck()
	number = {}
	number['user'] = db.session.query(User).count()
	number['event'] = db.session.query(Event).count()
	number['team'] = db.session.query(Team).count()
	number['contestant'] = db.session.query(Contestant).count()

	return render_template('AdminPannel.html', title='AdminPannel', **number)


'''
	 Admin User related
'''

@admin.route('/admin/users', methods=['GET', 'POST'])
@login_required
def AdminUsers():
	AdminCheck()
	page = request.args.get('page', 1, type=int)
	query = request.args.get('q')
	if query != None:
		users = User.query.filter(User.username.like('%' + query + '%')).paginate(page=page, per_page=10)
	else:
		users = User.query.paginate(page=page ,per_page=20)
	last = ceil(users.total/20)	
	return render_template('AdminUsers.html', title='User View', users=users, last_page=last)


@admin.route('/admin/usercreation', methods=['GET', 'POST'])
@login_required
def UserCreation():
	AdminCheck()
	form = RegisterForm()
	if form.validate_on_submit():	
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash("Account has been created for "+form.email.data, category='success')
		return redirect(url_for('admin.UserCreation'))
	return render_template('register.html', title='Admin user registeration', form=form)


@admin.route('/admin/user/<int:uid>/delete')
@login_required
def delete_account(uid):
	AdminCheck()
	user = User.query.get(uid)
	username = user.username
	profile = Profile.query.filter_by(user_id=uid).first()
	contestants = Contestant.query.filter_by(user_id=uid)
	events = Event.query.filter_by(user_id=uid)

	if user != None:
		db.session.delete(user)

	if profile != None:
		db.session.delete(profile)

	if contestants != None:
		for contestant in contestants:
			db.session.delete(contestant)

	if events != None:
		for event in events:
			event.user_id = 1

	db.session.commit()

	flash(f'{username} account has been been deleted!', category='success')
	return redirect(url_for('admin.AdminUsers'))


'''
admin event related
'''


@admin.route('/admin/events')
@login_required
def AdminEvents():
	AdminCheck()
	query = request.args.get('q')
	page = request.args.get('page', 1, type=int)
	if query != None:
		events = Event.query.filter(Event.title.like('%' + query + '%')).paginate(page=page, per_page=10)
	else:
		events = Event.query.paginate(page=page ,per_page=10)

	last = ceil(events.total/10)
	return render_template('AdminEvents.html', title='Events View', events=events, last_page=last)


@admin.route('/admin/event/add', methods=['GET', 'POST'])
@login_required
def add_event():
	AdminCheck()
	if current_user.getProfile() == None:
		flash('Create your profile first', category='info')
		return redirect(url_for('profile.create_profile'))

	form = EventForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.orguname.data).first()
		if user is not None:
			oid = user.id
		else:
			flash('Event form validate orguname filter not working', category='danger')
			abort(500)

		if form.image.data:
			picture = save_picture(form.image.data)
		else:
			picture = "default.jpg"
		try:	
			if form.status.data == 'T':
				form.status.data = True
			else:
				form.status.data = False

			event = Event(title=form.title.data, category=form.category.data, subcategory=form.subcategory.data ,image=picture, user_id=oid, team_limit=form.num_of_member.data, about=form.about.data, status=form.status.data)
			db.session.add(event)
			db.session.commit()
			flash('Your Event Registered Successfully!', 'success')
			return redirect('/')
		except:
			flash('Something went wrong into database', 'danger')
			abort(403)

	return render_template('addevent.html', form=form, title='Register Event')


@admin.route('/admin/event/<int:eid>/update', methods=['GET', 'POST'])
@login_required
def update_event(eid):
	AdminCheck()
	event = Event.query.get_or_404(eid)
	form = EventForm()
	if form.validate_on_submit():
		if form.image.data:
			event.image = save_picture(form.image.data)
		user=User.query.filter_by(username=form.orguname.data).first()		
		
		event.title = form.title.data
		event.user_id=user.id
		event.team_limit = form.num_of_member.data
		event.category = form.category.data
		event.subcategory = form.subcategory.data
		event.about = form.about.data
		if form.status.data == 'T':
			event.status = True
		else:
			event.status = False

		db.session.commit()
		flash('Your event is updated!', category='success')
		return redirect(url_for('event.event_page', eid=eid))

	elif request.method == 'GET':
		form.title.data = event.title
		form.orguname.data = event.getOrganizer().username
		form.num_of_member.data = event.team_limit
		form.category.data = event.category
		form.subcategory.data = event.subcategory
		form.about.data = event.about
		if event.status == True:
			form.status.data = 'T'
		else:
			form.status.data = 'F'

	return render_template('addevent.html', form=form, title='Update Event')



@admin.route('/admin/event/<int:eid>/delete')
@login_required
def delete_event(eid):
	AdminCheck()
	event = Event.query.get_or_404(eid)
	db.session.delete(event)
	db.session.commit()
	flash('Your event has been deleted', category='success')
	return redirect(url_for('event.all_events'))



@admin.route('/admin/verify/<string:username>/', methods=['GET', 'POST'])
@login_required
def toggleVerfiy(username):
	AdminCheck()
	user = User.query.filter_by(username=username).first()
	if user.verified:
		user.verified = False
	else:
		user.verified = True

	db.session.commit()
	
	return redirect(url_for('admin.AdminUsers'))


'''
Admin Team related
'''
@admin.route('/admin/teams')
@login_required
def AdminTeams():
	page = request.args.get('page', 1, type=int)
	teams = Team.query.paginate(page=page ,per_page=10)
	last = ceil(teams.total/10)
	return render_template('AdminTeams.html', title='Team View', teams=teams, last_page=last)



@admin.route('/admin/contestants')
@login_required
def AdminContestants():
	page = request.args.get('page', 1, type=int)
	contestants = Contestant.query.paginate(page=page ,per_page=10)
	last = ceil(contestants.total/10)
	return render_template('AdminContestants.html', title='Contestants View', contestants=contestants, last_page=last)