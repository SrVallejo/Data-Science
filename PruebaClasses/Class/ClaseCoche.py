'''
Clase coche prueba
'''

class Coche:

    tires = 4
    brand = " "
    model = " "
    color = " "

    def __init__(self,brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def imprimir(self):

        print("Prueba coche")
