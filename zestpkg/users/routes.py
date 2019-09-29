from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app
from zestpkg.users.forms import RegisterForm, LoginForm, RequestResetForm, ResetPasswordForm
from flask_login import current_user, login_user, logout_user, login_required
from zestpkg import bcrypt, db
from zestpkg.models import User
from zestpkg.users.utils import send_confirmation_link, send_reset_email
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))

	registerform = RegisterForm()
	if registerform.validate_on_submit():
		send_confirmation_link( registerform.username.data, registerform.email.data, registerform.password.data)
		success = {'title': 'Confirmation link sended', 'heading': 'Confirmation Link sended', 'message': 'A email confirmation link has been sended to email address you used at the time of creating account'}
		return render_template('success.html', **success)
	return render_template('register.html', title='Register', form=registerform)


@users.route('/register/<token>', methods=['GET'])
def confirmation(token):
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	s = Serializer(current_app.config['SECRET_KEY'])
	try:
		username = s.loads(token)['username']
		email = s.loads(token)['email']
		password = hashed_password = bcrypt.generate_password_hash(s.loads(token)['password']).decode('utf-8')
		user = User(username=username, email=email, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash("You account has been created!", category='success')
	except Exception as e:
		flash("Sorry your link is expired, try again", category='danger')

	return redirect(url_for('users.login'))


@users.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))

	loginform = LoginForm()
	request_form = RequestResetForm()
	if loginform.validate_on_submit():
		user = User.query.filter_by(email=loginform.email.data).first()
		if user and bcrypt.check_password_hash(user.password, loginform.password.data):
			login_user(user, remember=loginform.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				if current_user.getProfile() == None:
					flash("Please create your profile card", category='info')
					return redirect('/create_profile')
					
				return redirect(url_for('main.home'))
		else:
			flash(f'Login Unsuccessful. Please check email or password', 'danger')
			return render_template('login.html', title='Login', form=loginform, request_form=request_form)


	if request_form.validate_on_submit():
		user=User.query.filter_by(email=request_form.email.data).first()
		send_reset_email(user)
		success = {}
		success['heading'] = "Email has been sended"
		success['message'] = "Check your email, there will be further instruction for reseting your password. Be quick link will expires in 10 min"
		return render_template('success.html', **success)

	return render_template('login.html', title='Login', form=loginform, request_form=request_form)


@users.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.home'))


@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form=RequestResetForm()
	
	return render_template('reset_request.html', title='Reset password', form=form)

@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	user=User.verify_reset_token(token)
	if user is None:
		flash('That is an invalid or expired token', 'warning')
		return redirect(url_for('users.login'))
	form=ResetPasswordForm()
	if form.validate_on_submit():
		hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user.password=hashed_password
		db.session.commit()
		flash("your account has been Updated! you are now able to log in", 'success')
		return redirect(url_for('users.login'))
	return render_template('reset_token.html', title='Reset Password', form=form)


@users.route('/account')
@login_required
def account():
	user = User.query.get_or_404(current_user.id)
	render_template('account.html', user=user)