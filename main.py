from automata.automata import *

automata = Automata()
automata.addEstado("p", False)
automata.addEstado("q", False)
automata.addEstado("r", True)
automata.conectar("a","#","#a","p","p")
automata.conectar("b","#","#b","p","p")
automata.conectar("a","a","aa","p","p")
automata.conectar("b","a","ab","p","p")
automata.conectar("a","b","ba","p","p")
automata.conectar("b","b","bb","p","p")
automata.conectar("c","#","#","p","q")
automata.conectar("c","b","b","p","q")
automata.conectar("c","a","a","p","q")
automata.conectar("b","b","λ","q","q")
automata.conectar("a","a","λ","q","q")
automata.conectar("λ","#","#","q","r")

automata.setPalabra("aabbacabbaa")
eval = automata.Evaluar(automata.getEstados()[0])
if eval == True:
    print("La palabra se ha validado")