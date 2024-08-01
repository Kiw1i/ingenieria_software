# Documentación del Proyecto

## Índice
- [Propósito del Proyecto](#propósito-del-proyecto)
- [Funcionalidades](#funcionalidades)
- [Modelo de dominio](#modelo-de-dominio)
- [Arquitectura y patrones](#arquitectura-y-patrones)
- [Practicas de codificación limpia aplicadas](#prácticas-de-codificación-limpia-aplicadas)
- [Estilos de programación aplicados](#estilos-de-programación-aplicados)
- [Principios SOLID aplicados](#principios-solid-aplicados)
- [Conceptos DDD aplicados](#conceptos-ddd-aplicados)

---
# Sistema de elecciones en linea
## Propósito del proyecto
El propósito de este proyecto es desarrollar un sistema de elecciones en línea que permita la gestión completa de un proceso electoral. Este sistema ofrece una plataforma segura y eficiente para registrar candidatos, electores y administrar la votación.

## Funcionalidades
#### 1. Diagramas de caso de uso

![diagrama de casos de uso](Imagenes/diagrama_de_casos_de_uso.png)

#### 2. Funcionalidades de Alto Nivel:
- Registro de Votantes: Permite a los usuarios registrarse en el sistema para poder votar.
- Gestión de Candidatos: Funcionalidad para registrar y gestionar candidatos en las elecciones.
- Votación en Línea: Los votantes pueden emitir su voto de forma segura.
- Resultados Electorales: Visualización de resultados en tiempo real una vez concluido el proceso de votación.
#### 3. Prototipo (o GUI):

##### Login:
![login](Imagenes/Login.png)
##### Menu:
![login](Imagenes/Menu.png)
##### Registro de Elector:
![registrar elector](Imagenes/Registrar_Elector.png)
##### Registro de Candidato:
![regitrar candidato](Imagenes/Registro_Candidato.png)
##### Registro de Elecciones:
![registro elecciones](Imagenes/Registro_Elecciones.png)


## Modelo de dominio
### 1. Diagrama de clases y modulos

#### Diagrama de clases:
![diagrama](Imagenes/diagrama_clases.png)
#### Diagrama de componentes:
![diagrama](Imagenes/diagrama_componentes.png)
#### Diagrama de despligue:
![diagrama](Imagenes/diagrama_despliegue.png)
#### Diagrama de paquetes:
![diagrama](Imagenes/diagrama_paquetes.png)

### 2. Módulos del Sistema
1. Módulo de Presentación
    - Maneja la interacción con el usuario.
    - Incluye vistas HTML y controladores para procesar las solicitudes.
  
2. Módulo de Proceso Electoral
    - Contiene la lógica para gestionar elecciones, incluyendo creación y conteo de votos.
    - Se ocupa de la ejecución del proceso electoral completo.
  
3. Módulo de Participantes
    - Gestiona la información sobre candidatos y electores.
    - Incluye operaciones CRUD y lógica de negocio relacionada con los participantes.
  
4. Módulo de Voto
    - Responsable de la creación, validación y almacenamiento de votos.
    - Implementa lógica para garantizar la integridad del proceso de votación.
  
5. Módulo de Resultados
    - Calcula y presenta los resultados de las elecciones.
    - Proporciona análisis y estadísticas sobre las elecciones.
  
6. Módulo de Registro Electoral
    - Gestiona el registro de electores y la validación de los derechos de voto.
    - Asegura que solo los usuarios autorizados puedan participar en las elecciones.

## Arquitectura y patrones
### 1. Arquitectura
#### Vista general de la arquitectura:
![general](Imagenes/vista_arquitectura.jpeg)

El proyecto sigue una arquitectura basada en capas, con una clara separación entre la lógica de negocio, la presentación y el acceso a datos:
- Capa de Presentación: Utiliza Flask para manejar las rutas y vistas. Los controladores gestionan las solicitudes HTTP y renderizan las plantillas HTML para la interacción con el usuario.
- Capa de Aplicación/Lógica de Negocio: Esta capa gestiona las reglas del negocio y coordina las interacciones entre la presentación y el acceso a datos. Aquí se incluyen las funciones y servicios que implementan la lógica del proceso electoral.
- Capa de Datos: Utiliza SQLAlchemy como ORM para gestionar la persistencia de datos en la base de datos, proporcionando una abstracción para el acceso a datos.

## Practicas de codificación limpia aplicadas
### Nombres de variables, funciones y clases
El proyecto hace uso de prácticas de codificación legible para variables, funciones y métodos según el estándar del lenguaje Python, que indica que se debe usar el *snake_case*. Del mismo modo, las clases siguen la convención *CamelCase*.

## Estilos de programación aplicados
### Modelo-Vista-Controlador (MVC): El proyecto sigue el patrón MVC, donde los modelos representan la estructura de datos, las vistas son las interfaces de usuario y los controladores manejan la interacción entre modelos y vistas.
- Repositorio: Se utiliza para la abstracción del acceso a datos, permitiendo a la capa de lógica de negocio interactuar con la base de datos a través de una interfaz coherente.

### Error/Exception Handling (constructive)
Este estilo se aplica en todos los métodos del repositorio para manejar posibles errores durante las operaciones con la base de datos. Si ocurre una excepción, la operación se revierte para mantener la integridad de los datos. 

### Cookbook
Con la integración de este estilo, se ve la implementación clara y directa de operaciones CRUD en los métodos del repositorio.

Constructive error/exception handling y Cookbook se ven en:

*candidato_repositorio_impl.py:*
```python
class candidato_respositorio_impl:
    def agregar_candidato(self, candidato): # Create
        try:
            db.session.add(candidato)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def eliminar_candidato(self, candidato): # Delete
        try:
            db.session.delete(candidato)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def obtener_candidato_por_id(self, id): # Read
        try:
            candidato = Candidato.query.get(id)
            return candidato
        except Exception:
            return None

    def actualizar_candidato(self, id, nueva_candidatura, nueva_propuesta): # Update
        try:
            candidato = Candidato.query.get(id)
            if candidato:
                candidato.candidatura = nueva_candidatura
                candidato.propuesta = nueva_propuesta
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False
```

*elector_repositorio_impl.py:*
```python
class elector_repositorio_impl:
    def agregar_elector(self, elector):
        try:
            db.session.add(elector)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def eliminar_elector(self, elector):
        try:
            db.session.delete(elector)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def obtener_elector_por_id(self, id):
        try:
            elector = Elector.query.get(id)
            return elector
        except Exception:
            return None
    
    def actualizar_elector(self, id, nuevo_correo, nueva_contrasena, nuevo_nombre, nuevo_apellido, nuevo_estado_voto):
        try:
            elector = Elector.query.get(id)
            if elector:
                elector.correo = nuevo_correo
                elector.contrasena = nueva_contrasena
                elector.nombre = nuevo_nombre
                elector.apellido = nuevo_apellido
                elector.estado_voto = nuevo_estado_voto
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False
```

### Persistent-Tables

Este estilo se aplica al definir los modelos de base de datos Candidato y Elector utilizando SQLAlchemy, lo que asegura que los datos se almacenan de manera óptima en la base de datos. 
Estas tablas se pueden ver en:

*En models/Candidato.py:*
```python
from Model.extensions import db

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidatura = db.Column(db.String(100), unique=True, nullable=False)
    propuesta = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Candidato {self.candidatura}>'
```

*En models/Elector.py:*
```python
from Model.extensions import db

class Elector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(120), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    estado_voto = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Elector {self.nombre} {self.apellido}>'
```
