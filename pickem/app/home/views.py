# app/home/views.py

from flask import render_template, request
from flask_login import login_required
from .. import models
from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/settings')
def settings():
    """
    Render the settings page on the settings route
    """
    return render_template('home/settings.html', my_name='Isaac')

@home.route('/say_hello', methods=['GET', 'POST'])
def say_hello():
    newUserName = request.form['newUserName']
    print("newUserName")
    return render_template('home/settings.html', my_name=newUserName)

