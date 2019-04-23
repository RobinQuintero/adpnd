from automata.automata import Automata, Estado

automata = Automata()
automata.addEstado("q1")
automata.addEstado("q2")
automata.conectar("a", "q1", "q2")
print(automata.buscar("q1").getTransiciones()[0].destino.getValor())
print("Este es el main")
print("git funcionando!!")