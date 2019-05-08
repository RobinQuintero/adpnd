from evaluador.resultado import *



class Evaluador:
    def __init__(self):
        self.automata = Automata()
        self.automata.addEstado("p", False)
        self.automata.addEstado("q", False)
        self.automata.addEstado("r", True)
        self.automata.conectar("a","#","#a","p","p")
        self.automata.conectar("b","#","#b","p","p")
        self.automata.conectar("a","a","aa","p","p")
        self.automata.conectar("b","a","ab","p","p")
        self.automata.conectar("a","b","ba","p","p")
        self.automata.conectar("b","b","bb","p","p")
        self.automata.conectar("c","#","#","p","q")
        self.automata.conectar("c","b","b","p","q")
        self.automata.conectar("c","a","a","p","q")
        self.automata.conectar("b","b","*","q","q")
        self.automata.conectar("a","a","*","q","q")
        self.automata.conectar("*","#","#","q","r")

    def evaluar(self, palabra):
        pasos = self.automata.Evaluar(palabra)
        if pasos[-1]['estadoActual'] == "r":
            aceptada = True
        else:
            aceptada = False
        return Resultado(aceptada, pasos)


