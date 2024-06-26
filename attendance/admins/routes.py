from flask import Blueprint, url_for, render_template

admins = Blueprint('admins', __name__)

@admins.route("/home")
def admin_home():
    return render_template('home.html', title="Admin Home")

@admins.route("/create")
def create():
    return render_template('create.html', title='Add Student')

@admins.route("/delete")
def delete():
    return render_template('delete.html', title='Add Student')

@admins.route("/update")
def update():
    return render_template('update.html', title='Add Student')


