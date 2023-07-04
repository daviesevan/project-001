from app import app
from flask import render_template
from flask_login import logout_user


# The home page route
@app.route('/')
def home():
    return render_template('index.html')





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