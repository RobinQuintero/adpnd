from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk
import requests
import json

botones_cinta = []
label_cinta = []
cinta = []
##
raiz = Tk()
palabra =""
def validar():
    global botones_cinta
    global cinta
    global label_cinta
    for boton in botones_cinta:
        w.delete(boton)
    for label in label_cinta:
        w.delete(label)
    
    botones_cinta = []
    label_cinta = []
    cinta = []
    palabra = entry.get()
    req = requests.get("https://adpnd.herokuapp.com/evaluar/"+palabra)
    pasos = json.loads(req.text)['pasos']
    for c in palabra: 
        cinta.append(c)
    x0 = 60
    y0 = 20
    x1 = 80
    y1 = 40
    for m in cinta:
        btn = w.create_rectangle(x0,y0,x1,y1,fill="gray")
        label = w.create_text(x0 + 8,y0+10,text=m)
        x0 = x0 + 20
        x1 = x1 + 20
        botones_cinta.append(btn)
        label_cinta.append(label)
    for paso in pasos:
        print(paso)




##lienzo = Canvas(raiz,width=500,height=500,bg = "#1E90FF")
raiz.geometry("800x500")

##lienzo.create_text(10,10,text="Automata de pila")
entry = Entry(raiz, textvariable=palabra, width=20)
entry.pack()
button = Button(raiz, text="Validar", command=validar)
button.pack()



estados = ["p","q","r"]
w=Canvas(raiz, width=800, height=300)
w.place(x=0,y=50)  
#line = canvas.create_line(x0, y0, x1, y1, ..., xn, yn, options)
#oval = canvas.create_polygon(x0, y0, x1, y1,...xn, yn, options)
points = [230,210,230,190, 250, 200]
punto = [50,210,50,190,65,200]
x = w.create_line(20,200,50,200,arrow=LAST,width=3,activefill="magenta")
#flechax = w.create_polygon(punto,width=3)

#flechapq = w.create_polygon(points, width=3)
#create_arc(x0, y0, x1, y1, options...) 

#ovalo1
p = w.create_oval(50,150,150,250, width=2,fill='#0000FF',activefill="#6A5ACD")
texto1= w.create_text(98,198,fill="white",font="Algerian 16 bold",text="p",activefill="yellow")
arco1 = w.create_arc(60, 90, 140, 240,extent=180,width="2",style=ARC,outline="red",activeoutline="green",activewidth="3")
flecha1 = w.create_line(140,170,140,171,fill="red",activefill="green",width="2",arrow=LAST,activewidth="3")
pq = w.create_line(150,200,250,200,arrow=LAST,width=3,activefill="magenta")


#ovalo2
q = w.create_oval(250,150,350,250, width=2,fill='#0000FF',activefill="#6A5ACD")
texto2= w.create_text(300,198,fill="white",font="Algerian 16 bold",text="q",activefill="yellow")
arco2 = w.create_arc(260, 90, 340, 240,extent=180,width="2",style=ARC,outline="red",activeoutline="green",activewidth="3")
flecha2 = w.create_line(340,170,340,171,arrow=LAST,fill="red",activefill="green",width="2",activewidth="3")
qr = w.create_line(350,200,450,200,arrow=LAST,width=3,activefill="magenta")

#pila =  w.create_rectangle(600,90,625,110,fill="gray")


points = [430,210,430,190, 450, 200]

boton= ttk.Button(raiz,text="QUIT",command=quit)
boton.place(x=150,y=150,)



#flechaqr = w.create_polygon(points, width=3)
r = w.create_oval(450,150,550,250, width=2,fill='#228B22',activefill="#ADFF2F")
r2 = w.create_oval(455,155,545,245, width=2,activefill="red")
texto3= w.create_text(500,198,fill="black",font="Algerian 16 bold",text="r",activefill="magenta")

#lienzo.create_oval(10,10,100,100,fill="yellow")
#lienzo.create_rectangle(10,10,100,100,fill="red")
#lienzo.create_line(60,60,100,100,fill="yellow")
#lienzo.create_text(50,50,fill="darkblue",font="Arial 11 italic bold",text="nigga xd")
raiz.configure(bg = "#1E90FF")
##lienzo.place(x=0,y=0)  
raiz.mainloop()