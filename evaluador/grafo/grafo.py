from evaluador.grafo.nodo import Nodo

class Grafo():
    def __init__(self):
        self.__nodos = []
    def addNodo(self, valor):
        self.__nodos.append(Nodo(valor))
    def buscar(self, valor):
        for nodo in self.__nodos:
            if nodo.getValor() == valor:
                return nodo

    def conectar(self, valorArista, valorOrigen, valorDestino):
        origen = self.buscar(valorOrigen)
        destino = self.buscar(valorDestino)
        if origen is not None and destino is not None:
            origen.addArista(valorArista, destino)
        else:
            raise Exception("Alguno de los nodos no existe")
