from flask import Blueprint, url_for, render_template
from attendance.admins.forms import RegistrationForm, LoginForm, UpdateForm, DeleteForm, CreateForm

admins = Blueprint('admins', __name__)

@admins.route("/home")
@login_required
def admin_home():
    return render_template('home.html', title="Admin Home")

@admins.route("/create")
@login_required
def create():
    form = CreateForm()
    return render_template('create.html', title='Add Student', form=form)

@admins.route("/delete")
@login_required
def delete():
    form = DeleteForm()
    return render_template('delete.html', title='Add Student', form=form)

@admins.route("/update")
@login_required
def update():
    form = UpdateForm()
    return render_template('update.html', title='Add Student', form=form)


