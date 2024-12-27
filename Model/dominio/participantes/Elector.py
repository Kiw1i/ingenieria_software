from Model.repositorio.MySQL.elector_repositorio_impl import elector_repositorio_impl
from Model.models.Elector import Elector

class Elector: 
    def __init__(self, id, correo, contrasena, nombre, apellido):
        self.id = id
        self.correo = correo
        self.contrasena = contrasena  
        self.nombre = nombre
        self.apellido = apellido
        self.ha_votado = "No"  

    def registrar(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        print(f"Registrado: {self.nombre} {self.apellido}") 
        return "Registro exitoso"

    def iniciar_sesion(self, correo, contrasena):
      
        if self.correo == correo and self.contrasena == contrasena:
            print("Inicio de sesión exitoso") 
            print(f"Error: correo o contraseña incorrectos para {correo}")
            return "Inicio de sesión exitoso"
        else:
            return f"Error: correo o contraseña incorrectos para {correo}" 

    def votar(self):
        if self.ha_votado == "No": 
            self.ha_votado = True
            print(f"Voto registrado para {self.nombre}") 
            return "Voto registrado"
        else:
            return "Ya ha votado"

    def estado_voto(self):
      
        return "Sí ha votado" if self.votado == "Yes" else "No ha votado"  

    def editar_datos(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        return f"Datos editados a: {self.nombre} {self.apellido}"  
