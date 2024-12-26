#!/usr/bin/python
# -*- coding: utf-8 -*-

from Model.dominio.proceso_electoral.interfaces.Iregistro_electoral_repositorio import IRegistroElectoralRepositorio
from Model.models.registro_electoral import RegistroElectoralModelo
from Model.repositorio.MySQL.registro_electoral_repositorio_impl import registro_electoral_repositorio_impl


class RegistroElectoral(IRegistroElectoralRepositorio):
    def __init__(self):
        """Inicializa las listas de electores, candidatos y partidos."""
        self.lista_electores = []  
        self.lista_candidatos = []  
        self.lista_partidos = []  
        return 
    
    def agregar_elector(self, elector) -> None:
        """Agrega un elector a la lista de electores."""
        self.lista_electores.append(elector)

    def eliminar_elector(self, elector) -> None:
        """Elimina un elector de la lista de electores."""
        if elector in self.lista_electores:
            self.lista_electores.remove(elector)

    def agregar_candidato(self, candidato) -> None:
        """Agrega un candidato a la lista de candidatos."""
        self.lista_candidatos.append(candidato)

    def eliminar_candidato(self, candidato) -> None:
        """Elimina un candidato de la lista de candidatos."""
        if candidato in self.lista_candidatos:
            self.lista_candidatos.remove(candidato)

    def agregar_partido(self, partido) -> None:
        """Agrega un partido a la lista de partidos."""
        self.lista_partidos.append(partido)

    def eliminar_partido(self, partido) -> None:
        """Elimina un partido de la lista de partidos."""
        if partido in self.lista_partidos:
            self.lista_partidos.remove(partido)

    def guardar_registro(self):
        registro_modelo = RegistroElectoralModelo(
            lista_electores="|".join(self.lista_electores),
            lista_candidatos="|".join(self.lista_candidatos),
            lista_partidos="|".join(self.lista_partidos)
        )
        registro_electoral_repositorio_impl.ingresar_nuevo_registro(registro_modelo)

    def eliminar_registro(self, registro_id):
        registro_modelo = RegistroElectoralModelo.query.filter_by(id=registro_id).first()
        if registro_modelo:
            registro_electoral_repositorio_impl.eliminar_registro(registro_modelo)

    def obtener_registro(self, registro_id):
        registro_modelo = RegistroElectoralModelo.query.filter_by(id=registro_id).first()
        if registro_modelo:
            self.lista_electores = registro_modelo.lista_electores.split("|")
            self.lista_candidatos = registro_modelo.lista_candidatos.split("|")
            self.lista_partidos = registro_modelo.lista_partidos.split("|")
        return self.lista_electores, self.lista_candidatos, self.lista_partidos
    