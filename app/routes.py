from app import app
from flask import render_template, flash, redirect, url_for, request
from flask_login import logout_user


# The home page route
@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error-404.html'), 404

# The dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('index-2.html')

#Routes for the doctors
@app.route('/doctors')
def doctors():
    return render_template('doctors.html')


# Routes for patients
@app.route('/patients')
def patients():
    return render_template('patients.html')

@app.route('/appointments')
def appointments():
    return render_template('appointments.html')


@app.route('/schedule')
def schedule():
    return render_template('schedule.html')


@app.route('/departments')
def departments():
    return render_template('departments.html')



# My profile route
@app.route('/my-profile')
def my_profile():
    return render_template('profile.html')




# Edit profile route
@app.route('/edit-profile')
def edit_profile():
    return render_template('edit-profile.html')




# Settings route
@app.route('/settings')
def settings():
    return render_template('settings.html')





# Logout Route 
@app.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')