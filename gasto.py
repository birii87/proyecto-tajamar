from tabulate import tabulate

class Gasto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class ListaGastos:
    
    def __init__(self):
        self.gastos = []

    def crear_gasto(self,gasto):
        self.gastos.append(gasto)

    def formatear_gasto(self):

        tabla = []

        for gasto in self.gastos:
            tabla.append([
                gasto.nombre,
                gasto.precio
            ])

        return tabulate(
            tabla,
            headers=["Nombre","Precio"]
        )