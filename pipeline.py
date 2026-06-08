from tarea import Tarea


class Pipeline:
    def __init__(self) -> None:
        self.tareas: list[Tarea] = []

    def añadir_tarea(self, tarea: Tarea) -> None:
        self.tareas.append(tarea)

    def quitar_tarea(self, tarea: Tarea) -> None:
        self.tareas.remove(tarea)

    def tiempo_estimado_total(self) -> float:
        return sum(tarea.tiempo_estimado for tarea in self.tareas)

    def tareas_pendientes(self) -> list[Tarea]:
        return [tarea for tarea in self.tareas if tarea.estado == "pendiente"]

    def tareas_terminadas(self) -> list[Tarea]:
        return [tarea for tarea in self.tareas if tarea.estado == "terminada"]

    def tareas_fallidas(self) -> list[Tarea]:
        return [tarea for tarea in self.tareas if tarea.estado == "fallida"]
