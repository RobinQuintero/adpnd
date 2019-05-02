from evaluador.grafo.nodo import Nodo, Arista
from evaluador.automata.transicion import Transicion
class Estado(Nodo):
    
    def __init__(self, valor, final):
        super().__init__(valor)
        self.__transiciones = self._Nodo__aristas
        self.addTransicion = self.addArista
        self.__final = final
    
    def addArista(self, valor, simbolo, tope, agregar, destino):
        self._Nodo__aristas.append(Transicion(valor, simbolo, tope, agregar, destino))
    
    def getValor(self):
        return self._Nodo__valor
    
    def getTransiciones(self):
        return self.__transiciones
    
    def esFinal(self):
        return self.__final

    def buscarTransicion(self, simbolo, tope):
        for t in self.__transiciones:
            if t.simbolo == simbolo and t.tope == tope:
                return t
        return None

    def __str__(self):
        return self._Nodo__valor