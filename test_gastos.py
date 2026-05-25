from gasto import crear_gasto

def test_crear_gasto():
    gasto = crear_gasto("Pistachos", 3.49)

    assert gasto["nombre"] == "Pistachos"
    assert gasto["precio"] == 3.49