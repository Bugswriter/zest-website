from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app
from zestpkg.users.forms import LoginForm, RequestResetForm, ResetPasswordForm
from flask_login import current_user, login_user, logout_user, login_required
from zestpkg import bcrypt, db
from zestpkg.admin.utils import AdminCheck
from zestpkg.models import User, Event
from zestpkg.users.forms import RegisterForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


admin = Blueprint('admin', __name__)


@admin.route('/admin', methods=['GET', 'POST'])
@admin.route('/admin/', methods=['GET', 'POST'])
@login_required
def AdminPannel():
	AdminCheck()
	return render_template('AdminPannel.html', title='AdminPannel')

@login_required
@admin.route('/admin/users', methods=['GET', 'POST'])
def AdminUsers():
	AdminCheck()
	users = User.query.all()
	return render_template('AdminUsers.html', title='User View', users=users)




@login_required
@admin.route('/admin/events')
def AdminEvents():
	AdminCheck()
	events = Event.query.all()
	return render_template('AdminEvents.html', title='Events View', events=events)




@login_required
@admin.route('/admin/verify/<string:username>/', methods=['GET', 'POST'])
def toggleVerfiy(username):
	AdminCheck()
	user = User.query.filter_by(username=username).first()
	if user.verified:
		user.verified = False
	else:
		user.verified = True

	db.session.commit()
	
	return redirect(url_for('admin.AdminPannel'))


@login_required
@admin.route('/admin/usercreation', methods=['GET', 'POST'])
def UserCreation():
	form = RegisterForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash("Account has been created for "+form.email.data, category='success')
		return redirect(url_for('admin.UserCreation'))
	return render_template('register.html', title='Register', form=form)
	