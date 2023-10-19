from nodoProducto import NodoProducto
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, producto):
        nuevo_nodo = NodoProducto(producto)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def retirar(self, indice):
        if not self.cabeza:
            print("La lista está vacía. No se pudo retirar el producto.")
            return
        
        if indice == 0:
            producto_retirado = self.cabeza.producto
            self.cabeza = self.cabeza.siguiente
            return producto_retirado

        actual = self.cabeza
        for i in range(indice - 1):
            if not actual.siguiente:
                print("Índice inválido. No se pudo retirar el producto.")
                return
            actual = actual.siguiente

        producto_retirado = actual.siguiente.producto
        actual.siguiente = actual.siguiente.siguiente
        return producto_retirado

    def mostrar(self):
        actual = self.cabeza 
        lista= []
        while actual:
            lista.append(actual.producto)
            actual = actual.siguiente

        return lista