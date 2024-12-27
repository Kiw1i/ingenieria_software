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

    @abstractmethod
    def guardar_eleccion(self, eleccion)->None:
        pass

    @abstractmethod
    def __init__(self, id, correo, contrasenia, nombre, apellido, candidatura, propuesta):
        pass

    @abstractmethod
    def __str__(self)->str:
        pass

    @abstractmethod
    def __repr__(self)->str:
        pass

    @abstractmethod
    def __eq__(self, other)->bool:
        pass

    @abstractmethod
    def __hash__(self)->int:
        pass

    @abstractmethod
    def __lt__(self, other)->bool:
        pass

    