from tabulate import tabulate

lista = [
    ["Pistachos", 3.49],
    ["Chocolate Blanco", 1.99],
    ["Arandanos", 3.30]
]

headers = ["Nombre", "Precio"]

print (tabulate(lista, headers=headers))