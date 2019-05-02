from evaluador.grafo.arista import Arista

class Transicion(Arista):
    def __init__(self, valor, simbolo, tope, agregar,destino):
        super().__init__(valor, destino)
        self.simbolo = simbolo
        self.tope = tope 
        self.agregar = agregar

    def __str__(self):
        return "'"+self.simbolo+","+self.tope+"/"+str(self.agregar)+"' -> ["+self.destino.getValor()+"]"