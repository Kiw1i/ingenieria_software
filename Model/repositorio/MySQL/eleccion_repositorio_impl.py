#!/usr/bin/python
#-*- coding: utf-8 -*-
from Model.extensions import db
from Model.models.eleccion import EleccionModelo

class eleccion_repositorio_impl:
    @staticmethod
    def nueva_eleccion(eleccion):
        try:
            db.session.add(eleccion)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @staticmethod
    def eliminar_eleccion(eleccion):
        try:
            entrada = db.session.query(EleccionModelo).filter_by(codigo = eleccion.codigo).one()
            db.session.delete(entrada)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
