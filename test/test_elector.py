import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from unittest.mock import Mock, patch
from Model.dominio.participantes.Candidato import Candidato
from Model.dominio.participantes.Elector import Elector
from Model.models.eleccion import EleccionModelo
from Model.repositorio.MySQL.eleccion_repositorio_impl import eleccion_repositorio_impl

# Fixtures
@pytest.fixture
def elector():
    return Elector(id=1, correo='test@example.com', contrasena='password123', nombre='Juan', apellido='Pérez')

@pytest.fixture
def candidato(elector):
    """Fixture para crear una instancia de Candidato antes de cada prueba."""
    return Candidato(
        id=2,
        correo='candidato@example.com',
        contrasena='password123',
        nombre='Pedro',
        apellido='Gómez',
        candidatura='Presidente',
        propuesta='Reformar la educación'
    )

# Test para modificar propuesta
def test_modificar_propuesta(candidato):
    """Prueba el método modificar_propuesta."""
    nueva_propuesta = "Mejorar la salud pública"
    resultado = candidato.modificar_propuesta(nueva_propuesta)
    assert candidato.propuesta == nueva_propuesta
    assert resultado == "Propuesta modificada exitosamente"

def test_modificar_propuesta_invalida(candidato):
    """Prueba manejar propuestas inválidas."""
    with pytest.raises(ValueError):
        candidato.modificar_propuesta("")

# Test para actualizar perfil
def test_actualizar_perfil(candidato, elector):
    """Prueba el método actualizar_perfil."""
    nueva_candidatura = "Vicepresidente"
    nueva_propuesta = "Aumentar el presupuesto de educación"
    resultado = candidato.actualizar_perfil(elector, nueva_candidatura, nueva_propuesta)
    
    assert candidato.nombre == elector.nombre
    assert candidato.apellido == elector.apellido
    assert candidato.candidatura == nueva_candidatura
    assert candidato.propuesta == nueva_propuesta
    assert resultado == "Perfil actualizado exitosamente"

def test_actualizar_perfil_no_altera_id(candidato, elector):
    """Asegura que actualizar perfil no modifica campos no relacionados."""
    candidato_id_original = candidato.id
    candidato.actualizar_perfil(elector, "Nueva Candidatura", "Nueva Propuesta")
    assert candidato.id == candidato_id_original

# Test para registrar candidato
def test_registrar_candidato(candidato, elector):
    """Prueba el método registrar_candidato."""
    nueva_candidatura = "Gobernador"
    nueva_propuesta = "Promover el empleo juvenil"
    resultado = candidato.registrar_candidato(elector, nueva_candidatura, nueva_propuesta)
    
    assert candidato.id == elector.id
    assert candidato.correo == elector.correo
    assert candidato.nombre == elector.nombre
    assert candidato.apellido == elector.apellido
    assert candidato.candidatura == nueva_candidatura
    assert candidato.propuesta == nueva_propuesta
    assert resultado == "Candidato registrado exitosamente"

def test_registrar_candidato_con_datos_incompletos(candidato, elector):
    """Prueba registrar candidato con datos incompletos."""
    with pytest.raises(ValueError):
        candidato.registrar_candidato(elector, None, "Propuesta válida")

# Test para guardar elección
@patch('Model.dominio.participantes.Candidato.eleccion_repositorio_impl.nueva_eleccion')
def test_guardar_eleccion(mock_nueva_eleccion, candidato):
    """Prueba el método guardar_eleccion."""
    eleccion = Mock(
        codigo=1,
        tipo_eleccion='Presidencial',
        fecha_inicio='2022-01-01',
        fecha_cierre='2022-01-02',
        lista_candidatos=[candidato]
    )
    resultado = candidato.guardar_eleccion(eleccion)
    
    mock_nueva_eleccion.assert_called_once()
    assert resultado == "Elección guardada exitosamente"

@patch('Model.dominio.participantes.Candidato.eleccion_repositorio_impl.nueva_eleccion', side_effect=Exception("Error al guardar"))
def test_guardar_eleccion_error(mock_nueva_eleccion, candidato):
    """Prueba manejar errores al guardar una elección."""
    eleccion = Mock(
        codigo=1,
        tipo_eleccion='Presidencial',
        fecha_inicio='2022-01-01',
        fecha_cierre='2022-01-02',
        lista_candidatos=[candidato]
    )
    with pytest.raises(Exception) as excinfo:
        candidato.guardar_eleccion(eleccion)
    assert "Error al guardar" in str(excinfo.value)
    mock_nueva_eleccion.assert_called_once()

@patch('Model.dominio.participantes.Candidato.eleccion_repositorio_impl.nueva_eleccion')
def test_guardar_eleccion_masiva(mock_nueva_eleccion, candidato):
    """Prueba guardar múltiples elecciones."""
    elecciones = [
        Mock(codigo=i, tipo_eleccion='General', fecha_inicio='2022-01-01', fecha_cierre='2022-01-02', lista_candidatos=[candidato])
        for i in range(1000)
    ]
    for eleccion in elecciones:
        candidato.guardar_eleccion(eleccion)
    assert mock_nueva_eleccion.call_count == 1000

# Test para independencia de datos
def test_candidato_independencia_datos(candidato):
    """Prueba que las copias de un candidato sean independientes."""
    otro_candidato = Candidato(
        id=candidato.id,
        correo=candidato.correo,
        contrasena=candidato.contrasena,
        nombre=candidato.nombre,
        apellido=candidato.apellido,
        candidatura=candidato.candidatura,
        propuesta=candidato.propuesta
    )
    otro_candidato.modificar_propuesta("Propuesta Diferente")
    assert candidato.propuesta != otro_candidato.propuesta
