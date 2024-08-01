#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class IEditor(ABC):
    #Elector
    @abstractmethod
    def registrar(self, nombre, apellido)->None:
        pass 

    @abstractmethod
    def iniciar_sesion(self, correo, contrasenia)->None:
        pass 
    
    @abstractmethod
    def votar(self)->None:
        pass 
    
    @abstractmethod
    def estado_voto(self)->None:
        pass 
    
    @abstractmethod    
    def editar_datos(self, nombre, apellido)->None:
        pass 
    