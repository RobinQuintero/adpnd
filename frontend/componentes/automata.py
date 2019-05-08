from tkinter import *
from componentes.arco import Arco
from componentes.estado import Estado
from componentes.transicion import Transicion
from componentes.estadofinal import EstadoFinal
class Automata:
    def __init__(self, raiz):
        self.botones_cinta = []
        self.label_cinta = []
        self.botones_pila = []
        self.label_pila = []
        self.cinta = []
        self.pila = []
        self.estados = []
        self.lienzo=Canvas(raiz, width=800, height=300, bg="#e0e0e0")
        self.lienzo.pack()
        self.inicio = Transicion(self.lienzo, [20,200,50,200])

        #Estado p
        self.p = Estado(self.lienzo, "p", [50,150,150,250])
        self.arcop = Arco(self.lienzo, [60, 90, 140, 240], [140,170,140,171])
        self.pq = Transicion(self.lienzo, [150,200,250,200])
        self.estados.append(self.p)

        #Estado q
        self.q = Estado(self.lienzo, "q", [250,150,350,250])
        self.texto2= self.lienzo.create_text(300,198,fill="black",font="Algerian 16 bold",text="q")
        self.arcoq = Arco(self.lienzo, [260, 90, 340, 240], [340,170,340,171])
        self.qr = Transicion(self.lienzo, [350,200,450,200])
        self.estados.append(self.q)

        #Estado r
        self.r = EstadoFinal(self.lienzo, "r", [450,150,550,250])
        self.texto3= self.lienzo.create_text(500,198,fill="black",font="Algerian 16 bold",text="r",activefill="magenta")
        self.estados.append(self.r)
    
    def activarEstado(self, valor):
        for estado in self.estados:
            if estado.valor == valor:
                estado.activar()
    
    def desactivarEstado(self, valor):
        for estado in self.estados:
            if estado.valor == valor:
                estado.desactivar()