from evaluador.grafo.grafo import Grafo, Nodo
from evaluador.automata.estado import Estado, Transicion
from evaluador.lib.pila import Pila

class Paso:
    def __init__(self, estadoActual, posCinta, pila):
        self.estadoActual = estadoActual
        self.posCinta = posCinta
        self.pila = pila
        self.transicion = None
    
    def setTransicion(self, transicion):
        self.transicion = transicion
    def __str__(self):
        return "estado: "+str(self.estadoActual)+"\nposición cinta: "+str(self.posCinta)+"\npila: "+str(self.pila)+"\ntransición: "+str(self.transicion)