#!/usr/bin/python
# -*- coding: utf-8 -*-
from Model.dominio.proceso_electoral.interfaces.Iadministrador_eleccion import IAdministradorEleccion
from Model.dominio.proceso_electoral import Eleccion
from Model.models.administrador_eleccion import AdministradorModelo
from Model.repositorio.MySQL.administrador_eleccion_repositorio_impl import AdministradorEleccionRepositorioImpl

class AdministradorEleccion(IAdministradorEleccion):
    def __init__(self, nombre=None, admin_id=None, password=None):
        self.nombre = nombre
        self.admin_id = admin_id
        self.password = password

    def registrar_administrador(self, nombre: str, password: str, admin_id: str) -> None:
        self.nombre = nombre
        self.password = password
        self.admin_id = admin_id
        admin_modelo = AdministradorModelo(id=admin_id, nombre=nombre, eleccion_asignada=None)
        AdministradorEleccionRepositorioImpl.insertar_administrador(admin_modelo)

    def configurar_eleccion(self, eleccion: Eleccion, nueva_fecha_inicio: str = None, 
                            nueva_fecha_fin: str = None, nuevos_candidatos: list = None) -> None:
        if nueva_fecha_inicio:
            eleccion.iniciar_eleccion(nueva_fecha_inicio)

        if nueva_fecha_fin:
            eleccion.finalizar_eleccion(nueva_fecha_fin)

        if nuevos_candidatos is not None:
            eleccion.lista_candidatos = nuevos_candidatos

    def agregar_candidato(self, eleccion: Eleccion, candidato: str) -> None:
        eleccion.lista_candidatos.append(candidato)

    def eliminar_candidato(self, eleccion: Eleccion, candidato: str) -> None:
        if candidato in eleccion.lista_candidatos:
            eleccion.lista_candidatos.remove(candidato)

    def obtener_nombre_administrador(self, admin_id):
        return AdministradorEleccionRepositorioImpl.get_administrador_nombre(admin_id)

    def asignar_eleccion(self, admin_id, eleccion_a_asignar):
        AdministradorEleccionRepositorioImpl.set_administrador_eleccion(admin_id, eleccion_a_asignar)

    def obtener_eleccion_asignada(self, admin_id):
        return AdministradorEleccionRepositorioImpl.get_administrador_eleccion(admin_id)