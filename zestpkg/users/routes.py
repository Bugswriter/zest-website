from flask import Blueprint, render_template, flash, request, redirect, url_for
from zestpkg.users.forms import RegisterForm, LoginForm
from flask_login import current_user, login_user, logout_user
from zestpkg import bcrypt, db
from zestpkg.models import User

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))

	registerform = RegisterForm()
	if registerform.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(registerform.password.data).decode('utf-8')
		user = User(username=registerform.username.data, email=registerform.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'You are successfully registered', 'success')

		return render_template(url_for('users.login'))

	return render_template('register.html', title='Register', form=registerform)


@users.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))

	loginform = LoginForm()

	if loginform.validate_on_submit():
		user = User.query.filter_by(email=loginform.email.data).first()
		if user and bcrypt.check_password_hash(user.password, loginform.password.data):
			login_user(user, remember=loginform.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('main.home'))

		else:
			flash(f'Login Unsuccessful. Please check email or password', 'danger')

	return render_template('login.html', title='Login', form=loginform)


@users.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.home'))