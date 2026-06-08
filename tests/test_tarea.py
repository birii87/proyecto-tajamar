from pipeline import Pipeline
from tarea import Tarea


def test_añadir_tarea() -> None:
    pipeline = Pipeline()

    tarea = Tarea(
        nombre="Desarrollar API", tiempo_estimado=3.5, prioridad=1, propietario="Manish"
    )

    pipeline.añadir_tarea(tarea)

    assert len(pipeline.tareas) == 1


def test_pipeline_empieza_vacia() -> None:
    pipeline = Pipeline()

    assert len(pipeline.tareas) == 0


def test_quitar_tarea() -> None:
    pipeline = Pipeline()

    tarea = Tarea(nombre="API", tiempo_estimado=3, prioridad=1, propietario="Manish")

    pipeline.añadir_tarea(tarea)
    pipeline.quitar_tarea(tarea)

    assert len(pipeline.tareas) == 0


def test_tiempo_estimado_total() -> None:
    pipeline = Pipeline()

    pipeline.añadir_tarea(Tarea("API", 3, 1, "Manish"))

    pipeline.añadir_tarea(Tarea("Frontend", 5, 2, "Manish"))

    assert pipeline.tiempo_estimado_total() == 8
