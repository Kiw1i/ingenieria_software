from flask import Flask, request, jsonify

app = Flask(__name__)

class Elector:
    def __init__(self, id, correo, contraseña, nombre, apellido):
        self.id = id
        self.correo = correo
        self.contraseña = contraseña
        self.nombre = nombre
        self.apellido = apellido
        self.ha_votado = False

    def registrar(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        return "Registro exitoso"

    def iniciar_sesion(self, correo, contraseña):
        if self.correo == correo and self.contraseña == contraseña:
            return "Inicio de sesión exitoso"
        else:
            return "Correo o contraseña incorrectos"

    def votar(self):
        if not self.ha_votado:
            self.ha_votado = True
            return "Voto registrado"
        else:
            return "Ya ha votado"

    def estado_voto(self):
        return "Ha votado" if self.ha_votado else "No ha votado"

    def editar_datos(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        return "Datos editados exitosamente"

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    return jsonify({"mensaje": elector.registrar(nombre, apellido)})

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    data = request.json
    correo = data.get('correo')
    contraseña = data.get('contraseña')
    return jsonify({"mensaje": elector.iniciar_sesion(correo, contraseña)})

@app.route('/votar', methods=['POST'])
def votar():
    return jsonify({"mensaje": elector.votar()})

@app.route('/estado_voto', methods=['GET'])
def estado_voto():
    return jsonify({"mensaje": elector.estado_voto()})

@app.route('/editar_datos', methods=['POST'])
def editar_datos():
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    return jsonify({"mensaje": elector.editar_datos(nombre, apellido)})

if __name__ == '__main__':
    app.run(debug=True)
