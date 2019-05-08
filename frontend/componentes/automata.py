from tkinter import *
class Automata:
    def __init__(self, raiz):
        self.botones_cinta = []
        self.label_cinta = []
        self.botones_pila = []
        self.label_pila = []
        self.cinta = []
        self.pila = []
        self.lienzo=Canvas(raiz, width=800, height=300, bg="#e0e0e0")
        self.lienzo.pack()
        self.points = [230,210,230,190, 250, 200]
        self.punto = [50,210,50,190,65,200]
        self.x = self.lienzo.create_line(20,200,50,200,arrow=LAST,width=3,activefill="magenta")

        #Estado p
        self.p = self.lienzo.create_oval(50,150,150,250, width=2,fill='white')
        self.texto1= self.lienzo.create_text(98,198,fill="black",font="Algerian 16 bold",text="p")
        self.arco1 = self.lienzo.create_arc(60, 90, 140, 240,extent=180,width="2",style=ARC,outline="black",activewidth="3")
        self.flecha1 = self.lienzo.create_line(140,170,140,171,fill="black",activefill="green",width="2",arrow=LAST,activewidth="3")
        self.pq = self.lienzo.create_line(150,200,250,200,arrow=LAST,width=3,activefill="magenta")


        #Estado q
        self.q = self.lienzo.create_oval(250,150,350,250, width=2,fill='white')
        self.texto2= self.lienzo.create_text(300,198,fill="black",font="Algerian 16 bold",text="q")
        self.arco2 = self.lienzo.create_arc(260, 90, 340, 240,extent=180,width="2",style=ARC,outline="black",activeoutline="green",activewidth="3")
        self.flecha2 = self.lienzo.create_line(340,170,340,171,arrow=LAST,fill="black",activefill="black",width="2",activewidth="3")
        self.qr = self.lienzo.create_line(350,200,450,200,arrow=LAST,width=3,activefill="magenta")

        self.r = self.lienzo.create_oval(450,150,550,250, width=2,fill='white')
        self.r2 = self.lienzo.create_oval(455,155,545,245, width=2)
        self.texto3= self.lienzo.create_text(500,198,fill="black",font="Algerian 16 bold",text="r",activefill="magenta")