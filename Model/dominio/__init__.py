from Model.dominio.proceso_electoral.interfaces import Iadministrador_eleccion, Ieleccion, Iregistro_electoral_repositorio, Iresultados
from Model.dominio.participantes import Elector
from Model.dominio.proceso_electoral import AdministradorEleccion,Eleccion,RegistroElectoral,Resultados

__all__ = [
    "Elector",
    "AdministradorEleccion",
    "RegistroElectoral",
    "Resultados",
    "Iadministrador_eleccion",
    "Ieleccion",
    "Iregistro_electoral_repositorio",
    "Iresultados"
]