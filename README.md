# Documentación del Proyecto

## Índice
- [Proposito del Proyecto](#proposito-del-proyecto)
- [Funcionalidades](#funcionalidades)
- [Modelo de dominio](#modelo-de-dominio)
- [Arquitectura y Patrones](#arquitectura-y-patrones)
- [Practicas de codificación limpia aplicadas](#practicas-de-codificacion-limpia-aplicadas)
- [Estilos de programación aplicados](#estilos-de-programacion-aplicados)
- [Principios SOLID aplicados](#principios-solid-aplicados)
- [Conceptos DDD aplicados](#conceptos-ddd-aplicados)

---
# Sistema de elecciones en linea
## Proposito del Proyecto
El propósito de este proyecto es desarrollar un sistema de elecciones en línea que permita la gestión completa de un proceso electoral. Este sistema ofrece una plataforma segura y eficiente para registrar candidatos, electores y administrar la votación.


## Funcionalidades
#### Diagramas de caso de uso
#### Funcionalidades de Alto Nivel:
- Registro de Votantes: Permite a los usuarios registrarse en el sistema para poder votar.
- Gestión de Candidatos: Funcionalidad para registrar y gestionar candidatos en las elecciones.
- Votación en Línea: Los votantes pueden emitir su voto de forma segura.
- Resultados Electorales: Visualización de resultados en tiempo real una vez concluido el proceso de votación.
#### Prototipo (o GUI):
![login](Imagenes/Login.png)


## Modelo del dominio
### Diagrama de clases y modulos

## Arquitectura y Patrones
###


## Error/Exception Handling (constructive)
Este estilo se aplica en todos los métodos del repositorio para manejar posibles errores durante las operaciones con la base de datos. Si ocurre una excepción, la operación se revierte para mantener la integridad de los datos. 
## Cookbook
Con la integración de este estilo, se ve la implementación clara y directa de operaciones CRUD en los métodos del repositorio.

Error/Exception Handling y Cookbook se ven en:

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
## Persistent-Tables
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
# Repositorios del sistema de elecciones online

Fork del [Sistema de elecciones online](https://github.com/Kiw1i/ingenieria_software)

## Descripción

El objetivo del proyecto original es implementar un sistema que permita a los usuarios programar elecciones para la fecha deseada, entre los candidatos inidicados y para los electores a quienes compete. Este fork implementa la parte de los repositorios al módulo `proceso_electoral` y conexiones a base de datos del sistema, así como modelos de flujo de información entre las diversas capas.

## SOLID

El programa cumple con principios SOLID.

### 1. Principio de única responsabilidad

Cada clase en el programa se encarga de una única cosa.

```python
class EleccionModelo(db.Model):
    codigo = db.Column(db.Integer, primary_key=True)
    tipo_eleccion = db.Column(db.Text)
    fecha_inicio = db.Column(db.DateTime)
    fecha_cierre = db.Column(db.DateTime)
    lista_candidatos = db.Columnd(db.Text)

    def __repr__(self):
        return f'{self.tipo_eleccion}'
```

Las clases modelo solo tienen la función de almacenar los datos de cada objeto. La única razón para cambiarlas es agregar más datos a guardar.

### 2. Principio de apertura/cierre

Las clases implementadas se pueden extender en sus métodos sin modificar los ya existentes.

```python
class AdministradorEleccionRepositorioImpl:
    @staticmethod
    def insertar_administrador(admin):
        try:
            db.session.add(admin)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
    
    @staticmethod
    def eliminar_administrador(admin):
        try:
            entrada = db.session.query(AdministradorModelo).filter_by(id = admin.id).one()
            db.session.delete(entrada)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
```

Se puede agregar una función `get_administrador_nombre(admin_id)` de tal modo que no modifique la funcionalidad de `insertar_administrador(admin)` ni `eliminar_administrador(admin)`.

```python
    @staticmethod
    def get_administrador_nombre(admin_id):
        admin_nombre = ""
        try:
            entrada = db.session.query(AdministradorModelo).filter_by(id = admin_id).one()
            admin_nombre = entrada.nombre
        except NoResultFound:
            print(f"No se encontró una entrada con la id {admin_id}\n")
            return None
        except SQLAlchemyError as e:
            print(f"Hubo un error al consultar la base de datos: {e}")
            return None
        finally:
            db.session.close()
        return admin_nombre
```

## Estilos

### Manejo de errores/excepciones: Constructivista

El programa intenta seguir con su ejecución si sucede algún error devolviendo valores determinados "razonables".

```python
except NoResultFound:
    print(f"No se encontró una entrada con la id {admin_id}\n")
    return None
except SQLAlchemyError as e:
    print(f"Hubo un error al consultar la base de datos: {e}")
    return None
```

### Tablas de persistencia

Los datos se almacenan en una base de datos relacional a la que se accede mediante consultas SQL.

Se accede a ellos usando las funciones ORM de la biblioteca SQLAlchemy para Flask.

```python
entrada = db.session.query(AdministradorModelo).filter_by(id = admin_id).one()
admin_nombre = entrada.nombre
```

### Trinity (MVC)

La base de datos se comunica con los repositorios a través de una clase (modelo), que a su vez comunica a los repositorios con el dominio y viceversa.

```python
db.session.add(admin)
```

```python
admin_nombre = entrada.nombre
```

## Uso

Se puede acceder a los repositorios mediante su interfaz, enviando la información pertinente a través de su modelo correspondiente. La información, si existe, se extraerá de la base de datos.

## Autor

Kristopher Rospigliosi Gonzales y Leonardo Ponze Bellido
# DOCUMENTACION DEL PROYECTO 

## Principio SOLID : 
1. Single Responsibility Principle (SRP) :
   La clase AdministradorEleccion se encarga únicamente de registrar a un administrador, cumpliendo con el principio de Responsabilidad Única (SRP).

```python
class AdministradorEleccion:
    def __init__(self):
        self.nombre = None
        self.id = None
        self.password = None

    def registrar_admin(self, nombre: str, password: str, id: int) -> None:
        self.nombre = nombre
        self.password = password
        self.id = id
```

2.  Open/Closed Principle (OCP):
    La clase Eleccion está diseñada para ser abierta para la extensión pero cerrada para la modificación (OCP), permitiendo añadir nuevas funcionalidades sin cambiar el código existente.

```python
class Eleccion:
    def __init__(self, tipo_eleccion: str = None, fecha_inicio: str = None, fecha_fin: str = None):
        self.tipo_eleccion = tipo_eleccion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def iniciar_eleccion(self, fecha_inicio: str) -> None:
        self.fecha_inicio = fecha_inicio

    def finalizar_eleccion(self, fecha_fin: str) -> None:
        self.fecha_fin = fecha_fin
```

3. Interface Segregation Principle (ISP):
   La interfaz IResultados está diseñada para proporcionar métodos específicos relacionados con la gestión de resultados, cumpliendo con el principio de Segregación de Interfaces (ISP) al asegurar que las 
   implementaciones solo dependan de métodos que realmente utilizan
from abc import ABC, abstractmethod

```python
class IResultados(ABC):
    @abstractmethod
    def agregar_voto(self, candidato: str) -> None:
        pass

    @abstractmethod
    def calcular_porcentajes(self) -> None:
        pass

    @abstractmethod
    def mostrar_resultados(self) -> dict:
        pass
---
```

## ESTILOS DE PROGRAMACION 
1. THINGS: El estilo "Things" se centra en representar entidades del mundo real y sus interacciones.  Estas clases encapsulan datos y comportamientos relacionados con cada entidad, facilitando la gestión y manipulación de objetos del sistema de votación

```python
class AdministradorEleccion:
    def __init__(self, nombre, password, id=None):
        self.nombre = nombre
        self.password = password
        self.id = id

    def registrar_admin(self, nombre, password, id):
        self.nombre = nombre
        self.password = password
        self.id = id

    def configurar_eleccion(self, eleccion, nueva_fecha_inicio=None, nueva_fecha_fin=None, nuevos_candidatos=None):
        if nueva_fecha_inicio:
            eleccion.iniciar_eleccion(nueva_fecha_inicio)
        if nueva_fecha_fin:
            eleccion.finalizar_eleccion(nueva_fecha_fin)
        if nuevos_candidatos:
            eleccion.lista_candidatos = nuevos_candidatos

    def agregar_candidato(self, eleccion, candidato):
        eleccion.lista_candidatos.append(candidato)

    def eliminar_candidato(self, eleccion, candidato):
        if candidato in eleccion.lista_candidatos:
            eleccion.lista_candidatos.remove(candidato)
```

3.  Error/Exception Handling: Este enfoque mejora el manejo de errores utilizando excepciones. Al usar raise ValueError para señalar problemas específicos, el código se vuelve más robusto y es más fácil de depurar, ya que los errores se identifican y manejan claramente.

```python
class Voto:
    def __init__(self):
        """Inicializa un nuevo objeto Voto con valores predeterminados."""
        self.fecha: Optional[datetime] = None
        self.hora: Optional[datetime] = None
        self.elector: Optional[str] = None  # Suponiendo que elector es un string con el nombre
        self.id_voto: Optional[str] = None  # Suponiendo que id_voto es un string

    def registrar_voto(self, elector: str, id_voto: str, fecha: Optional[datetime] = None, hora: Optional[datetime] = None) -> None:
        """Registra un voto con el elector y el ID, y establece la fecha y la hora actuales si no se proporcionan."""
        self.elector = elector
        self.id_voto = id_voto
        
        if fecha is None:
            self.fecha = datetime.now().date()
        else:
            self.fecha = fecha

        if hora is None:
            self.hora = datetime.now().time()
        else:
            self.hora = hora

    def confirmar_voto(self):
        if not self.elector:
            raise ValueError("Elector no proporcionado.")
        if not self.fecha:
            raise ValueError("Fecha no proporcionada.")
        if not self.hora:
            raise ValueError("Hora no proporcionada.")
        if not self.id_voto:
            raise ValueError("ID de voto no proporcionado.")
        print("Voto confirmado")
        return True
```

3. PIPELINE : procesar datos a través de una serie de pasos, donde la salida de un paso se convierte en la entrada del siguiente
class Resultados(IResultados):

```python
   def __init__(self):
        """Inicializa la clase Resultados con total de votos y listas vacías."""
        self.total_votos: int = 0
        self.votos_candidatos: List[int] = []  # Lista de votos por candidato
        self.porcentajes_candidatos: List[float] = []  # Lista de porcentajes por candidato

    def agregar_votos(self, votos_candidatos: List[int]) -> None:
        """Añade los votos de los candidatos y actualiza el total de votos."""
        if not all(isinstance(voto, int) for voto in votos_candidatos):
            raise ValueError("Todos los votos deben ser enteros.")
        
        self.votos_candidatos = votos_candidatos
        self.total_votos = sum(votos_candidatos)
        self.calcular_porcentajes()

    def calcular_porcentajes(self) -> None:
        """Calcula el porcentaje de votos que obtuvo cada candidato."""
        if self.total_votos > 0:
            self.porcentajes_candidatos = [(votos / self.total_votos) * 100 for votos in self.votos_candidatos]
        else:
            self.porcentajes_candidatos = [0 for _ in self.votos_candidatos]

    def get_votos_totales(self) -> int:
        """Retorna el total de votos."""
        return self.total_votos

    def get_votos_candidatos(self) -> List[int]:
        """Retorna la lista de votos por candidato."""
        return self.votos_candidatos

    def get_porcentajes_candidatos(self) -> List[float]:
        """Retorna la lista de porcentajes de votos por candidato."""
        return self.porcentajes_candidatos

    def publicar_resultados(self) -> dict:
        """Publica los resultados mostrando los votos totales y los porcentajes por candidato."""
        return {
            "total_votos": self.get_votos_totales(),
            "votos_candidatos": self.get_votos_candidatos(),
            "porcentajes_candidatos": self.get_porcentajes_candidatos()
        }
```
# Documentación del Proyecto

## Índice
- [ParticipantesController](#participantescontroller)
- [ProcesoElectoralController](#procesoelectoralcontroller)
- [Estilos CSS](#estilos-css)
- [JavaScript Principal](#javascript-principal)
- [JavaScript de Participantes](#javascript-de-participantes)
- [Página de Participantes](#pagina-de-participantes)
- [Configuración de la Aplicación Flask](#configuracion-de-la-aplicacion-flask)
- [Archivo Principal](#archivo-principal)

---

## ParticipantesController

### 1. Nombres Descriptivos
Se utilizaron nombres claros y descriptivos para los métodos en el controlador de participantes. Esto facilita la comprensión del código y su propósito.

**Ejemplo:**
```python
@participantes_bp.route('/participantes', methods=['GET'])
def obtener_participantes(self):
    participantes = self.servicio.obtener_todos()
    return jsonify(participantes)
```

## ProcesoElectoralController

### 1. Nombres Descriptivos
Se utilizaron nombres claros y descriptivos para los métodos en el controlador de procesos electorales. Esto facilita la comprensión del código y su propósito.

**Ejemplo:**
```python
@proceso_electoral_bp.route('/procesos-electorales', methods=['GET'])
def obtener_procesos(self):
    procesos = self.servicio.obtener_todos()
    return jsonify(procesos)
```

## Estilos CSS

### 1. Nombres Descriptivos
Se utilizaron nombres claros y descriptivos para las variables CSS. Esto facilita la comprensión del código y su propósito.

**Ejemplo:**
```css
:root {
    --primary-color: #007bff;
    --primary-color-hover: #0056b3;
    --background-color: #f8f9fa;
    --text-color: #343a40;
    --border-color: #dee2e6;
    --white-color: #ffffff;
}
```

### 2. Comentarios
Se añadieron comentarios para describir las secciones del código CSS. Esto ayuda a otros desarrolladores a entender rápidamente la funcionalidad del código.

**Ejemplo:**
```css
/* Variables de diseño */
:root {
    --max-width-container: 800px;
    --padding-container: 20px;
}
```

## JavaScript Principal

### 1. Nombres Descriptivos
Se utilizó un mensaje claro en el console.log para indicar que el documento está completamente cargado y listo.

**Ejemplo:**
```javascript
document.addEventListener('DOMContentLoaded', function() {
    console.log("Documento cargado y listo.");
});
```

## JavaScript de Participantes

### 1. Nombres Descriptivos
Se utilizaron nombres claros y descriptivos para variables y funciones. Esto facilita la comprensión del código y su propósito.

**Ejemplo:**
```javascript
const listaParticipantes = document.getElementById('lista-participantes');
```

### 2. Comentarios
Se añadieron comentarios para describir la funcionalidad del código JavaScript. Esto ayuda a otros desarrolladores a entender rápidamente la estructura y propósito del código.

**Ejemplo:**
```javascript
// Obtener y mostrar la lista de participantes
fetch('/participantes')
    .then(response => response.json())
    .then(data => {
        data.forEach(participante => {
            const item = document.createElement('li');
            item.textContent = participante.nombre;
            listaParticipantes.appendChild(item);
        });
    });

```

## Página de Participantes

### 1. Estructura y Comentarios
Se añadieron comentarios para describir las secciones del código HTML. Esto ayuda a otros desarrolladores a entender rápidamente la estructura de la página.

**Ejemplo:**
```html
<!-- Lista para mostrar los participantes -->
<ul id="lista-participantes"></ul>
```

## Configuración de la Aplicación Flask

### 1. Comentarios y Docstrings
Se añadió un docstring a la función create_app para describir su propósito y lo que devuelve. Esto ayuda a otros desarrolladores a entender rápidamente la función de esta configuración.

**Ejemplo:**
```python
def create_app():
    """
    Crea y configura una instancia de la aplicación Flask.
    
    Returns:
        app (Flask): La instancia de la aplicación Flask configurada.
    """
    app = Flask(__name__)
    # Registro de Blueprints
    app.register_blueprint(participantes_bp)
    app.register_blueprint(proceso_electoral_bp)
    
    return app
```

## Archivo Principal

### 1. Comentarios
Se añadieron comentarios para describir el propósito del código, como la creación de la instancia de la aplicación y la ejecución en modo de depuración. Esto ayuda a otros desarrolladores a entender rápidamente el propósito de cada parte del código.

**Ejemplo:**
```python
# Crear una instancia de la aplicación Flask
app = create_app()

if __name__ == "__main__":
    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)
```

## Principios SOLID en ParticipantesController

### 1. Principio de Responsabilidad Única (SRP)
El ParticipantesController tiene una única responsabilidad: manejar las solicitudes relacionadas con los participantes. No mezcla lógica de negocio ni de acceso a datos.

**Ejemplo:**
```python
class ParticipantesController:
    def __init__(self):
        self.servicio = ParticipantesServicio()

    @participantes_bp.route('/participantes', methods=['GET'])
    def obtener_participantes(self):
        participantes = self.servicio.obtener_todos()
        return jsonify(participantes)

    @participantes_bp.route('/participantes', methods=['POST'])
    def crear_participante(self):
        data = request.json
        nuevo_participante = self.servicio.crear(data)
        return jsonify(nuevo_participante), 201

    @participantes_bp.route('/participantes/<int:id>', methods=['PUT'])
    def actualizar_participante(self, id):
        data = request.json
        participante_actualizado = self.servicio.actualizar(id, data)
        return jsonify(participante_actualizado)

    @participantes_bp.route('/participantes/<int:id>', methods=['DELETE'])
    def eliminar_participante(self, id):
        self.servicio.eliminar(id)
        return '', 204
```

### 2. Principio de Inversión de Dependencias (DIP)
El controlador depende de una abstracción (ParticipantesServicio) en lugar de una implementación concreta. Esto permite cambiar la implementación del servicio sin modificar el controlador.

**Ejemplo:**
```python
class ParticipantesController:
    def __init__(self, servicio):
        self.servicio = servicio

# Uso
servicio = ParticipantesServicio()
controller = ParticipantesController(servicio)
```

### 3. Principio de Abierto/Cerrado (OCP)
El ParticipantesController está abierto para la extensión (puedes añadir nuevos endpoints) pero cerrado para la modificación (no necesitas modificar el código existente para añadir nuevas funcionalidades).

**Ejemplo:**
```python
class ParticipantesController:
    # Métodos existentes...

    @participantes_bp.route('/participantes/<int:id>/detalle', methods=['GET'])
    def obtener_detalle_participante(self, id):
        detalle = self.servicio.obtener_detalle(id)
        return jsonify(detalle)
```

## Principios SOLID en ProcesoElectoralController

### 1. Principio de Responsabilidad Única (SRP)
El ProcesoElectoralController tiene una única responsabilidad: manejar las solicitudes relacionadas con los procesos electorales.

**Ejemplo:**
```python
class ProcesoElectoralController:
    def __init__(self):
        self.servicio = ProcesoElectoralServicio()

    @proceso_electoral_bp.route('/procesos-electorales', methods=['GET'])
    def obtener_procesos(self):
        procesos = self.servicio.obtener_todos()
        return jsonify(procesos)

    @proceso_electoral_bp.route('/procesos-electorales', methods=['POST'])
    def crear_proceso(self):
        data = request.json
        nuevo_proceso = self.servicio.crear(data)
        return jsonify(nuevo_proceso), 201

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>', methods=['PUT'])
    def actualizar_proceso(self, id):
        data = request.json
        proceso_actualizado = self.servicio.actualizar(id, data)
        return jsonify(proceso_actualizado)

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>', methods=['DELETE'])
    def eliminar_proceso(self, id):
        self.servicio.eliminar(id)
        return '', 204
```

### 2. Principio de Inversión de Dependencias (DIP)
El controlador depende de una abstracción (ProcesoElectoralServicio) en lugar de una implementación concreta.

**Ejemplo:**
```python
class ProcesoElectoralController:
    def __init__(self, servicio):
        self.servicio = servicio

# Uso
servicio = ProcesoElectoralServicio()
controller = ProcesoElectoralController(servicio)
```

### 3. Principio de Abierto/Cerrado (OCP)
El ProcesoElectoralController está abierto para la extensión pero cerrado para la modificación.

**Ejemplo:**
```python
class ProcesoElectoralController:
    # Métodos existentes...

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>/detalle', methods=['GET'])
    def obtener_detalle_proceso(self, id):
        detalle = self.servicio.obtener_detalle(id)
        return jsonify(detalle)
```

## Principios de Estilo CSS Legible en estilos_generales.css

### 1. Principio de Responsabilidad Única (SRP)
Cada sección de estilos CSS tiene una responsabilidad única, por ejemplo, estilizar el cuerpo del documento, encabezados, listas y botones. No mezcla estilos de diferentes componentes.

**Ejemplo:**
```css
/* Estilo global del cuerpo */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: var(--background-color);
}

/* Estilo para los encabezados */
h1 {
    color: var(--text-color);
}

/* Estilo para listas no ordenadas */
ul {
    list-style-type: none;
    padding: 0;
}

/* Estilo para los elementos de la lista */
li {
    padding: 10px;
    background-color: var(--white-color);
    margin-bottom: 5px;
    border: 1px solid var(--border-color);
    border-radius: 5px;
}

/* Estilo para los botones */
button {
    background-color: var(--primary-color);
    color: var(--white-color);
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

/* Estilo para el estado hover de los botones */
button:hover {
    background-color: var(--primary-color-hover);
}
```

### 3. Principio de Abierto/Cerrado (OCP)
El archivo CSS está abierto para la extensión (puedes añadir nuevos estilos) pero cerrado para la modificación (no necesitas modificar el código existente para añadir nuevos estilos).

**Ejemplo:**
```css
/* Estilo para los párrafos */
p {
    color: var(--text-color);
    line-height: 1.6;
}
```

## JavaScript Principal

### 1. Principio de Responsabilidad Única (SRP)
Se utilizó un mensaje claro en el console.log para indicar que el documento está completamente cargado y listo.

**Ejemplo:**
```javascript
document.addEventListener('DOMContentLoaded', function() {
    console.log("Documento cargado y listo.");
});
```

## JavaScript de Participantes

### 1. Principio de Responsabilidad Única (SRP)
Se utilizaron nombres claros y descriptivos para variables y funciones. Esto facilita la comprensión del código y su propósito.

**Ejemplo:**
```javascript
const listaParticipantes = document.getElementById('lista-participantes');

fetch('/participantes')
    .then(response => response.json())
    .then(data => {
        data.forEach(participante => {
            const item = document.createElement('li');
            item.textContent = participante.nombre;
            listaParticipantes.appendChild(item);
        });
    });

// Evento para agregar participante (suponiendo que tienes un formulario)
const form = document.getElementById('form-participante');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    const nombre = document.getElementById('nombre').value;

    fetch('/participantes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre: nombre })
    })
    .then(response => response.json())
    .then(participante => {
        const item = document.createElement('li');
        item.textContent = participante.nombre;
        listaParticipantes.appendChild(item);
        form.reset();
    });
});
```

## Página de Participantes

### 1. Principio de Responsabilidad Única (SRP)
Se añadieron comentarios para describir las secciones del código HTML. Esto ayuda a otros desarrolladores a entender rápidamente la estructura de la página.

**Ejemplo:**
```html
<!-- Lista para mostrar los participantes -->
<ul id="lista-participantes"></ul>
```

## Configuración de la Aplicación Flask

### 1. Principio de Responsabilidad Única (SRP)
La función create_app tiene una única responsabilidad: crear y configurar una instancia de la aplicación Flask.

**Ejemplo:**
```python
def create_app():
    """
    Crea y configura una instancia de la aplicación Flask.
    
    Returns:
        app (Flask): La instancia de la aplicación Flask configurada.
    """
    app = Flask(__name__)
    # Registro de Blueprints
    app.register_blueprint(participantes_bp)
    app.register_blueprint(proceso_electoral_bp)
    
    return app
```

## Archivo Principal

### 1. Principio de Responsabilidad Única (SRP)
Se añadieron comentarios para describir el propósito del código, como la creación de la instancia de la aplicación y la ejecución en modo de depuración. Esto ayuda a otros desarrolladores a entender rápidamente el propósito de cada parte del código.

**Ejemplo:**
```python
# Crear una instancia de la aplicación Flask
app = create_app()

if __name__ == "__main__":
    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)
```

## Estilos de Programacion

### ParticipantesController
#### 1. Restful
Las rutas están diseñadas siguiendo las convenciones REST, con métodos HTTP adecuados para cada operación (GET, POST, PUT, DELETE).

**Ejemplo:**
```python
@participantes_bp.route('/participantes', methods=['GET'])
def obtener_participantes(self):
    ...

@participantes_bp.route('/participantes', methods=['POST'])
def crear_participante(self):
    ...
```

#### 2. Error/Exception Handling
El ParticipantesController maneja excepciones y errores que pueden ocurrir durante las operaciones CRUD. Utiliza el manejo de errores para asegurar que el sistema responda adecuadamente ante fallos.

**Ejemplo:**
```python
try:
    data = request.json
    nuevo_participante = self.servicio.crear(data)
    return jsonify(nuevo_participante), 201
except Exception as e:
    return jsonify({"error": "Error al crear participante: " + str(e)}), 400

```

#### 3. Cookbook
Se ha añadido una receta estándar para validar los datos de entrada y manejar errores en el método crear_participante.

**Ejemplo:**
```python
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
```

### ProcesoElectoralController

#### 1. Cookbook
Se ha añadido una receta estándar para validar los datos de entrada y manejar errores en el método crear_proceso.

**Ejemplo:**
```python
@proceso_electoral_bp.route('/procesos-electorales', methods=['POST'])
def crear_proceso(self):
    try:
        data = request.json
        # Validación de datos
        if not data.get('nombre') or not data.get('fecha'):
            return jsonify({"error": "Faltan campos obligatorios: nombre y fecha"}), 400

        nuevo_proceso = self.servicio.crear(data)
        return jsonify(nuevo_proceso), 201
    except Exception as e:
        return jsonify({"error": "Error al crear proceso electoral: " + str(e)}), 400
```
#### 3. Error/Exception Handling
Se ha mejorado el manejo de excepciones en todos los métodos del controlador, proporcionando mensajes de error específicos y uniformes. Se proporciona un manejo uniforme de excepciones en cada método, retornando mensajes de error específicos y códigos de estado adecuados.

**Ejemplo:**
```python
try:
    data = request.json
    nuevo_proceso = self.servicio.crear(data)
    return jsonify(nuevo_proceso), 201
except Exception as e:
    return jsonify({"error": "Error al crear proceso electoral: " + str(e)}), 400
```

#### 3. RESTful
Las rutas están diseñadas siguiendo las convenciones REST, con métodos HTTP adecuados para cada operación (GET, POST, PUT, DELETE).

**Ejemplo:**
```python
@proceso_electoral_bp.route('/procesos-electorales', methods=['GET'])
def obtener_procesos(self):
    ...

@proceso_electoral_bp.route('/procesos-electorales', methods=['POST'])
def crear_proceso(self):
    ...
```

### Estilos CSS

####1. Cookbook: Estilos Consistentes y Variables CSS
Se ha añadido una receta estándar para mantener la consistencia en los estilos y facilitar su mantenimiento utilizando variables CSS. Se utilizan variables CSS para definir colores, lo que permite un fácil mantenimiento y cambios rápidos en toda la aplicación.

**Ejemplo:**
```css
/* Variables de colores */
:root {
    --primary-color: #007bff;
    --primary-color-hover: #0056b3;
    --background-color: #f8f9fa;
    --text-color: #343a40;
    --border-color: #dee2e6;
    --white-color: #ffffff;
}
```

#### 2. Error/Exception Handling: Reseteo y Normalización de Estilos
Se ha añadido un reseteo de estilos para asegurar la consistencia entre diferentes navegadores. Se aplican resets de estilos para asegurar que todos los elementos tengan un comportamiento consistente en diferentes navegadores.

**Ejemplo:**
```css
/* Reset de estilos para mantener la consistencia entre navegadores */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

#### 3. RESTful: Organización Lógica de Estilos
Se ha organizado el archivo CSS de manera lógica para facilitar la lectura y el mantenimiento. Los estilos se organizan de manera lógica, agrupando estilos globales, de encabezados, listas, botones y párrafos, para facilitar su lectura y mantenimiento.

**Ejemplo:**
```css
/* Estilo global del cuerpo */
body {
    font-family: Arial, sans-serif;
    background-color: var(--background-color);
    color: var(--text-color);
}

/* Estilo para los encabezados */
h1 {
    color: var(--text-color);
    margin-bottom: 20px;
}

/* Estilo para listas no ordenadas */
ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

/* Estilo para los elementos de la lista */
li {
    padding: 10px;
    background-color: var(--white-color);
    margin-bottom: 5px;
    border: 1px solid var(--border-color);
    border-radius: 5px;
}

/* Estilo para los botones */
button {
    background-color: var(--primary-color);
    color: var(--white-color);
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

/* Estilo para el estado hover de los botones */
button:hover {
    background-color: var(--primary-color-hover);
}

/* Estilo para los párrafos */
p {
    color: var(--text-color);
    line-height: 1.6;
    margin-bottom: 20px;
}
```

### Estilos participantes

#### 1. Cookbook: Variables de Diseño y Estructura
Se han añadido variables CSS y una receta estándar para definir la estructura y el diseño de los contenedores y elementos de la lista de participantes. Se utilizan variables CSS para definir propiedades de diseño como el ancho máximo del contenedor, el padding, el gap entre elementos de la lista, el radio de borde y los colores de fondo y borde. Esto facilita el mantenimiento y la consistencia en el diseño.

**Ejemplo:**
```css
/* Variables de diseño */
:root {
    --max-width-container: 800px;
    --padding-container: 20px;
    --gap-list-items: 10px;
    --border-radius: 5px;
    --background-color-item: var(--white-color);
    --border-color-item: var(--border-color);
}
```

#### 2. Error/Exception Handling: Mejoras en la Estructura
Se ha mejorado la estructura del contenedor principal y los elementos de la lista, añadiendo sombras y bordes redondeados para una mejor apariencia visual y legibilidad.
El contenedor principal se ha mejorado con un fondo, bordes redondeados y una sombra para mejorar la apariencia visual y los elementos de la lista de participantes ahora tienen un diseño consistente con padding, margen, fondo, borde y sombra, lo que mejora la legibilidad y la apariencia visual.

**Ejemplo:**
```css
/* Contenedor principal para los participantes */
#participantes-container {
    max-width: var(--max-width-container);
    margin: auto;
    padding: var(--padding-container);
    background-color: var(--background-color);
    border-radius: var(--border-radius);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Estilo para los elementos de la lista de participantes */
#lista-participantes li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--padding-container);
    margin-bottom: var(--gap-list-items);
    background-color: var(--background-color-item);
    border: 1px solid var(--border-color-item);
    border-radius: var(--border-radius);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

#### 3. RESTful: Organización Lógica de Estilos
Se ha organizado el archivo CSS de manera lógica para facilitar la lectura y el mantenimiento. Los estilos se organizan de manera que las variables CSS se definen primero, seguidas por los estilos del contenedor principal y luego los estilos de los elementos de la lista. Esto facilita la lectura y el mantenimiento del código CSS.

**Ejemplo:**
```css
/* Variables de diseño */
:root {
    --max-width-container: 800px;
    --padding-container: 20px;
    --gap-list-items: 10px;
    --border-radius: 5px;
    --background-color-item: var(--white-color);
    --border-color-item: var(--border-color);
}

/* Contenedor principal para los participantes */
#participantes-container {
    max-width: var(--max-width-container);
    margin: auto;
    padding: var(--padding-container);
    background-color: var(--background-color);
    border-radius: var(--border-radius);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Estilo para los elementos de la lista de participantes */
#lista-participantes li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--padding-container);
    margin-bottom: var(--gap-list-items);
    background-color: var(--background-color-item);
    border: 1px solid var(--border-color-item);
    border-radius: var(--border-radius);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

### main.js

#### 1. Cookbook: Modularización y Funciones Reutilizables
Se ha modularizado el código en un IIFE (Immediately Invoked Function Expression) para encapsular el comportamiento y evitar la contaminación del espacio global de nombres. Se encapsulan las funciones en un módulo para evitar conflictos de nombres y mejorar la organización del código.

**Ejemplo:**
```javascript
// Módulo para manejar el comportamiento de los participantes
const ParticipantesModule = (() => {
    // Código del módulo
    return {
        init,
    };
})();
```

#### 2. Pipeline: Flujo de Datos y Promesas
Se ha mejorado el flujo de datos usando promesas para manejar la carga de participantes desde una API. Uso de promesas para manejar asincronía y flujo de datos de manera clara y legible.

**Ejemplo:**
```javascript
const cargarParticipantes = () => {
    fetch('/api/participantes')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar los participantes');
            }
            return response.json();
        })
        .then(data => {
            console.log(data); // Log de los participantes cargados
            mostrarParticipantes(data); // Mostrar participantes en la interfaz
        })
        .catch(error => {
            console.error('Error:', error); // Log de cualquier error al cargar los participantes
            mostrarError('No se pudieron cargar los participantes.');
        });
};
```

#### 3. Things: Encapsulación de Funcionalidades
Se han encapsulado funcionalidades específicas en funciones para mejorar la legibilidad y reutilización del código. Cada funcionalidad específica (mostrar participantes, mostrar error) se encapsula en su propia función, mejorando la organización y la mantenibilidad del código.

**Ejemplo:**
```javascript
const mostrarParticipantes = (participantes) => {
    const listaParticipantes = document.getElementById('lista-participantes');
    listaParticipantes.innerHTML = ''; // Limpiar la lista antes de agregar los nuevos participantes

    participantes.forEach(participante => {
        const li = document.createElement('li');
        li.textContent = participante.nombre;
        listaParticipantes.appendChild(li);
    });
};
```

#### 4. Error/Exception Handling: Manejo de Errores
Se ha añadido manejo de errores para todas las operaciones asíncronas y se proporciona retroalimentación al usuario. Se manejan los errores de manera uniforme, proporcionando logs de errores y retroalimentación al usuario.

**Ejemplo:**
```javascript
fetch('/api/participantes')
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al cargar los participantes');
        }
        return response.json();
    })
    .catch(error => {
        console.error('Error:', error); // Log de cualquier error al cargar los participantes
        mostrarError('No se pudieron cargar los participantes.');
    });
```

#### 5. RESTful: Organización Lógica y Semántica
Se ha organizado el código de manera lógica y semántica, siguiendo las mejores prácticas para mejorar la legibilidad y mantenibilidad. El código está organizado de manera lógica, con la inicialización del módulo en la carga del documento y las funciones encapsuladas dentro de un módulo.

**Ejemplo:**
```javascript
document.addEventListener('DOMContentLoaded', () => {
    console.log("Documento cargado y listo."); // Log para indicar que el documento está completamente cargado
    cargarParticipantes(); // Cargar participantes al cargar la página
});
```

### participantes.js

#### 1. Cookbook: Modularización y Funciones Reutilizables
Se han añadido funciones reutilizables para cargar participantes, mostrar participantes y manejar el envío del formulario. La lógica se encapsula en funciones específicas, mejorando la organización y reutilización del código.

**Ejemplo:**
```javascript
const cargarParticipantes = () => {
    fetch('/participantes')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar los participantes');
            }
            return response.json();
        })
        .then(data => {
            mostrarParticipantes(data);
        })
        .catch(error => {
            console.error('Error:', error);
            mostrarError('No se pudieron cargar los participantes.');
        });
};
```

#### 2. Error/Exception Handling: Manejo de Errores
Se ha añadido manejo de errores para todas las operaciones asíncronas y se proporciona retroalimentación en la consola. Se manejan los errores de manera uniforme, proporcionando logs de errores y retroalimentación al usuario.

**Ejemplo:**
```javascript
fetch('/participantes')
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al cargar los participantes');
        }
        return response.json();
    })
    .catch(error => {
        console.error('Error:', error);
        mostrarError('No se pudieron cargar los participantes.');
    });
```

#### 3. Things: Encapsulación de Funcionalidades
Se han encapsulado funcionalidades específicas en funciones para mejorar la legibilidad y reutilización del código. Cada funcionalidad específica (cargar participantes, mostrar participantes, agregar participante) se encapsula en su propia función, mejorando la organización y la mantenibilidad del código.

**Ejemplo:**
```javascript
const mostrarParticipantes = (participantes) => {
    listaParticipantes.innerHTML = ''; // Limpiar la lista antes de agregar los nuevos participantes
    participantes.forEach(participante => {
        const item = document.createElement('li');
        item.textContent = participante.nombre;
        listaParticipantes.appendChild(item);
    });
};
```
### index.html

#### 1. Cookbook: Estructura y Enlaces Consistentes
El código HTML sigue una estructura consistente, donde se incluyen las hojas de estilo y los scripts JavaScript de manera ordenada y modular. Los enlaces a las hojas de estilo y scripts están organizados de manera lógica y ordenada.

**Ejemplo:**
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Participantes</title>
    <!-- Vincular hojas de estilo CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/estilos_generales.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/participantes.css') }}">
</head>
```

#### 2. Pipeline: Flujo de Carga de Recursos
El código HTML asegura que los recursos (hojas de estilo y scripts) se cargan en el orden adecuado para garantizar que el estilo y el comportamiento se apliquen correctamente. Los scripts se cargan después del contenido HTML para asegurar que el DOM esté completamente cargado antes de ejecutar el código JavaScript.

**Ejemplo:**
```html
<!-- Vincular archivos JavaScript -->
<script src="{{ url_for('static', filename='js/main.js') }}"></script>
<script src="{{ url_for('static', filename='js/participantes.js') }}"></script>
```

#### 3. RESTful: Organización Semántica y Estructura Lógica
El código HTML sigue una estructura semántica, con elementos claramente definidos para los diferentes componentes de la página. Uso de etiquetas HTML semánticas para estructurar el contenido, mejorando la accesibilidad y mantenibilidad del código.

**Ejemplo:**
```html
<body>
    <div id="participantes-container">
        <h1>Lista de Participantes</h1>
        <!-- Lista para mostrar los participantes -->
        <ul id="lista-participantes"></ul>

        <!-- Formulario para agregar un nuevo participante -->
        <form id="form-participante">
            <input type="text" id="nombre" placeholder="Nombre del participante" required>
            <button type="submit">Agregar Participante</button>
        </form>
    </div>
</body>
```

### presentacion/_init_.py

#### 1. Cookbook: Modularización y Funciones Reutilizables
Se ha creado una función específica create_app() para configurar y retornar la instancia de la aplicación Flask, siguiendo un patrón de fábrica. La configuración de la aplicación se encapsula en una función reutilizable, mejorando la organización y facilitando las pruebas.

**Ejemplo:**
```python
def create_app():
    """
    Crea y configura una instancia de la aplicación Flask.

    Returns:
        app (Flask): La instancia de la aplicación Flask configurada.
    """
    app = Flask(__name__)
    # Registro de Blueprints
    app.register_blueprint(participantes_bp)
    app.register_blueprint(proceso_electoral_bp)
    
    return app
```

#### 2. Pipeline: Flujo de Configuración
La función create_app() asegura que la configuración y el registro de blueprints se realizan en el orden adecuado para garantizar que la aplicación esté correctamente configurada antes de ser usada. Los blueprints se registran en un flujo claro y ordenado, asegurando que la configuración de la aplicación sea lógica y predecible.

**Ejemplo:**
```python
app = Flask(__name__)

# Registro de Blueprints
app.register_blueprint(participantes_bp)
app.register_blueprint(proceso_electoral_bp)
```

#### 3. Error/Exception Handling: Manejo de Errores
Se ha añadido manejo de errores para capturar y registrar cualquier excepción que ocurra durante el registro de blueprints, proporcionando retroalimentación en el log de la aplicación. Se manejan los errores de manera uniforme, registrando cualquier excepción que ocurra durante el registro de blueprints y proporcionando retroalimentación en el log de la aplicación.

**Ejemplo:**
```python
try:
    # Registro de Blueprints
    app.register_blueprint(participantes_bp)
    app.register_blueprint(proceso_electoral_bp)
except Exception as e:
    app.logger.error(f"Error al registrar blueprints: {e}")
    raise
```

### main.py

#### 1. Cookbook: Función Principal y Modularización
Se ha creado una función principal main() para encapsular la lógica de inicialización y ejecución de la aplicación. La lógica de inicialización y ejecución de la aplicación se encapsula en una función main(), mejorando la organización y la posibilidad de reutilización del código.

**Ejemplo:**
```python
def main():
    """
    Punto de entrada principal para ejecutar la aplicación Flask.
    """
    # Crear una instancia de la aplicación Flask
    app = create_app()

    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)
```

#### 2. Pipeline: Flujo de Inicialización
El código sigue un flujo claro y ordenado para inicializar y ejecutar la aplicación Flask. La aplicación se inicializa y se ejecuta de manera lógica y ordenada, asegurando que todos los componentes se configuren correctamente antes de iniciar la ejecución.

**Ejemplo:**
```python
# Crear una instancia de la aplicación Flask
app = create_app()

# Ejecutar la aplicación en modo de depuración
app.run(debug=True)
```

#### 3. Lazy-Rivers: Inicialización Bajo Demanda
El código se asegura de que la instancia de la aplicación Flask y su ejecución solo se realicen cuando el archivo se ejecute directamente, evitando inicializaciones innecesarias. La función main() solo se llama si el script se ejecuta directamente, lo que evita inicializaciones innecesarias cuando el módulo es importado por otros módulos.

**Ejemplo:**
```python
if __name__ == "__main__":
    main()
```
