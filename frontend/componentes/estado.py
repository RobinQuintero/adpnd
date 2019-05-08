from tkinter import *
class Estado:
    def __init__(self, canvas, texto, x0,x1,y0,y1):
        self.ovalo = canvas.create_oval(x0,y0,x1,y1, width=2,fill='white')
        self.texto = canvas.create_text(x0+48,x1+48,fill="black",font="Algerian 16 bold",text=texto)