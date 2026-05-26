from gasto import Gasto, ListaGastos

def test_crear_gasto():

    gasto = Gasto("Pistachos", 3.49)

    assert gasto.nombre == "Pistachos"
    assert gasto.precio == 3.49

def test_añadir_gasto():
    carrito = ListaGastos()

    gasto = Gasto("Pistachos", 3.49)
    carrito.crear_gasto(gasto)
    assert len(carrito.gastos) == 1

def test_formato():
    
    carrito = ListaGastos()
    carrito.crear_gasto(Gasto("Pistachos", 3.49)),
    carrito.crear_gasto(Gasto("Chocolate", 1.99))

    salida = carrito.formatear_gasto()

    assert "Pistachos" in salida