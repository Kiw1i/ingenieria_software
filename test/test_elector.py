import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Model.dominio.participantes.Elector import Elector


@pytest.fixture
def elector():
    return Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')


def test_elector_initialization(elector):
    assert elector.id == 1
    assert elector.correo == 'test@example.com'
    assert elector.contrasena == 'password123'
    assert elector.nombre == 'Juan'
    assert elector.apellido == 'Pérez'
    assert elector.ha_votado == False


def test_registrar(elector):
    resultado = elector.registrar(nombre='Ana', apellido='García')
    assert elector.nombre == 'Ana'
    assert elector.apellido == 'García'
    assert resultado == "Registro exitoso"


def test_iniciar_sesion_correcto(elector):
    resultado = elector.iniciar_sesion(correo='test@example.com', contrasena='password123')
    assert resultado == "Inicio de sesión exitoso"


def test_iniciar_sesion_incorrecto(elector):
    resultado = elector.iniciar_sesion(correo='wrong@example.com', contrasena='wrongpassword')
    assert resultado == "Correo o contraseña incorrectos"


def test_votar_por_primera_vez(elector):
    resultado = elector.votar()
    assert elector.ha_votado == True
    assert resultado == "Voto registrado"


def test_votar_por_segunda_vez(elector):
    elector.votar()  
    resultado = elector.votar()  
    assert elector.ha_votado == True
    assert resultado == "Ya ha votado"


def test_estado_voto_no_votado(elector):
    assert elector.estado_voto() == "No ha votado"


def test_estado_voto_despues_de_votar(elector):
    elector.votar()
    assert elector.estado_voto() == "Ha votado"


def test_editar_datos(elector):
    resultado = elector.editar_datos(nombre='Carlos', apellido='López')
    assert elector.nombre == 'Carlos'
    assert elector.apellido == 'López'
    assert resultado == "Datos editados exitosamente"



def test_elector_initialization_with_empty_values():
    elector = Elector(id=None, correo='', contrasena='', nombre='', apellido='')
    assert elector.id is None
    assert elector.correo == ''
    assert elector.contrasena == ''
    assert elector.nombre == ''
    assert elector.apellido == ''


def test_elector_initial_state():
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    assert elector.estado_voto() == "No ha votado"


def test_editar_datos_con_valores_vacios():
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    resultado = elector.editar_datos(nombre='', apellido='')
    assert elector.nombre == ''
    assert elector.apellido == ''
    assert resultado == "Datos editados exitosamente"


def test_registrar_con_valores_vacios():
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    resultado = elector.registrar(nombre='', apellido='')
    assert elector.nombre == ''
    assert elector.apellido == ''
    assert resultado == "Registro exitoso"


def test_votacion_sin_iniciar_sesion():
    elector = Elector(id=1, correo=None, contrasena=None, nombre='Juan', apellido='Pérez')
    resultado = elector.votar()
    assert resultado == "Ya ha votado"  


def test_iniciar_sesion_despues_de_votacion():
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    elector.votar()
    resultado = elector.iniciar_sesion(correo='test@example.com', contrasena='wrongpassword')
    assert resultado == "Correo o contraseña incorrectos"


def test_votar_sin_cambiar_estado():
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    elector.votar()
    estado_previo = elector.estado_voto()
    elector.votar()  
    assert elector.estado_voto() == estado_previo  


def test_multiple_votaciones_y_edicion():
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    assert elector.estado_voto() == "No ha votado"
    elector.votar()
    assert elector.estado_voto() == "Ha votado"
    elector.editar_datos(nombre="Carlos", apellido="López")
    assert elector.nombre == "Carlos"
    assert elector.apellido == "López"


def test_iniciar_sesion_despues_de_editar_datos():
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    elector.editar_datos(nombre='Carlos', apellido='López')
    resultado = elector.iniciar_sesion(correo='test@example.com', contrasena='password123')
    assert resultado == "Inicio de sesión exitoso"


def test_votar_con_datos_incorrectos():
    elector = Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')
    elector.nombre = "No válido"
    resultado = elector.votar()
    assert resultado == "Ya ha votado" 
