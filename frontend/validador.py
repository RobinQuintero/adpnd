import requests
import json
import time
import ast
class Validador:
    def validar(self, automata, palabra):
        
        lienzo = automata.lienzo
        for boton in automata.botones_cinta:
            lienzo.delete(boton)
        for label in automata.label_cinta:
            lienzo.delete(label)
        lienzo.update()
        automata.botones_cinta = []
        automata.label_cinta = []
        automata.cinta = []
        self.palabra = palabra
        req = requests.get("http://127.0.0.1:8000/evaluar/"+palabra)
        pasos = json.loads(req.text)['pasos']
        for c in palabra: 
            automata.cinta.append(c)
        x0 = 60
        y0 = 20
        x1 = 90
        y1 = 50
        for m in automata.cinta:
            btn = lienzo.create_rectangle(x0,y0,x1,y1,fill="gray")
            label = lienzo.create_text(x0 + 16,y0+20,text=m)
            x0 = x0 + 30
            x1 = x1 + 30
            automata.botones_cinta.append(btn)
            automata.label_cinta.append(label)
        for paso in pasos:
            print(paso['transicion'])
            try:
                for boton in automata.botones_pila:
                    lienzo.delete(boton)
                for label in automata.label_pila:
                    lienzo.delete(label)
                coordsbtn = lienzo.coords(automata.botones_cinta[paso['posCinta']])
                coordslabel = lienzo.coords(automata.label_cinta[paso['posCinta']])
                automata.botones_cinta[paso['posCinta']] = lienzo.create_rectangle(coordsbtn,fill="red")
                automata.label_cinta[paso['posCinta']] = lienzo.create_text(coordslabel,text=automata.cinta[paso['posCinta']])
            except:
                print("s")
            lienzo.update()
            x0 = 620
            y0 = 200
            x1 = 650
            y1 = 230
            pila = ast.literal_eval(paso['pila'])
            automata.activarEstado(paso['estadoActual'])
            for elem in pila:
                lienzo.pack()
                btn = lienzo.create_rectangle(x0,y0,x1,y1,fill="gray")
                label = lienzo.create_text(x0 + 10,y0+15,text=elem)
                automata.botones_pila.append(btn)
                automata.label_pila.append(label)
                y0 = y0 - 30
                y1 = y1 - 30
                lienzo.update()
            try:
                time.sleep(1.5)
                automata.activarTransicion(str(paso['transicion']['transicion']))
                lienzo.update()
                time.sleep(1.5)
                automata.desactivarTransicion(str(paso['transicion']['transicion']))
                automata.desactivarEstado(paso['estadoActual'])
            except:
                print("a")
        
        if json.loads(req.text)['aceptada']:
            automata.mensaje = lienzo.create_text([400, 100], fill="green", text="PALABRA ACEPTADA")
        else:
            automata.mensaje = lienzo.create_text([400, 100], fill="red", text="PALABRA RECHAZADA")
        
        