from zestpkg import mail
from flask_mail import Message
from flask import url_for, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

def send_confirmation_link(username, email, password):
	s=Serializer(current_app.config['SECRET_KEY'], 1800)
	token= s.dumps({'username': username,'email': email, 'password':password}).decode('utf-8')
	msg=Message('Verify your Account of HungryNigga',
				sender='akashraj5399@gmail.com',
				recipients=[email])
	msg.body='''To Confirm your Account, visit following link:
					{}
				If you did not make this request then simply ignore this email.
			'''.format(url_for('users.confirmation', token=token, _external=True))
	mail.send(msg)