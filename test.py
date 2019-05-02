from automata.au import Evaluador

evaluador = Evaluador()
eval = evaluador.evaluar("abbacabba")
if eval != False:
    print("La palabra se ha validado")
    for paso in eval:
        print("\n\n"+str(paso))
else:
    print("La palabra no se ha validado")
    for paso in eval:
        print("\n\n"+str(paso))