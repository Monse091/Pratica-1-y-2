from nodo import Nodo
class ListaEnlazada:
    def __init__(self):
        self.PrimerN = None

    def agregar_elemento(self, numero):
        nuevo_nodo = Nodo(numero)
        if self.PrimerN is None:
            self.PrimerN = nuevo_nodo
        else:
            actual = self.PrimerN
            while actual.siguiente_nodo:
                actual = actual.siguiente_nodo
            actual.siguiente_nodo = nuevo_nodo

    def get_lista(self):
        actual = self.PrimerN
        lista = []
        while actual:
            lista.append(actual.numero)
            actual = actual.siguiente_nodo
        return lista
