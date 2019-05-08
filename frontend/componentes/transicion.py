from tkinter import *
class Transicion:
    def __init__(self, lienzo, coords):
        lienzo.create_line(coords,arrow=LAST,width=3,activefill="magenta")