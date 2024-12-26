import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

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
