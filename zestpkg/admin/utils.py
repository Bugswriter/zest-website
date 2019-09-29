import secrets
import os
from flask_login import current_user
from flask import abort, current_app
from zestpkg.models import User 


def AdminCheck():
	if current_user.is_authenticated and current_user.username == 'rakash':
		return True
	else:
		abort(403)

