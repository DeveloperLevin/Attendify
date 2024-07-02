from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'admins.login'
login_manager.login_message_category = 'info'

from attendance.admins.routes import admins
from attendance.main.routes import main

app.register_blueprint(main)
app.register_blueprint(admins, url_prefix='/admin')