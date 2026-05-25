from gasto import crear_gasto, formatear_gastos

def test_crear_gasto():
    gasto = crear_gasto("Pistachos", 3.49)

    assert gasto["nombre"] == "Pistachos"
    assert gasto["precio"] == 3.49


def test_formato():
    gastos = [
        {"nombre": "Pistachos", "precio": 3.49},
        {"nombre": "Chocolate", "precio": 1.99}
    ]

    salida = formatear_gastos(gastos)

    assert "Pistachos" in salida