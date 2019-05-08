from tkinter import *
class Transicion:
    def __init__(self, lienzo, coords, valor):
        self.valor = valor
        self.lienzo = lienzo
        self.coords = coords
        self.transicion = lienzo.create_text(coords,fill="black",text = valor)
    def activar(self):
        self.lienzo.delete(self.transicion)
        self.transicion = self.lienzo.create_text(self.coords,fill="magenta", text = self.valor)
        self.lienzo.update()
    def desactivar(self):
        self.lienzo.delete(self.transicion)
        self.transicion = self.lienzo.create_text(self.coords,fill="black", text = self.valor)
        self.lienzo.update()