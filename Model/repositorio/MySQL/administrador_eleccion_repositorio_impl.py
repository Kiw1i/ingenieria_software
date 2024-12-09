#!/usr/bin/python
#-*- coding: utf-8 -*-
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from Model.extensions import db
from Model.models.administrador_eleccion import AdministradorModelo

class AdministradorEleccionRepositorioImpl:
    @staticmethod
    def insertar_administrador(admin):
        try:
            db.session.add(admin)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
    
    @staticmethod
    def eliminar_administrador(admin):
        try:
            entrada = db.session.query(AdministradorModelo).filter_by(id = admin.id).one()
            db.session.delete(entrada)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @staticmethod
    def get_administrador_nombre(admin_id):
        admin_nombre = ""
        try:
            entrada = db.session.query(AdministradorModelo).filter_by(id = admin_id).one()
            admin_nombre = entrada.nombre
        except NoResultFound:
            print(f"No se encontró una entrada con la id {admin_id}\n")
            return None
        except SQLAlchemyError as e:
            print(f"Hubo un error al consultar la base de datos: {e}")
            return None
        finally:
            db.session.close()
        return admin_nombre

    @staticmethod
    def set_administrador_eleccion(admin_id, eleccion_a_asignar):
        try:
            entrada = db.session.query(AdministradorModelo).filter_by(id = admin_id).one()
            entrada.eleccion_asignada = eleccion_a_asignar
            db.session.commit()
        except NoResultFound:
            print(f"No se encontró una entrada con la id {admin_id}\n")
        except SQLAlchemyError as e:
            print(f"Hubo un error al consultar la base de datos: {e}")
        finally:
            db.session.close()
    
    @staticmethod
    def get_administrador_eleccion(admin_id):
        admin_eleccion = ""
        try:
            entrada = db.session.query(AdministradorModelo).filter_by(id = admin_id).one()
            admin_eleccion = entrada.eleccion_asignada
        except NoResultFound:
            print(f"No se encontró una entrada con la id {admin_id}\n")
            return None
        except SQLAlchemyError as e:
            print(f"Hubo un error al consultar la base de datos: {e}")
            return None
        finally:
            db.session.close()
        return admin_eleccion