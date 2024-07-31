from flask import Flask, request, jsonify

app = Flask(__name__)
class Candidato(Elector):
    def __init__(self, id, correo, contraseña, nombre, apellido, candidatura, propuesta):
        super().__init__(id, correo, contraseña, nombre, apellido)
        self.candidatura = candidatura
        self.propuesta = propuesta

    def modificar_propuesta(self, propuesta):
        self.propuesta = propuesta
        return "Propuesta modificada exitosamente"

    def actualizar_perfil(self, elector, candidatura, propuesta):
        self.nombre = elector.nombre
        self.apellido = elector.apellido
        self.candidatura = candidatura
        self.propuesta = propuesta
        return "Perfil actualizado exitosamente"

    def registrar_candidato(self, elector, candidatura, propuesta):
        self.id = elector.id
        self.correo = elector.correo
        self.contraseña = elector.contraseña
        self.nombre = elector.nombre
        self.apellido = elector.apellido
        self.candidatura = candidatura
        self.propuesta = propuesta
        return "Candidato registrado exitosamente"

@app.route('/modificar_propuesta', methods=['POST'])
def modificar_propuesta():
    data = request.json
    propuesta = data.get('propuesta')
    return jsonify({"mensaje": candidato.modificar_propuesta(propuesta)})

@app.route('/actualizar_perfil', methods=['POST'])
def actualizar_perfil():
    data = request.json
    candidatura = data.get('candidatura')
    propuesta = data.get('propuesta')
    return jsonify({"mensaje": candidato.actualizar_perfil(elector, candidatura, propuesta)})

@app.route('/registrar_candidato', methods=['POST'])
def registrar_candidato():
    data = request.json
    candidatura = data.get('candidatura')
    propuesta = data.get('propuesta')
    return jsonify({"mensaje": candidato.registrar_candidato(elector, candidatura, propuesta)})

if __name__ == '__main__':
    app.run(debug=True)
