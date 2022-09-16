from typing import Type

'''
6) Crea una clase persona. Sus atributos deben ser su nombre y su edad. Además crea un método cumpleaños, 
que aumente en 1 la edad de la persona.

7) Para la clase anterior definir el método str. Debe retornar al menos el nombre de la persona.

8) Extender la clase persona agregando un atributo saldo y un método transferencia(self, persona2, monto). 
El saldo representa el dinero que tiene la persona. 
El método transferencia hace que la Persona que llama el método le transfiera la cantidad monto al objeto persona2. 
Si no tiene el dinero suficiente no se ejecuta la acción.
'''

class Human:
    money = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    def aniversary(self):
        self.age +=1
        print(f"Muchas felicidades {self.name}.\nHas cumplido {self.age} años")

    def __str__(self):
        return f"{self.name}:{self.age}"

    def add_money(self,x:float):
        self.money += x

    def get_money(self):
        return self.money

    def transference(self,other,quantity):
        if self.money < quantity:
            print("Fondos insuficientes")
            return False

        if quantity <= 0:
            print("La cantidad no puede ser negativa")
            return False
        
        self.money -= quantity
        other.add_money(quantity)

        print(f"{self.name} le ha hecho una transferencia de {quantity}€ a {other.name} ")
        return True

    def check_money(self):
        print(f"{self.name} dispone de {self.money}€")


    
