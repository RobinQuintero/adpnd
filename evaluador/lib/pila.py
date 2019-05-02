class Pila:
    def __init__(self):
        self.__items = []
    def estaVacia(self):
        return self.__items == []

    def incluir(self, item):
        self.__items.append(item)

    def extraer(self):
        return self.__items.pop()

    def inspeccionar(self):
        return self.__items[len(self.__items)-1]

    def tamano(self):
        return len(self.__items)
    def __str__(self):
        return str(self.__items)
    def getItems(self):
        return self.__items
