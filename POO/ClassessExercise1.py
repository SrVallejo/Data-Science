class Library:
    name = ""
    genre = ""
    publisher = ""
    year = 0

    def __init__(self,name,genre,publisher,year):
        self.name = name
        self.genre = genre
        self.publisher = publisher
        self.year = year


class Rosalia(Library):

    def print(self):
        print(f"Nombre: {self.name}")
        print(f"Género: {self.genre}")
        print(f"Editorial: {self.publisher}")
        print(f"Año: {self.year}\n")
    

    def get_year(self): return self.year


    def fun(self):
        print("Tra, Tra")

class Persona:
    def __check_dni(self,dni):
        letters_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(dni) != 9:
            print("Error: Longitud DNI erronea")
            return False
        letter = dni[-1]
        number = dni.replace(letter,"")
        try:
            number = int(number)
        except:
            print("Error: No es un número")
            return False
        i = number % 23
        if letters_dni[i] == letter.upper():
            return True
        else:
            print("Error: La letra no coincide")
            return False


    name = ""
    age = 0
    dni = ""

    

    def __init__(self, name = "Jane Doe", age = 18, dni = "00000000T"):
        self.name = name
        self.age = age
        if self.__check_dni(dni): self.dni = dni
        else: self.dni = "Incorrecto"

    def print(self):
        print(f"{self.name}, con DNI {self.dni}, tiene {self.age} años")

    def is_legal_of_age(self):
        return self.age >= 18


#EJERCICIO 4
'''
4) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

    Un constructor, donde los datos pueden estar vacíos.
    El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    mostrar(): Muestra los datos de la cuenta.
    ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos si es saldo negativo.
'''

class Cuenta:

    titular = ""
    cantidad = 0

    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad

    def is_red_numbers(self):
        if self.cantidad < 0:
            print("La cuenta está en números rojos")
            return False
        return True

    def print(self):
        print(f"La cuenta bancaria de {self.titular} tiene {self.cantidad}€")
        self.is_red_numbers()
        print()
    
    def ingresar(self, x: float):
        if x < 0:
            print("Error: Número negativo")
            return False
        self.cantidad += x
        print(f"Ha ingresado {x}€.\nLa cuenta de {self.titular} dispone de {self.cantidad}€")
        self.is_red_numbers()
        print()

    def retirar(self, x: float):
        if x < 0:
            print("Error: Número negativo")
            return False
        self.cantidad -= x
        print(f"Ha retirado {x}€ de su cuenta bancaria.\nLa cuenta de {self.titular} ahora dispone de {self.cantidad}€")
        self.is_red_numbers()
        print()
    

#EJERCICIO 5

'''

5) Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:

    Un constructor.
    En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
    Además la retirada de dinero sólo se podrá hacer si el titular es válido.
    El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
    Piensa los métodos heredados de la clase madre que hay que reescribir.

'''

class CuentaJoven(Cuenta):
    age_limit = 25
    age = 0
    def __init__(self, titular,edad, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
        self.age = edad

    def __check_age(self):
        return (self.age <= self.age_limit) & (self.age >= 18)

    

    def retirar(self, x: float):

        if x < 0:
            print("Error: Número negativo")
            return False
        if not self.__check_age():
            print("Edad no validad para retirar dinero\n")
            return False

        self.cantidad -= x
        print(f"Ha retirado {x}€ de su cuenta bancaria.\nLa cuenta de {self.titular} ahora dispone de {self.cantidad}€")
        self.is_red_numbers()
        print()


    def print(self):
        print("Cuenta Joven")
        print(f"La cuenta bancaria de {self.titular} tiene {self.cantidad}€")
        self.is_red_numbers()
        print()

    

