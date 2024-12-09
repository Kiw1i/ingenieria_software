#!/usr/bin/python
# -*- coding: utf-8 -*-

from Model.dominio.proceso_electoral.interfaces.Iresultados import IResultados
from typing import List


class Resultados(IResultados):
    def __init__(self):
        """Inicializa la clase Resultados con total de votos y listas vacías."""
        self.total_votos: int = 0
        self.votos_candidatos: List[int] = []  # Lista de votos por candidato
        self.porcentajes_candidatos: List[float] = []  # Lista de porcentajes por candidato

    def agregar_votos(self, votos_candidatos: List[int]) -> None:
        """Añade los votos de los candidatos y actualiza el total de votos."""
        if not all(isinstance(voto, int) for voto in votos_candidatos):
            raise ValueError("Todos los votos deben ser enteros.")
        
        self.votos_candidatos = votos_candidatos
        self.total_votos = sum(votos_candidatos)
        self.calcular_porcentajes()

    def calcular_porcentajes(self) -> None:
        """Calcula el porcentaje de votos que obtuvo cada candidato."""
        if self.total_votos > 0:
            self.porcentajes_candidatos = [(votos / self.total_votos) * 100 for votos in self.votos_candidatos]
        else:
            self.porcentajes_candidatos = [0 for _ in self.votos_candidatos]

    def get_votos_totales(self) -> int:
        """Retorna el total de votos."""
        return self.total_votos

    def get_votos_candidatos(self) -> List[int]:
        """Retorna la lista de votos por candidato."""
        return self.votos_candidatos

    def get_porcentajes_candidatos(self) -> List[float]:
        """Retorna la lista de porcentajes de votos por candidato."""
        return self.porcentajes_candidatos

    def publicar_resultados(self) -> dict:
        """Publica los resultados mostrando los votos totales y los porcentajes por candidato."""
        return {
            "total_votos": self.get_votos_totales(),
            "votos_candidatos": self.get_votos_candidatos(),
            "porcentajes_candidatos": self.get_porcentajes_candidatos()
        }
        
