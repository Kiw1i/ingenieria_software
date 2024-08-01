#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from Model.dominio.proceso_electoral.Voto import Voto 
from Model.dominio.participantes.Elector import Elector  

class IEleccion(ABC):
    @abstractmethod
    def iniciar_eleccion(self, fecha_inicio: str) -> None:
        """Inicia la elección con la fecha proporcionada."""
        pass

    @abstractmethod
    def finalizar_eleccion(self, fecha_fin: str) -> None:
        """Finaliza la elección con la fecha proporcionada."""
        pass

    @abstractmethod
    def registrar_voto(self, voto: Voto) -> None:
        """Registra un voto en la elección."""
        pass

    @abstractmethod
    def obtener_resultados(self) -> dict:
        """Devuelve los resultados de la elección."""
        pass

    @abstractmethod
    def enviar_notificacion(self, elector: Elector) -> None:
        """Envía una notificación al elector."""
        pass
