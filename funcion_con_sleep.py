import time


def espera_5_segundos(funcion):
    def wrapper(*args, **kwargs):
        print(f"Pausando el tiempo, tras 5 segundos ejecutaré {funcion.__name__}")
        time.sleep(5)
        resultado = funcion(*args, **kwargs)
        return resultado

    return wrapper


@espera_5_segundos
def sumar(n1, n2):
    return n1 + n2


print("Lanzamos")
sumatorio = sumar(10, 15)
print(f"Resultado de la suma es = {sumatorio}")
