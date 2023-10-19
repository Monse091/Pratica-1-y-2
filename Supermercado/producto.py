
class Producto:
    def __init__(self, Nombre, Cantidad, Precio):
        self.Nombre = Nombre
        self.Cantidad = Cantidad
        self.Precio = Precio

    def __str__(self):
        return f"Producto: {self.Nombre}, Cantidad: {self.Cantidad}, Precio: {self.Precio}"

