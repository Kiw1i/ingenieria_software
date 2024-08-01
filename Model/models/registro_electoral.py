from Model.extensions import db

class RegistroElectoralModelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lista_electores = db.Column(db.Text)
    lista_candidatos = db.Column(db.Text)
    lista_partidos = db.Column(db.Text)

    def __repr__(self):
        return f'Registro electoral con id {self.id}'