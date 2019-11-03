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
app.config['MAIL_USERNAME'] = 'akashraj5399@gmail.com'
#app.config['MAIL_PASSWORD'] = 'uxsaaqoabuaplxxz'
app.config['MAIL_PASSWORD'] = 'vgdvirbrjdlakbky'



db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
bcrypt = Bcrypt(app)
mail = Mail(app)


from zestpkg.main.routes import main
from zestpkg.users.routes import users
from zestpkg.profile.routes import profile
from zestpkg.event.routes import event
from zestpkg.contestant.routes import contestant
from zestpkg.team.routes import team
from zestpkg.errors.handlers import errors
from zestpkg.admin.routes import admin

app.register_blueprint(main)
app.register_blueprint(admin)
app.register_blueprint(users)
app.register_blueprint(profile)
app.register_blueprint(event)
app.register_blueprint(contestant)
app.register_blueprint(team)
app.register_blueprint(errors)
