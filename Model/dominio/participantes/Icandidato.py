#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class ICandidato(ABC):
    @abstractmethod
    def modificar_propuesta(self, propuesta:str)->None:
        pass 

    @abstractmethod
    def actualizar_perfil(self, elector, candidatura, propuesta)->None:
        pass 

    @abstractmethod
    def registrar_candidato(self, elector, candidatura, propuesta)->None:
        pass 

    