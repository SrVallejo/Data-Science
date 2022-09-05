import numpy as np
import os
clear = lambda: os.system('cls')

# EJERCICIO 1

# a) Declara la variable "test" como una lista con los siguientes componentes: 25, 8, 32, 20, 1.
    # Usa las formas que conozcas para crearla y el uso de type para asegurarte de que es una lista.

# b) Apendiza un valor de valor 20, 32, 25, 32

# c) Elimina el valor 8 de la lista

# d) Elimina los duplicados que haya en la lista test

# e) Crea una segunda lista de nombre "info" que contenga los valores:
    #  25, 100, 10, 20, 5, 25, 30, 200

# f) ¿Cuántos valores se repiten entre las listas?

# g) Muéstrame el maximo y mínimo en las dos listas

# h) Crea una nueva variable de nombre "matriz" transformando la lista test en matriz

# i) Crea una función que se llame "funcion_división" donde se divida
    # el test con valor 32 entre info con valor 5 y muestra el resto de la división

# j) Con ayuda de reverse() muestra la inversa de test

# k) Con el listado info utiliza un bucle for con la ayuda de enumerate(),
    # para mostrar posición y valor y crea un diccionario de nombre "newDict"

# l) Crea un nuevo listado con nombre "info2" donde los valores: 25 se sustituya por "María",
    # el valor 20 por "Juan" y el valor 10 por "Pedro"

# m) Sustituye en el listado test los multiplos de 2 por "Dos"

def funcion_división(x,y):
    return int(x/y),x%y

def ejercicio_1():
    #a)
    test = [25, 8, 32, 20, 1]
    print(f"a)\n{test}\n{type(test)}")

    #b)
    test_aux =[20, 32, 25, 32]
    for e in test_aux:
        test.append(e)
    print(f"\nb)\nValores apendizados:\n{test}")

    #c)
    test.remove(8)
    print(f"\nc)\nValor 8 eliminado:\n{test}")

    #d)
    test = set(test)
    test = list(test)
    test.sort()

    print(f"\nd)\nValores duplicados eliminados y ordenada:\n{test}")

    #e)
    info = [25, 100, 10, 20, 5, 25, 30, 200]
    print(f"\ne)\nLista info creada:\n{info}")

    #f)

    #lista donde guardare los repetidos y contador
    rep_list=[]
    count = 0

    #elimino duplicados
    info_aux = set(info)
    info_aux = list(info_aux)


    for e in info_aux:
        if e in test: 
            count +=1
            rep_list.append(e)

    print(f"\nf)Se repiten {count} valores, que son los siguientes\n{rep_list}")

    #g)
    print(f"\ng)\nTest:\nMax: {max(test)}\nMin: {min(test)}\n\nInfo:\nMax: {max(info)}\nMin: {min(info)}")

    #h)
    matriz = np.array(test)

    print("\nh)")
    print(f"Matriz: {matriz}")
    print(type(matriz))

    #i)
    x = 32
    y = 5
    div,resto=funcion_división(x,y)
    print(f"\ni)\nLa division entre {x} y {y} es igual a {div} con resto {resto}")

    #j)
    test.reverse()
    print(f"\nj)\nInversa de test:\n{test}")

    #k)

    newDict = {}
    for i,e in enumerate(info):
        newDict[i]=e
    print(f"\nk)\nDiccionario newDict:\n{newDict}")

    #l)
    info2 = []
    for e in info:
        if e == 25: e="María"
        elif e== 20: e="Juan"
        elif e== 10: e="Pedro"
        info2.append(e)
    print(f"\nl)\nInfo 2:\n{info2}")

    #m)
    for i in range(len(test)):
        if test[i]%2 == 0: test[i] = "Dos"

    print(f"\nm)\nTest:\n{test}")       

# EJERCICIO 2

"""
    Escribe un programa que imprima los números desde 1 hasta 100
    Pero:
    * Para los múltiplos de 3 escribe "Hello"
    * Para los múltiplos de 5 escribe "World"
    * Para los múltiplos de ambos (3 y 5) escribe "Hello World"
    (en vez de los números correspondientes)
"""

def ejercicio_2():
    for i in range (1,101):
        if i%3==0 and i%5==0: print("Hello World")
        elif i%3==0: print("Hello")
        elif i%5==0: print("World")
        else: print(i)


#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Ejercicios listas")
    print("Opcion 2: 1 al 100 Hello World")
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

        elif option == "-1":
            print("Gracias por usar este menú")
            break

        else:
            print("La opción introducida no es valida")
            input("Vuelve a intentarlo")


if __name__ == "__main__":
    main()
