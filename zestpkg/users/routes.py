from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app
from zestpkg.users.forms import RegisterForm, LoginForm
from flask_login import current_user, login_user, logout_user
from zestpkg import bcrypt, db
from zestpkg.models import User
from zestpkg.users.utils import send_confirmation_link
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))

	registerform = RegisterForm()
	if registerform.validate_on_submit():
		send_confirmation_link( registerform.username.data, registerform.email.data, registerform.password.data)
		flash(f"Conformation link is on your email", 'success')
		return redirect(url_for('users.login'))
	return render_template('register.html', title='Register', form=registerform)


@users.route('/register/<token>', methods=['GET'])
def confirmation(token):
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	s=Serializer(current_app.config['SECRET_KEY'])
	try:
		username=s.loads(token)['username']
		email=s.loads(token)['email']
		password=hashed_password = bcrypt.generate_password_hash(s.loads(token)['password']).decode('utf-8')
		user = User(username=username, email=email, password=hashed_password, verified=1)
		db.session.add(user)
		db.session.commit()
	except Exception as e:
		raise e
	return redirect(url_for('users.login'))


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