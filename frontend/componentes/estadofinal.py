from tkinter import *
from componentes.estado import Estado
class EstadoFinal(Estado):
    def __init__(self, lienzo, texto, coords):
        super().__init__(lienzo, texto, coords)
        self.inner = lienzo.create_oval(coords[0]+5,coords[1]+5,coords[2]-5,coords[3]-5, width=2, outline="black")
    
    def activar(self):
        self.ovalo = self.canvas.create_oval(self.coords, width=2, outline="green")
        self.inner = self.canvas.create_oval(self.coords[0]+5,self.coords[1]+5,self.coords[2]-5,self.coords[3]-5, width=2, outline="green")
    def desactivar(self):
        self.ovalo = self.canvas.create_oval(self.coords, width=2, outline="black")
        self.inner = self.canvas.create_oval(self.coords[0]+5,self.coords[1]+5,self.coords[2]-5,self.coords[3]-5, width=2, outline="black")