#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class IEditor(ABC):
    #Elector
    @abstractmethod
    def registrar(self, nombre, apellido)->None:
        pass 

    @abstractmethod
    def iniciar_sesion(self, correo, contraseña)->None:
        pass 
    
    @abstractmethod
    def votar(self)->None:
        pass 
    
    def estado_voto(self)->None:
        pass 

    def editar_datos(self, nombre, apellido)->None:
        pass 
    
