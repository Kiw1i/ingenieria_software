from flask import Blueprint, render_template

participantes_bp = Blueprint('participantes', __name__)

@participantes_bp.route('/modificar/perfil/')
def modificar_perfil():
    return render_template('modificar_perfil.html')

@participantes_bp.route('/registrar/candidato/')
def registrar_candidato():
    return render_template('registrar_candidato.html')

@participantes_bp.route('/registrar/elector/')
def registrar_elector():
    return render_template('registrar_elector.html')
