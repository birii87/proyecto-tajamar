from log_decorador import log


def test_log_crea_fichero():
    @log
    def saludar():
        return "hola"

    saludar()

    with open("historial.log") as fichero:
        contenido = fichero.read()

    assert "saludar" in contenido
