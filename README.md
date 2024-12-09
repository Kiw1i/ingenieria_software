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
# SOLID

## Principios SOLID aplicados
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

Asimismo, la clase AdministradorEleccion se encarga únicamente de registrar a un administrador, cumpliendo con el principio.

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

### 3. Principio de Segregación de Interfaces (ISP):
La interfaz IResultados está diseñada para proporcionar métodos específicos relacionados con la gestión de resultados, cumpliendo con el principio de Segregación de Interfaces (ISP) al asegurar que las implementaciones solo dependan de métodos que realmente utilizan `from abc import ABC`, que son `@abstractmethod`.

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

El controlador depende de una abstracción (ProcesoElectoralServicio) en lugar de una implementación concreta.

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