from tkinter import *
class Arco:
    def __init__(self, lienzo, arccoords, arrowcoords):
        self.arco = lienzo.create_arc(arccoords,extent=180,width="2",style=ARC,outline="black",activewidth="3")
        self.flecha = lienzo.create_line(arrowcoords,fill="black",activefill="green",width="2",arrow=LAST,activewidth="3")