from grafo.nodo import Nodo

class Grafo:
    def __init__(self):
        self.__nodos = []
    def addNodo(self, valor):
        self.__nodos.append(Nodo(valor))