from Model.extensions import db

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidatura = db.Column(db.String(100), nullable=False)
    partido = db.Column(db.String(100), nullable=False)  # Verifica que esta columna exista
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    estado_voto = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Candidato {self.candidatura}>'