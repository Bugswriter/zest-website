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
	return render_template('AdminPannel.html', title='AdminPannel')


#admin user related

@admin.route('/admin/users', methods=['GET', 'POST'])
@login_required
def AdminUsers():
	AdminCheck()
	users = User.query.all()
	
	return render_template('AdminUsers.html', title='User View', users=users)


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


#admin event related



@admin.route('/admin/events')
@login_required
def AdminEvents():
	AdminCheck()
	page = request.args.get('page', 1, type=int)
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
			event = Event(title=form.title.data, category=form.category.data, subcategory=form.subcategory.data ,image=picture, user_id=oid, team_limit=form.num_of_member.data, about=form.about.data)
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
	event = Event.query.get_or_404(eid)
	if current_user.username != 'admin' or current_user.id != event.user_id:
		flash("You are not allowed on this page!", category='danger')
		abort(500)

	if current_user.getProfile() == None:
		flash('Create your profile first', category='info')
		return redirect('/create_profile')

	form = EventForm()


	if form.validate_on_submit():
		if user is not None:
			oid = user.id
		else:
			flash('Event form validate orguname filter not working', category='danger')
			abort(500)

		event.title = form.title.data
		if form.image.data:
			event.image = save_picture(form.image.data)
		
		event.team_limit = form.num_of_member.data
		event.user_id = oid
		event.category = form.category.data
		event.subcategory = form.subcategory.data
		event.about = form.about.data

		db.session.commit()
		flash('Your event is updated!', category='success')
		return redirect('/event')

	elif request.method == 'GET':
		form.title.data = event.title
		user = User.query.get_or_404(event.user_id)
		form.orguname.data = user.username
		form.num_of_member.data = event.team_limit
		event.category = form.category.data
		event.subcategory = form.subcategory.data
		form.about.data = event.about

		return render_template('addevent.html', form=form, title='Update Event')




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
	
	return redirect(url_for('admin.AdminPannel'))




	