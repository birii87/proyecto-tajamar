from dataclasses import dataclass
from typing import Literal

Estado = Literal["pendiente", "en_progreso", "terminada", "fallida"]


@dataclass
class Tarea:
    nombre: str
    tiempo_estimado: float
    prioridad: int
    propietario: str
    estado: Estado = "pendiente"

    def empezar(self) -> None:
        self.estado = "en_progreso"

    def cambiar_a_terminada(self) -> None:
        self.estado = "terminada"

    def cambiar_a_fallida(self) -> None:
        self.estado = "fallida"

    def esta_pendiente(self) -> bool:
        return self.estado == "pendiente"

    def esta_terminada(self) -> bool:
        return self.estado == "terminada"

    def esta_fallida(self) -> bool:
        return self.estado == "fallida"
