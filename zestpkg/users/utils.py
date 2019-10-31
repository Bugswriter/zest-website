from zestpkg import mail
from flask_mail import Message
from flask import url_for, current_app, render_template
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

def send_confirmation_link(username, email, password):
	s=Serializer(current_app.config['SECRET_KEY'], 1800)
	token= s.dumps({'username': username,'email': email, 'password':password}).decode('utf-8')
	msg = Message('Confirm your email',
				sender='admin@zest2019.in',
				recipients=[email])
	data = {'username': username, 'token': token}
	msg.html = render_template('account_email.html', **data)
	mail.send(msg)


def send_reset_email(user):
	token=user.get_reset_token()
	msg = Message('Password Reset Request',
				sender='admin@zest2019.in',
				recipients=[user.email])
	data = {'username': user.username, 'token': token}
	msg.html = render_template('reset_pass_email.html', **data)
	mail.send(msg)