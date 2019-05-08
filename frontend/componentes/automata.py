from tkinter import *
from componentes.arco import Arco
from componentes.estado import Estado
from componentes.transicion import Transicion
from componentes.estadofinal import EstadoFinal
class Automata:
    def __init__(self, raiz):
        self.raiz = raiz
        self.botones_cinta = []
        self.label_cinta = []
        self.botones_pila = []
        self.label_pila = []
        self.cinta = []
        self.pila = []
        self.estados = []
        self.transiciones = []
        self.lienzo=Canvas(raiz, width=800, height=400, bg="#e0e0e0")
        self.lienzo.pack()
        self.inicio = self.lienzo.create_line([120,300,150,300],arrow=LAST,width=3, fill="black")
        self.transiciones.append(Transicion(self.lienzo,[130,240],"a,#/#a"))
        self.transiciones.append(Transicion(self.lienzo,[130,220],"b,#/#b"))
        self.transiciones.append(Transicion(self.lienzo,[130,200],"a,a/aa"))
        self.transiciones.append(Transicion(self.lienzo,[130,180],"b,a/ab"))
        self.transiciones.append(Transicion(self.lienzo,[130,160],"a,b/ba"))
        self.transiciones.append(Transicion(self.lienzo,[130,140],"b,b/bb"))
        self.mensaje = self.lienzo.create_text([400, 100], fill="green", text="")
        #Estado p
        self.p = Estado(self.lienzo, "p", [150,250,250,350])
        self.arcop = Arco(self.lienzo, [160, 190, 240, 340], [240,270,240,271])
        self.pq = self.lienzo.create_line([250,300,350,300],arrow=LAST,width=3, fill="black")
        self.estados.append(self.p)
        self.transiciones.append(Transicion(self.lienzo,[290,320],"c,a/a"))
        self.transiciones.append(Transicion(self.lienzo,[290,280],"c,b/b"))
        self.transiciones.append(Transicion(self.lienzo,[290,260],"c,#/#"))

        #Estado q
        self.q = Estado(self.lienzo, "q", [350,250,450,350])
        self.texto2= self.lienzo.create_text(400,298,fill="black",font="Algerian 16 bold",text="q")
        self.arcoq = Arco(self.lienzo, [360, 190, 440, 340], [440,270,440,271])
        self.qr = self.lienzo.create_line([450,300,550,300],arrow=LAST,width=3, fill="black")
        self.transiciones.append(Transicion(self.lienzo,[500,320],"*,#/#"))
        self.transiciones.append(Transicion(self.lienzo,[460,240],"a,a/*"))
        self.transiciones.append(Transicion(self.lienzo,[460,220],"b,b/*"))
 
        self.estados.append(self.q)

        #Estado r
        self.r = EstadoFinal(self.lienzo, "r", [550,250,650,350])
        self.texto3= self.lienzo.create_text(600,298,fill="black",font="Algerian 16 bold",text="r",activefill="magenta")
        self.estados.append(self.r)
    
    def activarEstado(self, valor):
        for estado in self.estados:
            if estado.valor == valor:
                estado.activar()
    
    def desactivarEstado(self, valor):
        for estado in self.estados:
            if estado.valor == valor:
                estado.desactivar()
    
    def activarTransicion(self, valor):
        for transicion in self.transiciones:
            if transicion.valor == valor:
                transicion.activar()
    def desactivarTransicion(self, valor):
        for transicion in self.transiciones:
            if transicion.valor==valor:
                transicion.desactivar()
    def actualizar(self, raiz):
        self.lienzo.delete("all")
        self.botones_cinta = []
        self.label_cinta = []
        self.botones_pila = []
        self.label_pila = []
        self.cinta = []
        self.pila = []
        self.estados = []
        self.transiciones = []
        self.inicio = self.lienzo.create_line([120,300,150,300],arrow=LAST,width=3, fill="black")
        self.transiciones.append(Transicion(self.lienzo,[130,240],"a,#/#a"))
        self.transiciones.append(Transicion(self.lienzo,[130,220],"b,#/#b"))
        self.transiciones.append(Transicion(self.lienzo,[130,200],"a,a/aa"))
        self.transiciones.append(Transicion(self.lienzo,[130,180],"b,a/ab"))
        self.transiciones.append(Transicion(self.lienzo,[130,160],"a,b/ba"))
        self.transiciones.append(Transicion(self.lienzo,[130,140],"b,b/bb"))
        self.mensaje = self.lienzo.create_text([400, 100], fill="green", text="")
        #Estado p
        self.p = Estado(self.lienzo, "p", [150,250,250,350])
        self.arcop = Arco(self.lienzo, [160, 190, 240, 340], [240,270,240,271])
        self.pq = self.lienzo.create_line([250,300,350,300],arrow=LAST,width=3, fill="black")
        self.estados.append(self.p)
        self.transiciones.append(Transicion(self.lienzo,[290,320],"c,a/a"))
        self.transiciones.append(Transicion(self.lienzo,[290,280],"c,b/b"))
        self.transiciones.append(Transicion(self.lienzo,[290,260],"c,#/#"))

        #Estado q
        self.q = Estado(self.lienzo, "q", [350,250,450,350])
        self.texto2= self.lienzo.create_text(400,298,fill="black",font="Algerian 16 bold",text="q")
        self.arcoq = Arco(self.lienzo, [360, 190, 440, 340], [440,270,440,271])
        self.qr = self.lienzo.create_line([450,300,550,300],arrow=LAST,width=3, fill="black")
        self.transiciones.append(Transicion(self.lienzo,[500,320],"*,#/#"))
        self.transiciones.append(Transicion(self.lienzo,[460,240],"a,a/*"))
        self.transiciones.append(Transicion(self.lienzo,[460,220],"b,b/*"))
 
        self.estados.append(self.q)

        #Estado r
        self.r = EstadoFinal(self.lienzo, "r", [550,250,650,350])
        self.texto3= self.lienzo.create_text(600,298,fill="black",font="Algerian 16 bold",text="r",activefill="magenta")
        self.estados.append(self.r)