#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from Model.dominio.proceso_electoral.Eleccion import Eleccion

class IAdministradorEleccion(ABC):
    @abstractmethod
    def registrar_admin(self, nombre: str, password: str, id: str) -> None:
        """Registra a un administrador con el nombre, la contraseña y el ID proporcionados."""
        pass

    @abstractmethod
    def configurar_eleccion(self, eleccion: Eleccion, nueva_fecha_inicio: str = None, nueva_fecha_fin: str = None, nuevos_candidatos: list = None) -> None:
        """Configura una elección actualizando la fecha de inicio, la fecha de fin y la lista de candidatos."""
        pass

    @abstractmethod
    def agregar_candidato(self, eleccion: Eleccion, candidato: str) -> None:
        """Agrega un candidato a la elección."""
        pass

    @abstractmethod
    def eliminar_candidato(self, eleccion: Eleccion, candidato: str) -> None:
        """Elimina un candidato de la elección."""
        pass
