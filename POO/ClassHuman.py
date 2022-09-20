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


    
