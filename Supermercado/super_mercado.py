from listaEnlazada import ListaEnlazada
class Super_mercado:
    def __init__(self):
        self.productos_disponibles = ListaEnlazada()
        self.productos_retirados = ListaEnlazada()

    def agregar_producto(self, producto):
        self.productos_disponibles.agregar(producto)

    def retirar_producto(self, indice):
        producto_retirado = self.productos_disponibles.retirar(indice)
        if producto_retirado:
            self.productos_retirados.agregar(producto_retirado)
            print(f"Producto retirado: {producto_retirado.Nombre}")

    def mostrar_inventario_disponible(self):
        return self.productos_disponibles.mostrar()
    
    def mostrar_inventario_retirados(self):
        return self.productos_retirados.mostrar()