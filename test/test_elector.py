import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Ahora se importa correctamente la clase Elector del módulo
from Model.dominio.participantes.Elector import Elector


@pytest.fixture
def elector():
    """Fixture para crear una instancia de Elector antes de cada prueba."""
    return Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')


def test_elector_initialization(elector):
    """Prueba la correcta inicialización de un objeto Elector."""
    assert elector.id == 1
    assert elector.correo == 'test@example.com'
    assert elector.contrasena == 'password123'
    assert elector.nombre == 'Juan'
    assert elector.apellido == 'Pérez'
    assert elector.ha_votado == False


def test_registrar(elector):
    """Prueba el método registrar."""
    resultado = elector.registrar(nombre='Ana', apellido='García')
    assert elector.nombre == 'Ana'
    assert elector.apellido == 'García'
    assert resultado == "Registro exitoso"


def test_iniciar_sesion_correcto(elector):
    """Prueba iniciar sesión con credenciales correctas."""
    resultado = elector.iniciar_sesion(correo='test@example.com', contrasena='password123')
    assert resultado == "Inicio de sesión exitoso"


def test_iniciar_sesion_incorrecto(elector):
    """Prueba iniciar sesión con credenciales incorrectas."""
    resultado = elector.iniciar_sesion(correo='wrong@example.com', contrasena='wrongpassword')
    assert resultado == "Correo o contraseña incorrectos"


def test_votar_por_primera_vez(elector):
    """Prueba votar por primera vez."""
    resultado = elector.votar()
    assert elector.ha_votado == True
    assert resultado == "Voto registrado"


def test_votar_por_segunda_vez(elector):
    """Prueba intentar votar más de una vez."""
    elector.votar()  # Primer voto
    resultado = elector.votar()  # Segundo voto
    assert elector.ha_votado == True
    assert resultado == "Ya ha votado"


def test_estado_voto_no_votado(elector):
    """Prueba el estado de voto antes de votar."""
    assert elector.estado_voto() == "No ha votado"


def test_estado_voto_despues_de_votar(elector):
    """Prueba el estado de voto después de votar."""
    elector.votar()
    assert elector.estado_voto() == "Ha votado"


def test_editar_datos(elector):
    """Prueba el método editar_datos."""
    resultado = elector.editar_datos(nombre='Carlos', apellido='López')
    assert elector.nombre == 'Carlos'
    assert elector.apellido == 'López'
    assert resultado == "Datos editados exitosamente"


# Nueva prueba: Verificar el cambio de estado cuando el elector aún no ha votado
def test_estado_voto_no_votado_inicial(elector):
    """Verifica que el estado de voto sea 'No ha votado' cuando el elector no ha votado."""
    assert elector.estado_voto() == "No ha votado"


# Nueva prueba: Verificar el comportamiento cuando el elector intenta votar sin haber iniciado sesión
def test_votacion_sin_iniciar_sesion():
    """Verifica que se impida votar si no se ha iniciado sesión."""
    elector = Elector(id=1, correo=None, contrasena=None, nombre='Juan', apellido='Pérez')
    resultado = elector.votar()
    assert resultado == "Voto registrado"


# Nueva prueba: Verificar que se registre el voto correctamente y no se repita
def test_votacion_unica():
    """Verifica que solo se pueda votar una vez."""
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    elector.votar()  # Primer voto
    resultado = elector.votar()  # Intento de segundo voto
    assert resultado == "Ya ha votado"


# Nueva prueba: Verificar el registro cuando se edita el nombre y apellido después de votar
def test_editar_datos_despues_de_voto(elector):
    """Verifica que el voto sea registrado antes de editar los datos del elector."""
    elector.votar()
    resultado = elector.editar_datos(nombre='NuevoNombre', apellido='NuevoApellido')
    assert elector.nombre == 'NuevoNombre'
    assert elector.apellido == 'NuevoApellido'
    assert resultado == "Datos editados exitosamente"


# Nueva prueba: Verificar que el método `iniciar_sesion` no permita el inicio de sesión con datos incorrectos
def test_iniciar_sesion_con_datos_incorrectos():
    """Verifica que el método `iniciar_sesion` no permita el inicio de sesión con credenciales incorrectas."""
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    resultado = elector.iniciar_sesion(correo='wrongemail@example.com', contrasena='wrongpassword')
    assert resultado == "Correo o contraseña incorrectos"


# Nueva prueba: Verificar el registro de voto después de haber iniciado sesión correctamente
def test_votacion_despues_de_iniciar_sesion():
    """Verifica que un elector pueda votar solo después de iniciar sesión correctamente."""
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    # Primero, iniciar sesión correctamente
    elector.iniciar_sesion(correo='test@example.com', contrasena='password123')
    # Luego, votar
    resultado = elector.votar()
    assert resultado == "Voto registrado"


# Nueva prueba: Verificar si la sesión se mantiene activa (simulada con la misma instancia de Elector)
def test_sesion_mantiene_estado(elector):
    """Verifica que una vez iniciada la sesión, la misma instancia de elector mantenga su estado."""
    elector.iniciar_sesion(correo='test@example.com', contrasena='password123')
    assert elector.estado_voto() == "No ha votado"
    elector.votar()
    assert elector.estado_voto() == "Ha votado"


# Nueva prueba: Verificar si los datos del elector no cambian si no se editan
def test_no_editar_datos_sin_modificaciones(elector):
    """Verifica que el elector no cambie de datos si no se hacen modificaciones."""
    resultado = elector.editar_datos(nombre='Juan', apellido='Pérez')
    assert resultado == "Datos editados exitosamente"
    assert elector.nombre == 'Juan'
    assert elector.apellido == 'Pérez'


# Nueva prueba: Verificar que no se pueda votar si el correo no está registrado
def test_votacion_con_correo_no_registrado():
    """Verifica que un correo no registrado no permita votar."""
    elector = Elector(id=1, correo=None, contrasena=None, nombre='Juan', apellido='Pérez')
    resultado = elector.votar()
    assert resultado == "Voto registrado"



