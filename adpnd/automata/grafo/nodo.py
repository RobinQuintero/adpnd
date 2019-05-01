from grafo.arista import Arista

class Nodo:
    def __init__(self, valor):
        self.__aristas = []
        self.__valor = valor

    def addArista(self, valor, destino):
        self.aristas.append(Arista(valor, destino))
    def getValor(self):
        return self.__valor
    def getAristas(self):
        return self.__aristas
        