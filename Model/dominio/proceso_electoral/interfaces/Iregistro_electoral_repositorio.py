from abc import ABC, abstractmethod

class IRegistroElectoralRepositorio(ABC):
    @abstractmethod
    def agregar_elector(self, elector: str) -> None:
        """Agrega un elector al registro.

        Args:
            elector: Un objeto de tipo Elector que representa al elector a agregar.
        """
        pass

    @abstractmethod
    def eliminar_elector(self, elector: str) -> None:
        """Elimina un elector del registro.

        Args:
            elector: Un objeto de tipo Elector que representa al elector a eliminar.
        """
        pass

    @abstractmethod
    def agregar_candidato(self, candidato: str) -> None:
        """Agrega un candidato al registro.

        Args:
            candidato: Un objeto de tipo Candidato que representa al candidato a agregar.
        """
        pass

    @abstractmethod
    def eliminar_candidato(self, candidato: str) -> None:
        """Elimina un candidato del registro.

        Args:
            candidato: Un objeto de tipo Candidato que representa al candidato a eliminar.
        """
        pass

    @abstractmethod
    def agregar_partido(self, partido: str) -> None:
        """Agrega un partido al registro.

        Args:
            partido: Un objeto de tipo Partido que representa al partido a agregar.
        """
        pass

    @abstractmethod
    def eliminar_partido(self, partido: str) -> None:
        """Elimina un partido del registro."""
        pass