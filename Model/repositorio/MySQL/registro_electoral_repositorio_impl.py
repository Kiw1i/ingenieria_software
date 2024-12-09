#!/usr/bin/python
#-*- coding: utf-8 -*-
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from Model.extensions import db
from Model.models.registro_electoral import RegistroElectoralModelo

class registro_electoral_repositorio_impl:
    @staticmethod
    def ingresar_nuevo_registro(registro):
        try:
            db.session.add(registro)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @staticmethod
    def eliminar_registro(registro):
        try:
            entrada = db.session.query(RegistroElectoralModelo).filter_by(id = registro.id).one()
            db.session.delete(entrada)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @staticmethod
    def agregar_elector_a_registro(registro_id, elector):
        try:
            entrada = db.session.query(RegistroElectoralModelo).filter_by(id = registro_id).one()
            entrada.lista_electores += '|' + elector  #elector.nombre / formato de ingreso de electores al registro?
            db.session.commit()
        except NoResultFound:
            print(f"No se encontró una entrada con la id {registro_id}\n")
        except SQLAlchemyError as e:
            print(f"Hubo un error al consultar la base de datos: {e}")
        finally:
            db.session.close()

    def obtener_elector_por_correo(self, correo):
        try:
            return db.session.query.filter_by(correo=correo).first()
        except Exception as e:
            print(f"Error al obtener elector por correo: {e}")
            return None