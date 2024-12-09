#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

class Voto:
    def __init__(self):
        """Inicializa un nuevo objeto Voto con valores predeterminados."""
        self.fecha: Optional[datetime] = None
        self.hora: Optional[datetime] = None
        self.elector: Optional[str] = None  # Suponiendo que elector es un string con el nombre
        self.id_voto: Optional[str] = None  # Suponiendo que id_voto es un string

    def registrar_voto(self, elector: str, id_voto: str, fecha: Optional[datetime] = None, hora: Optional[datetime] = None) -> None:
        """Registra un voto con el elector y el ID, y establece la fecha y la hora actuales si no se proporcionan."""
        self.elector = elector
        self.id_voto = id_voto
        
        if fecha is None:
            self.fecha = datetime.now().date()
        else:
            self.fecha = fecha

        if hora is None:
            self.hora = datetime.now().time()
        else:
            self.hora = hora

    def confirmar_voto(self):
        if not self.elector:
            raise ValueError("Elector no proporcionado.")
        if not self.fecha:
            raise ValueError("Fecha no proporcionada.")
        if not self.hora:
            raise ValueError("Hora no proporcionada.")
        if not self.id_voto:
            raise ValueError("ID de voto no proporcionado.")
        print("Voto confirmado")
        return True
