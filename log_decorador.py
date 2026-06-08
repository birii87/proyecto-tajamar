from functools import wraps
from datetime import datetime

fecha = datetime.now()


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open("historial.log", "a") as fichero:
            fichero.write(f"Fecha {fecha} - Ejecutando {func.__name__}\n")
        return func(*args, **kwargs)

    return wrapper
