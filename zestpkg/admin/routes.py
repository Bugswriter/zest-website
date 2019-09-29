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

@login_required
@admin.route('/admin/users', methods=['GET', 'POST'])
def AdminUsers():
	AdminCheck()
	users = User.query.all()
	return render_template('AdminUsers.html', title='User View', users=users)

@login_required
@admin.route('/admin/user/<string:username>/toggleVerify', methods=['GET', 'POST'])
def toggleVerfiy(username):
	AdminCheck()
	user = User.query.filter_by(username=username).first()
	if user.verified:
		user.verified = False
	else:
		user.verified = True

	db.session.commit()
	
	return redirect(url_for('admin.AdminPannel'))
