from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app
from zestpkg.users.forms import LoginForm, RequestResetForm, ResetPasswordForm
from flask_login import current_user, login_user, logout_user, login_required
from zestpkg import bcrypt, db
from zestpkg.admin.utils import AdminCheck
from zestpkg.models import User

admin = Blueprint('admin', __name__)


@admin.route('/admin', methods=['GET', 'POST'])
@admin.route('/admin/', methods=['GET', 'POST'])
@login_required
def AdminPannel():
	AdminCheck()
	return render_template('AdminPannel.html', title='AdminPannel')

@admin.route('/admin/login', methods=['GET', 'POST'])
def AdminLogin():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))

	loginform = LoginForm()
	request_form = RequestResetForm()
	if loginform.validate_on_submit():	
		user = User.query.filter_by(email=loginform.email.data).first()
		if user and bcrypt.check_password_hash(user.password, loginform.password.data) and user.username=='rakash':
			login_user(user, remember=loginform.remember.data)
			return redirect(url_for('admin.AdminPannel'))
		flash(f'Login Unsuccessful. Please check email or password', 'danger')
		return render_template('login.html', title='Login', form=loginform, request_form=request_form)
	else:
		flash(f'Login Unsuccessful. Please check email or password', 'danger')
		return render_template('login.html', title='Login', form=loginform, request_form=request_form)


@login_required
@admin.route('/admin/users', methods=['GET', 'POST'])
def AdminUsers():
	AdminCheck()
	users=User.query.all()
	return render_template('AdminUsers.html', title='User View', users=users)

@login_required
@admin.route('/admin/users/verified/<string:username>', methods=['GET', 'POST'])
def UserVerifier(username):
	AdminCheck()
	user = User.query.filter_by(username=username).first()
	user.verified=True
	db.session.commit()
	return redirect(url_for('admin.AdminPannel'))
