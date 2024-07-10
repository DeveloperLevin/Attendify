from flask import Blueprint, url_for, render_template
from attendance.admins.forms import RegistrationForm, LoginForm, UpdateForm, DeleteForm, CreateForm
from flask_login import login_required, current_user

admins = Blueprint('admins', __name__)

@admins.route("/home")
def admin_home():
    return render_template('adminhome.html', title="Admin Home")

@admins.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateForm()
    return render_template('create.html', title='Add Student', form=form)

@admins.route("/delete", methods=['GET', 'POST'])
def delete():
    form = DeleteForm()
    return render_template('delete.html', title='Delete Student', form=form)

@admins.route("/update", methods=['GET', 'POST'])
def update():
    form = UpdateForm()
    return render_template('update.html', title='Update Student', form=form)


