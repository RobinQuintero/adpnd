#Clase autómata
from grafo.grafo import Grafo, Nodo
from automata.estado import Estado, Transicion
from lib.pila import Pila
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
    def setPalabra(self, palabra):
        for letra in palabra:
            self.__palabra.append(letra)
    def getPalabra(self):
        return self.__palabra
    def Evaluar(self, estado):
        if estado.esFinal() == True:
            return True
        else:
            print("------------------------------------------")
            print("Estado actual: "+estado.getValor())
            print("Cinta: "+str(self.__palabra))
            print("Pila: "+str(self.pila))
            if len(self.__palabra) == 0:
                self.__palabra.append("λ")
            transicion = estado.buscarTransicion(self.__palabra[0], self.pila.inspeccionar())
            if(transicion is not None):
                self.__palabra = self.__palabra[1:]
                self.pila.extraer()
                for elem in transicion.agregar:
                    if elem == "λ":
                        pass
                    else:
                        self.pila.incluir(elem)
                print("Se utiliza la sgte transición: "+str(transicion))
                print("-----------------------------------------------")
                return self.Evaluar(transicion.destino)
        
