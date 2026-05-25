from tabulate import tabulate

def crear_gasto(nombre,precio):
    return {
        "nombre": nombre,
        "precio": precio
    }

def formatear_gastos (lista_de_gastos):
    tabla = []

    for gasto in lista_de_gastos:
        tabla.append(
            [
                gasto["nombre"],
                gasto["precio"]
             ]
        )

    return tabulate(tabla,headers=["Nombre","Precio"])