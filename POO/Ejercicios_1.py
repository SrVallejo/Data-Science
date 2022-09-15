from MenuClass import menu
from ClassessExercise1 import *


#EJERCICIO 1

'''
1) Crea el siguiente programa:

    Una clase de nombre Librería
    Inicia los siguientes atributos: nombre, sección, editorial y año
    Crea una segunda clase con nombre Rosalia que herede la clase librería.
    En esta clase Rosalia, crea una función "result" cuyo resultado sea los datos de los libros.
    declara los Objetos siguientes:
        libro1 --> Oceanarium, Ciencia, Impedimenta, 2021
        libro2 --> 33 Botones, Novela negra, Atlantis, 2022
        libro3 --> Venganza en Compostela, Historia, Universo de letras, 2022

'''

def ejercicio_1():
    libro1 = Rosalia("Oceanarium", "Ciencia", "Impedimenta", 2021)
    libro2 = Rosalia("33 Botones", "Novela negra", "Atlantis", 2022)
    libro3 = Rosalia("Venganza en Compostela", "Historia", "Universo de letras", 2022)

    libro1.print()
    libro2.print()
    libro3.print()

#EJERCICIO 2

'''
Crea otra libraría de nombre MiLibro, que corresponde a una nueva clase, define una función de nombre misLibros, cuyo resultado sea los datos de los libros:

    libro4 --> Mi primera Novela, Novela, Bruño, 2019
    libro5 --> Gatos, Literatura, Listado, 2018

    Realiza la media de los años de los libros 4 y 5
'''

def ejercicio_2():
    mis_libros = []
    mis_libros.append(Rosalia("Oceanarium", "Ciencia", "Impedimenta", 2021))
    mis_libros.append(Rosalia("33 Botones", "Novela negra", "Atlantis", 2022))
    mis_libros.append(Rosalia("Venganza en Compostela", "Historia", "Universo de letras", 2022))
    mis_libros.append(Rosalia("Mi primera Novela","Novela","Bruño",2019))
    mis_libros.append(Rosalia("Gatos","Literatura","Listado",2018))

    sum = 0
    for libro in mis_libros:
        sum += libro.get_year()
    
    mean = sum//len(mis_libros)
    print(f"Los libros se publicaron de media el año {mean}")

#EJERCICIO 3

'''
3) Crea una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

    Un constructor, donde los datos pueden estar vacíos.
    mostrar(): Muestra los datos de la persona.
    esMayorDeEdad(): Devuelve un valor indicando si es mayor de edad.


'''

def ejercicio_3():
    print("Inicializando a Pablo")
    pablo = Persona("Pablo Franco",29,"34561234P")
    pablo.print()
    if pablo.is_legal_of_age(): print("Es mayor de edad")
    else: print("No es mayor de edad")

    print()
    print("Inicializando a Josefina")
    josefa = Persona("Josefina Dedal",10, "34456789J")
    josefa.print()
    if josefa.is_legal_of_age(): print("Es mayor de edad")
    else: print("No es mayor de edad")


#EJERCICIO 4
'''
4) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

    Un constructor, donde los datos pueden estar vacíos.
    El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    mostrar(): Muestra los datos de la cuenta.
    ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos si es saldo negativo.
'''

def ejercicio_4():
    cuenta = Cuenta("Luis", 1000)
    cuenta.print()
    cuenta.ingresar(200)
    cuenta.ingresar(-30)
    cuenta.retirar(1000)
    cuenta.retirar(1000)
    cuenta.print()




def ejercicio_5():
    cuenta_joven = CuentaJoven("Anastasia",19,3000)
    cuenta_joven.ingresar(3000)
    cuenta_joven.retirar(100)
    cuenta_joven.print()

    cuenta_joven = CuentaJoven("Penelope",49,2450)
    cuenta_joven.ingresar(3000)
    cuenta_joven.retirar(100)
    cuenta_joven.print()




#MENU


def main():
    funciones =[
        ejercicio_1,ejercicio_2,ejercicio_3,
        ejercicio_4,ejercicio_5
    ]

    opciones = [
        "Clase Libros", "Media años libros", "Clase Personas",
        "Clase Cuenta Bancaria","Clase Cuenta Joven"
    ]

    my_menu = menu(funciones,opciones)

    while True:
        function = my_menu.select_menu()
        if function == -1: break
        else: function()
        input("Continue...")
    input("Thanks for using this menu")

if __name__ == "__main__":
    main()