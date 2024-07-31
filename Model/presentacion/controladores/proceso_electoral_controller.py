from flask import Blueprint, request, jsonify
from servicios.Iproceso_electoral import Iproceso_electoral
from servicios.proceso_electoral_servicio import ProcesoElectoralServicio

# Crear un blueprint para los procesos electorales
proceso_electoral_bp = Blueprint('proceso_electoral', __name__)

class ProcesoElectoralController:
    def __init__(self):
        self.servicio = ProcesoElectoralServicio()

    @proceso_electoral_bp.route('/procesos-electorales', methods=['GET'])
    def obtener_procesos(self):
        """
        Obtener todos los procesos electorales.
        """
        try:
            procesos = self.servicio.obtener_todos()
            return jsonify(procesos)
        except Exception as e:
            return jsonify({"error": "Error al obtener procesos electorales: " + str(e)}), 500

    @proceso_electoral_bp.route('/procesos-electorales', methods=['POST'])
    def crear_proceso(self):
        """
        Crear un nuevo proceso electoral.
        """
        try:
            data = request.json
            # Validación de datos
            if not data.get('nombre') or not data.get('fecha'):
                return jsonify({"error": "Faltan campos obligatorios: nombre y fecha"}), 400

            nuevo_proceso = self.servicio.crear(data)
            return jsonify(nuevo_proceso), 201
        except Exception as e:
            return jsonify({"error": "Error al crear proceso electoral: " + str(e)}), 400

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>', methods=['PUT'])
    def actualizar_proceso(self, id):
        """
        Actualizar un proceso electoral existente.
        """
        try:
            data = request.json
            proceso_actualizado = self.servicio.actualizar(id, data)
            return jsonify(proceso_actualizado)
        except Exception as e:
            return jsonify({"error": "Error al actualizar proceso electoral: " + str(e)}), 400

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>', methods=['DELETE'])
    def eliminar_proceso(self, id):
        """
        Eliminar un proceso electoral existente.
        """
        try:
            self.servicio.eliminar(id)
            return '', 204
        except Exception as e:
            return jsonify({"error": "Error al eliminar proceso electoral: " + str(e)}), 400

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>/detalle', methods=['GET'])
    def obtener_detalle_proceso(self, id):
        try:
            detalle = self.servicio.obtener_detalle(id)
            return jsonify(detalle)
        except Exception as e:
            return jsonify({"error": "Error al obtener detalle del proceso electoral: " + str(e)}), 500

# Uso
controller = ProcesoElectoralController()
