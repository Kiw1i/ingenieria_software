#!/usr/bin/python
#-*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class IResultados(ABC):
    @abstractmethod
    def agregar_voto(self, candidato:str)->None:
        pass

    @abstractmethod
    def calcular_porcentajes(self)-> None:
        pass

    @abstractmethod
    def mostrar_resultados(self)-> dict:
        pass
