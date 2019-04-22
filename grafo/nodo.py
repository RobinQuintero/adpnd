from grafo.arista import Arista

class Nodo:
    def __init__(self, valor):
        self.__aristas = []
        self.__valor = valor

    def addArista(self, valor, destino):
        self.aristas.append(Arista(valor, destino))
    
    def getAristas():
        return self.__aristas
    def getValor():
        return self.__valor
        