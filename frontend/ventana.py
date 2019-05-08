from tkinter import *
from tkinter import ttk
import requests
import json
import time
import ast
from componentes.automata import Automata

def validar(automata, lienzo):
    for boton in automata.botones_cinta:
        lienzo.delete(boton)
    for label in automata.label_cinta:
        lienzo.delete(label)
    
    automata.botones_cinta = []
    automata.label_cinta = []
    automata.cinta = []
    palabra = entry.get()
    req = requests.get("https://adpnd.herokuapp.com/evaluar/"+palabra)
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
        if paso != pasos[-1]:
            for boton in automata.botones_pila:
                lienzo.delete(boton)
            for label in automata.label_pila:
                lienzo.delete(label)
            coordsbtn = lienzo.coords(automata.botones_cinta[paso['posCinta']])
            coordslabel = lienzo.coords(automata.label_cinta[paso['posCinta']])
            automata.botones_cinta[paso['posCinta']] = lienzo.create_rectangle(coordsbtn,fill="red")
            automata.label_cinta[paso['posCinta']] = lienzo.create_text(coordslabel,text=automata.cinta[paso['posCinta']])
        lienzo.update()
        x0 = 620
        y0 = 200
        x1 = 650
        y1 = 230
        pila = ast.literal_eval(paso['pila'])
        for elem in pila:
            lienzo.pack()
            btn = lienzo.create_rectangle(x0,y0,x1,y1,fill="gray")
            label = lienzo.create_text(x0 + 10,y0+15,text=elem)
            automata.botones_pila.append(btn)
            automata.label_pila.append(label)
            y0 = y0 - 30
            y1 = y1 - 30
            lienzo.update()
        time.sleep(1)

raiz = Tk()
palabra =""
raiz.geometry("800x500")
automata = Automata(raiz)
entry = Entry(raiz, textvariable=palabra, width=80)
entry.pack()
button = Button(raiz, text="Validar", command=lambda: validar(automata,automata.lienzo))
button.pack()
raiz.configure(bg = "#e0e0e0")
raiz.mainloop()