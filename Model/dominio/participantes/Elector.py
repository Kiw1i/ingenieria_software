from Model.repositorio.MySQL.elector_repositorio_impl import elector_repositorio_impl
from Model.models.Elector import Elector

class Elector:
    def __init__(self, id, correo, contrasena, nombre, apellido):
        self.id = id
        self.correo = correo
        self.contrasena = contrasena
        self.nombre = nombre
        self.apellido = apellido
        self.ha_votado = False

    def registrar(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        return "Registro exitoso"

    def iniciar_sesion(self, correo, contrasena):
        if self.correo == correo and self.contrasena == contrasena:
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
