from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    user = {"username": "John Doe"}  # Ejemplo de un usuario
    return render_template('profile.html', user=user)
