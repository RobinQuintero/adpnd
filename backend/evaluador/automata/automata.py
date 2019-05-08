#Clase autómata
from evaluador.automata.paso import *
class Automata(Grafo):
    def __init__(self):
        super().__init__()
        self.__estados = self._Grafo__nodos
        self.addEstado = self.addNodo
        self.__palabra = []
        self.pila = Pila()
        self.pila.incluir("#")

    def addNodo(self, valor, final):
        self._Grafo__nodos.append(Estado(valor, final))

    def buscar(self, valor):
        for estado in self.__estados:
            if estado.getValor() == valor:
                return estado

    def getEstados(self):
        return self.__estados

    def conectar(self, simbolo, tope, agregar,  valorOrigen, valorDestino):
        origen = self.buscar(valorOrigen)
        destino = self.buscar(valorDestino)
        if origen is not None and destino is not None:
            origen.addArista(None, simbolo, tope, agregar, destino)
        else:
            raise Exception("Alguno de los nodos no existe")

    def llenarpila(self, elementos):
        for elem in elementos:
            if elem == "*":
                pass
            else:
                self.pila.incluir(elem)

    def __Evaluar(self, estado, pospalabra, pasos):
        if estado.esFinal() == True:
            paso = Paso(estado, pospalabra, self.pila)
            pasos.append(paso.__dict__)
        else:
            paso = Paso(estado, pospalabra, self.pila)
            transicion = estado.buscarTransicion(self.__palabra[pospalabra], self.pila.inspeccionar())
            if transicion is not None:
                paso.setTransicion(transicion.dict)
                self.pila.extraer()
                self.llenarpila(transicion.agregar)
                pasos.append(paso.__dict__)
                return self.__Evaluar(transicion.destino, pospalabra+1, pasos)
            pasos.append(paso.__dict__)
        return pasos

    def Evaluar(self, palabra):
        pasos = []
        for letra in palabra:
            self.__palabra.append(letra)
        self.__palabra.append("*")
        return self.__Evaluar(self.__estados[0], 0, pasos)
