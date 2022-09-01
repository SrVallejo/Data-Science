import os
clear = lambda: os.system('cls')
import pandas as pd

# EJERCICIO 1

"""
   Dado el siguiente listado: ["Python", "Matlab", "R", "VBA", "Julia", "C++"].
    Modifica con un algoritmo ese listado.
    Cuando encuentre Python debe poner un 1
    y cuando encuentre otro lenguaje de programacion, un 0
    es un simple ejemplo de modificación de valores en una lista.
"""
def ejercicio_1():
    lenguages = ["Python", "Matlab", "R", "VBA", "Julia", "C++"]
    print(lenguages)

    for i in range (len(lenguages)):
        if lenguages[i] == "Python": lenguages[i]= 1
        else: lenguages[i] = 0


    print(lenguages)

# EJERCICIO 2

"""
    Dada la siguiente lista:
    L = [10, None, 8, 5, None, 20]
"""
    # 1) Susitituir por -1 el valor None usando bucles y listas
    # 2) Creamos un dataframe con los valores de la lista y
    #     modificamos los "NaN" por un valor de -1 (Valores nulos, suma, etc..)
    # 3) Vuelve a escribir el listado con falta de valores (inicial),
    #     y sustituye por la media.
    # 4) Apendiza la columna con estos valores
    #     listado2 = [10, 20, 50, 30, 20, 0]
    # 5) Elimina la columna L

def lista_quitar_none(L):
    for i in range(len(L)):
        if L[i]== None: L[i]=-1
    print(L)

def ejercicio_2():

    L = [10, None, 8, 5, None, 20]
    print("Lista sin none")
    lista_quitar_none(L)


    L = [10, None, 8, 5, None, 20]
    df = pd.DataFrame({"Valores":L})
    print("\nData Frame inicial")
    print (df)
    print("\nData Frame sin none")
    print(df.fillna(-1))


    df["Valores"] = df["Valores"].fillna(df["Valores"].mean())
    print("\nData Frame con media")
    print(df)


    listado2 = [10, 20, 50, 30, 20, 0]
    df["V2"] = listado2
    print("\nData Frame con nueva columna")
    print(df)

    df = df.drop(columns=['Valores'])
    print("\nData Frame drop")
    print(df)




# EJERCICIO 3

"""
    Crear un listado con los siguientes numeros:
        10, 20, 30, 40 (nombra la lista con nombre: "listado")
"""
    # 1) Crea el listado e imprimelo:
    # 2) Apendiza el valor 50 ( si es posible)
    # 3) Modifica (si es posible) el valor 10 por 100

def ejercicio_3():

    listado = [10,20,30,40]
    print("Lista original")
    print(listado)

    listado.append(50)
    print("\nNuevo elemento apendizado")
    print(listado)

    for i in range(len(listado)):
        if listado[i] == 10: listado[i] = 100

    print("\n Número 10 modificado")
    print(listado)

# EJERCICIO 4

"""
    Da una lista de nombre "Temperatura" con valores: 10, 20, 30, 40, 50
"""
    # 1) Crea el listado e imprimelo:
    # 2) En este "Temperatura". ¿Cuál es el elemento en la posición (index) 1?
    # 3) ¿Y en la posición (index) 0?
    # 4) ¿Y en la posición (index) -1?

def imprimir_indice(indice, lista):
    print(f"El elemento en el indice {indice} es: {lista[indice]}")

def ejercicio_4():
    temperatura = [10, 20, 30, 40, 50]
    print("Lista de temperaturas:")
    print(temperatura)
    print()

    imprimir_indice(1,temperatura)
    imprimir_indice(0,temperatura)
    imprimir_indice(-1,temperatura)


#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Lista lenguajes")
    print("Opcion 2: Lista y dataframe con None")
    print("Opcion 3: Apendizar y modificar lista")
    print("Opcion 4: Imprimir temperatura por indice")
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