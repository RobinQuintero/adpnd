from tkinter import *
class Estado:
    def __init__(self, canvas, texto, coords):
        self.valor = texto
        self.coords = coords
        self.canvas = canvas
        self.ovalo = canvas.create_oval(coords, width=2,fill='white')
        self.texto = canvas.create_text(coords[0]+48,coords[2]+48,fill="black",font="Algerian 16 bold",text=texto)
    def activar(self):
        self.ovalo = self.canvas.create_oval(self.coords, width=2, outline="green")
    def desactivar(self):
        self.ovalo = self.canvas.create_oval(self.coords, width=2, outline="black")