from Model.extensions import db

class EleccionModelo(db.Model):
    codigo = db.Column(db.Integer, primary_key=True)
    tipo_eleccion = db.Column(db.Text)
    fecha_inicio = db.Column(db.DateTime)
    fecha_cierre = db.Column(db.DateTime)
    lista_candidatos = db.Column(db.Text)

    def __repr__(self):
        return f'{self.tipo_eleccion}'