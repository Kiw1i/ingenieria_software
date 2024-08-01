from flask import Blueprint, render_template

proceso_electoral_bp = Blueprint('proceso_electoral', __name__)

@proceso_electoral_bp.route('/administrador/eleccion/')
def administrador_eleccion():
    return render_template('administrador_eleccion.html')

@proceso_electoral_bp.route('/eleccion/')
def eleccion():
    return render_template('eleccion.html')

@proceso_electoral_bp.route('/registro/electoral/')
def registro_electoral():
    return render_template('registro_electoral.html')

@proceso_electoral_bp.route('/resultados/')
def resultados():
    return render_template('resultados.html')
