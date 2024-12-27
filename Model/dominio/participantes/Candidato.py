from Model.repositorio.MySQL.eleccion_repositorio_impl import EleccionRepositorioImpl
from Model.dominio.participantes.Elector import Elector
from Model.models.eleccion import EleccionModelo

class candidato(Elector):
    def __init__(self, id, correo, contrasenia, nombre, apellido, candidatura, propuesta):
        super().__init__(id, correo, contrasenia, nombre, apellido)
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
        if not candidatura or not propuesta:
            raise ValueError("Datos incompletos para registrar candidato.")
        self.id = elector.id
        self.correo = elector.correo
        self.contrasena = elector.contrasena
        self.nombre = elector.nombre
        self.apellido = elector.apellido
        self.candidatura = candidatura
        self.propuesta = propuesta
        return "Candidato registrado exitosamente"
    
    def guardar_eleccion(self, eleccion):
        eleccion_modelo = EleccionModelo(
            codigo=eleccion.codigo,
            tipo_eleccion=eleccion.tipo_eleccion,
            fecha_inicio=eleccion.fecha_inicio,
            fecha_cierre=eleccion.fecha_cierre,
            lista_candidatos=eleccion.lista_candidatos
        )
        EleccionRepositorioImpl.nueva_eleccion(eleccion_modelo)
        return "Elección guardada exitosamente"
