import os
clear = lambda: os.system('cls')
import pandas as pd

# EJERCICIO 1

"""
    Dada una lista de nombre "listado" y con valores: 10,20,30,40,50
"""
# 1) Crea un pequeño programa capaz de conseguir el orden inverso de los números de "listado"
# imprime nuevamente el listado para tenerlo "a mano"
# 10-20-30-40-50 (tengo)
# 50-40-30-20-10 (lo que busco)

def reverse_list(firstlist):
    reverse = []
    for i in range(-1,0-len(firstlist)-1,-1):
        reverse.append(firstlist[i])
    return reverse

def ejercicio_1():
    listado = [10,20,30,40,50]
    print(f"Original:\n{listado}\nInverso:\n{reverse_list(listado)}")



# EJERCICIO 2

"""
    Programa que coge por teclado 5 números y los almacena en una lista
    Nota:
    debería estar en la misma celda
    Hazlo como puedas, discurre cómo sería..
"""

def ejercicio_2():
    num = 0
    limit = 5
    numlist = []
    while(num < limit):
        value = input(f"Introduce el valor Nº{num+1}: ")
        clear()
        try:
            value = int(value)
            numlist.append(value)
            num += 1
        except:
            print("Error: No es un valor numérico.")
    
    print(f"Su lista de números és:\n{numlist}")



# EJERCICIO 3

"""
    Programa que coge por teclado una frase y es capaz de decir cuántas vocales hay
    Nota: asume que son letras minúsculas sin tildes.
"""

# 1) Entrada de texto por teclado
# 2) Hazlo si puedes de varias formas
    # forma 1: contar vocales en palabra/frase
# 3) Hazlo de otra forma si se te ocurre..
    # forma 2

def count_vowels_1(text):
    text = text.lower()
    vowels = ["a","e","i","o","u"]
    text_len = len(text)
    for vowel in vowels:
        text = text.replace(vowel,"")

    return text_len - len(text)

def count_vowels_2(text):
    text = text.lower()
    vowels = ["a","e","i","o","u"]
    num_vowels = 0
    for c in text:
        if c in vowels: num_vowels +=1

    return num_vowels

def ejercicio_3():
    text = input("Introduce la frase que quiera analizar:\n")
    print(f"La frase contiene {count_vowels_2(text)} vocales")

# EJERCICIO 4

"""
    Tablas de multiplicar:
    Haz algo tal que:
"""

# 1) Pregunta al usuario que tabla quiere multiplicar: <1 al 10>

# 2) Muestra los resultados de esta forma:

"""
        2 x 1 = 2
        2 x 2 = 4
        ...
        2 x 10 = 20
"""
def multiplication_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

def ejercicio_4():
    num = int(input("Introduce número del que quieras obtener la tabla: "))
    clear()
    multiplication_table(num)


#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Lista Inversa")
    print("Opcion 2: Introducir Lista")
    print("Opcion 3: Contar Vocales")
    print("Opcion 4: Tablas de multiplicar")
    print("Opcion -1: Salir")

def main():

    while True:
        clear()
        pintar_menu()
        option = input("Elige una opción: ")
        clear()

        if option == "1":
            ejercicio_1()
            input("Continuar...")

        elif option == "2":
            ejercicio_2()
            input("Continuar...")

        elif option == "3":
            ejercicio_3()
            input("Continuar...")

        elif option == "4":
            ejercicio_4()
            input("Continuar...")

        elif option == "-1":
            print("Gracias por usar este menú")
            break

        else:
            print("La opción introducida no es valida")
            input("Vuelve a intentarlo")


if __name__ == "__main__":
    main()