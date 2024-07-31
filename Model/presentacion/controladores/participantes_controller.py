from flask import Blueprint, request, jsonify
from servicios.participantes_servicio import ParticipantesServicio

# Crear un blueprint para los participantes
participantes_bp = Blueprint('participantes', __name__)

class ParticipantesController:
    def __init__(self):
        self.servicio = ParticipantesServicio()

    @participantes_bp.route('/participantes', methods=['GET'])
    def obtener_participantes(self):
        """
        Obtener todos los participantes.
        """
        try:
            participantes = self.servicio.obtener_todos()
            return jsonify(participantes)
        except Exception as e:
            return jsonify({"error": "Error al obtener participantes: " + str(e)}), 500

    @participantes_bp.route('/participantes', methods=['POST'])
    def crear_participante(self):
        try:
            data = request.json
            # Validación de datos
            if not data.get('nombre') or not data.get('edad'):
                return jsonify({"error": "Faltan campos obligatorios: nombre y edad"}), 400
            if not isinstance(data.get('edad'), int):
                return jsonify({"error": "El campo edad debe ser un número entero"}), 400

            nuevo_participante = self.servicio.crear(data)
            return jsonify(nuevo_participante), 201
        except Exception as e:
            return jsonify({"error": "Error al crear participante: " + str(e)}), 400

            
    @participantes_bp.route('/participantes/<int:id>', methods=['PUT'])
    def actualizar_participante(self, id):
        """
        Actualizar un participante existente.
        """
        try:
            data = request.json
            participante_actualizado = self.servicio.actualizar(id, data)
            return jsonify(participante_actualizado)
        except Exception as e:
            return jsonify({"error": "Error al actualizar participante: " + str(e)}), 400

    @participantes_bp.route('/participantes/<int:id>', methods=['DELETE'])
    def eliminar_participante(self, id):
        """
        Eliminar un participante existente.
        """
        try:
            self.servicio.eliminar(id)
            return '', 204
        except Exception as e:
            return jsonify({"error": "Error al eliminar participante: " + str(e)}), 400

    @participantes_bp.route('/participantes/<int:id>/detalle', methods=['GET'])
    def obtener_detalle_participante(self, id):
        try:
            detalle = self.servicio.obtener_detalle(id)
            return jsonify(detalle)
        except Exception as e:
            return jsonify({"error": "Error al obtener detalle del participante: " + str(e)}), 500

# Uso
controller = ParticipantesController()
