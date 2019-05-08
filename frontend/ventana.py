from tkinter import *
from tkinter import ttk
from componentes.automata import Automata
from validador import Validador

class Ventana:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry("800x500")
        self.automata = Automata(self.raiz)
        self.entry = Entry(self.raiz,  width=80)
        self.entry.pack()
        self.validador = Validador()
        self.button = Button(self.raiz, text="Validar", command=lambda: self.validar())
        self.button.pack()
        self.raiz.configure(bg = "#e0e0e0")
        self.raiz.mainloop()

    def validar(self):
        self.automata.actualizar(self.raiz)
        self.automata.lienzo.delete(self.automata.mensaje)
        self.validador.validar(self.automata,self.entry.get())
if __name__ == "__main__":
    try:
        Ventana()
    except:
        print(" ")