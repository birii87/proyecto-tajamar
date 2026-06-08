import time


def reintentar_3_veces(funcion):
    def wrapper(*args, **kwargs):
        max_intentos = 3

        for intento in range(max_intentos):
            try:
                resultado = funcion(*args, **kwargs)
                return resultado
            except Exception as error:
                print(f"Intento {intento + 1} fallido. Por {error}")

                if intento < max_intentos - 1:
                    print("Reintentando en 2 segundos \n")
                    time.sleep(2)
                else:
                    print(
                        f"Se han agotado el número de {max_intentos} intentos máximos"
                    )

    return wrapper


class Error_de_envio(Exception):
    pass


intentos = 0


@reintentar_3_veces
def enviar_correo():
    global intentos
    intentos += 1

    print(f"Intentando enviar correo. Intento {intentos}")

    if intentos < 3:
        raise Error_de_envio("No ha sido posible entregar el correo")

    return "Correo enviado con exito"


print("Enviando Correo...")
resultado_final = enviar_correo()

if resultado_final:
    print(resultado_final)
