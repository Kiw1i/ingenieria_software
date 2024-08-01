from flask import Blueprint

# Crear el blueprint para el proceso electoral
proceso_electoral_bp = Blueprint('proceso_electoral', __name__)

from . import proceso_electoral_controller
