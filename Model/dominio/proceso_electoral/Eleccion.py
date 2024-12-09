#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from Model.dominio.proceso_electoral.Voto import Voto
from Model.dominio.proceso_electoral.Resultados import Resultados
from Model.dominio.participantes.Elector import Elector
from Model.dominio.proceso_electoral.interfaces.Ieleccion import IEleccion
from Model.models.eleccion import EleccionModelo
from Model.repositorio.MySQL.eleccion_repositorio_impl import eleccion_repositorio_impl

class Eleccion(IEleccion):
    def __init__(self, tipo_eleccion: str = None, fecha_inicio: datetime = None, fecha_fin: datetime = None):
        self.tipo_eleccion = tipo_eleccion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.lista_candidatos = []  # Lista de candidatos
        self.votos = []  
        self.resultados = Resultados()  

    def iniciar_eleccion(self, fecha_inicio: datetime) -> None:
        """Inicia la elección estableciendo la fecha de inicio."""
        self.fecha_inicio = fecha_inicio

    def finalizar_eleccion(self, fecha_fin: datetime) -> None:
        """Finaliza la elección estableciendo la fecha de fin."""
        self.fecha_fin = fecha_fin

    def registrar_voto(self, voto: Voto) -> None:
        """Registra un voto si es válido."""
        if isinstance(voto, Voto) and voto.confirmar_voto():
            self.votos.append(voto)
            self.resultados.agregar_voto(voto.elector.nombre)

    def obtener_resultados(self) -> dict:
        """Obtiene los resultados de la elección."""
        return self.resultados.mostrar_resultados()

    def enviar_notificacion(self, elector: Elector) -> None:
        """Envía una notificación al elector después de votar."""
        if isinstance(elector, Elector):
            return

    def guardar_eleccion(self):
        eleccion_modelo = EleccionModelo(
            tipo_eleccion=self.tipo_eleccion,
            fecha_inicio=self.fecha_inicio,
            fecha_cierre=self.fecha_fin,
            lista_candidatos="|".join(self.lista_candidatos)
        )
        eleccion_repositorio_impl.nueva_eleccion(eleccion_modelo)
    
    def eliminar_eleccion(self):
        eleccion_modelo = EleccionModelo.query.filter_by(tipo_eleccion=self.tipo_eleccion).first()
        if eleccion_modelo:
            eleccion_repositorio_impl.eliminar_eleccion(eleccion_modelo)
