from evaluador.grafo.arista import Arista

class Transicion(Arista):
    def __init__(self, valor, simbolo, tope, agregar,destino):
        super().__init__(valor, destino)
        self.simbolo = simbolo
        self.tope = tope 
        self.agregar = agregar
        self.dict = {}
        self.dict['transicion'] = self.__str__()
        self.dict['destino'] = self.destino.getValor()

    def __str__(self):
        return self.simbolo+","+self.tope+"/"+str(self.agregar)