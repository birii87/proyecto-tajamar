class Usuario:
    def __init__(self, nombre, es_admin=False):
        self.nombre = nombre
        self.es_admin = es_admin

    def drop_database(self):
        print(f"{self.nombre} ha borrado la bd")


class ModoAdmin:
    def __init__(self, usuario):
        self.usuario = usuario

    def __enter__(self):
        print(f"Verificando rol del usuario {self.usuario.nombre}")

        if not self.usuario.es_admin:
            raise PermissionError("Privilegios insuficientes")

        print("Usuario autenticado correctamente como Admin")
        return self.usuario

    def __exit__(self, exc_type, exc, tb):
        print("Desconectado del modo Admin")
        return False


Pepito = Usuario("Pepito")
Juanito = Usuario("Juanito", True)

print("Prueba Pepito")
try:
    with ModoAdmin(Pepito) as usuario1:
        usuario1.drop_database()
except PermissionError as error:
    print(error)

print("Prueba Juanito")
try:
    with ModoAdmin(Juanito) as usuario2:
        usuario2.drop_database()
except PermissionError as error:
    print(error)
