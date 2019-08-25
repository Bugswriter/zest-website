import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SECRET_KEY'] = "9be8f28f87c515b14ea6bf8a647fdcf5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
bcrypt = Bcrypt(app)
mail = Mail(app)


from zestpkg.main.routes import main
from zestpkg.users.routes import users
from zestpkg.profile.routes import profile
from zestpkg.errors.handlers import errors

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(profile)
app.register_blueprint(errors)