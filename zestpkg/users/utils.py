from zestpkg import mail
from flask_mail import Message
from flask import url_for, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

def send_confirmation_link(username, email, password):
	s=Serializer(current_app.config['SECRET_KEY'], 1800)
	token= s.dumps({'username': username,'email': email, 'password':password}).decode('utf-8')
	msg=Message('Verify your Account for Zest registeration account',
				sender='akashraj5399@gmail.com',
				recipients=[email])
	msg.body='''<h1>Zest2019</h1> To Confirm your Account, visit following link:
				<a href='{}'>Click here</a>
				If you did not make this request then simply ignore this email.
			'''.format(url_for('users.confirmation', token=token, _external=True))
	mail.send(msg)




def send_reset_email(user):
	token=user.get_reset_token()
	msg=Message('Password Reset Request',
				sender='akashraj5399@gmail.com',
				recipients=[user.email])
	msg.body='''
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
			To Reset your password, visit following link:
				<a href='{}'>Click here</a>
				If you did not make this request then simply ignore this email.
			'''.format(url_for('users.reset_token', token=token, _external=True))
	mail.send(msg)