from grafo.nodo import Nodo, Arista
class Estado(Nodo):
    
    def __init__(self, valor, final):
        super().__init__(valor)
        self.__valor = self._Nodo__valor
        self.__transiciones = self._Nodo__aristas
        self.addTransicion = self.addArista
        self.__final = final
        self.__palabra = []
        
    
    def addArista(self, valor, destino):
        self._Nodo__aristas.append(Arista(valor, destino))
    
    def getValor(self):
        return self.__valor
    
    def getTransiciones(self):
        return self.__transiciones
    
    def esFinal(self):
        return self.__final