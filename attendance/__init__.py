from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345"

from attendance.admins.routes import admins
from attendance.main.routes import main

app.register_blueprint(main)
app.register_blueprint(admins, url_prefix='/admin')