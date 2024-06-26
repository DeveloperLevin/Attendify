from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

# Home route
@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title="Home")

@main.route("/attendify")
def video():
    return render_template('camera.html', title="video")
