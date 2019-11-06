import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_compress import Compress

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://bugswriter:Suraj_20@bugswriter.mysql.pythonanywhere-services.com/bugswriter$default"
app.config['SECRET_KEY'] = "9be8f28f87c515b14ea6bf8a647fdcf5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['COMPRESS_MIMETYPES'] = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
app.config['COMPRESS_LEVEL'] = 6
app.config['COMPRESS_MIN_SIZE'] = 500
app.config['MAIL_USERNAME'] = 'admin@zest2019.in'
app.config['MAIL_PASSWORD'] = 'uxsaaqoabuaplxxz' # admin@zest2019.in
#app.config['MAIL_PASSWORD'] = 'vgdvirbrjdlakbky' #akashraj5399
#app.config['MAIL_PASSWORD'] = 'ypuhhcnuxhawaswq' #zest2k19@gmail.com



db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
Compress(app)
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
