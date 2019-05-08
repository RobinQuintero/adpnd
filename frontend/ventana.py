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
        self.button = Button(self.raiz, text="Validar", command=lambda: self.validador.validar(self.automata,self.entry.get()))
        self.button.pack()
        self.raiz.configure(bg = "#e0e0e0")
        self.raiz.mainloop()

if __name__ == "__main__":
    Ventana()