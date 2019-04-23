#Clase autómata
from grafo.grafo import Grafo, Nodo
from automata.estado import Estado
class Automata(Grafo):
    def __init__(self):
        super().__init__()
        self.__estados = self._Grafo__nodos
        self.addEstado = self.addNodo
    def addNodo(self, valor):
        self._Grafo__nodos.append(Estado(valor))
    def buscar(self, valor):
        for estado in self.__estados:
            if estado.getValor() == valor:
                return estado
    def getEstados(self):
        return self.estados
        
