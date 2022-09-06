import pandas as pd
import numpy as np
import os
import time
clear = lambda: os.system('cls')


#EJERCICIO 1

# Calcula la longitud de una cadena de texto sin usar la instruccion len(cadena)

# 1)

# Cadena de texto: hola como estas?

# Nombre de la variable: "cadena"

# 2)

# Longitud de la cadena de texto

# 3)

# Longitud de la cadena de texto calculada con un bucle

def size_aux(data):
    i = 0
    while True:
        try:
            data[i]
            i += 1
        except:
            return i
    
def ejercicio_1():
    s = input("Introuduce un texto:\n")
    print(f"La cadena tiene {size_aux(s)} caracteres")


#EJERCICIO 2

# Crea un diccionario que tenga la nota de 3 asignaturas y

# haz un pequeño algoritmo que calcule la nota media

# CURSO         -> Nota
# ---------------------
# Python        ->  10
# Big Data      ->  8
# NLP           ->  6

# 1) Muestra el valor de las claves

# 2) Muestra el valor de los valores del diccionario

# 3) Apendiza en el diccionario un nuevo elemento:

# Machine Learning --> 9

# 4) Haciendo uso un bucle muestra la clave y el valor del diccionario, cuyo resultado final sean listas anidadas.

# 5) Reconvierte el diccionario para transformarlo en un dataframe y busca la asignatura con la nota más alta

# 6) ¿y la nota más baja?

# 7) Ordena el dataframe en orden descendente: 

# Extra Calcula la media de notas usando el diccionario

def ejercicio_2():
    dic_scores = {"Python":10,"Big Data":8,"NLP":6}

    #1)
    print("1)\nClaves del diccionario:")
    for key in dic_scores.keys():
        print(key)
    print()

    #2)
    print("2)\nValores del diccionario:")
    for value in dic_scores.values():
        print(value)
    print()

    #3)
    dic_scores["Machine Learning"] = 9
    print(f"3)\nDiccionario con elemento apendizado:\n{dic_scores}\n")

    #4)
    dlist=[]
    for key,values in dic_scores.items():
        dlist.append([key,values])
    print(f"4)\nListas anidadas:\n{dlist}\n")

    #5)
    df_score = pd.DataFrame(dlist, columns=["Asignatura","Nota"])
    print(f"5)\nData Frame:\n{df_score}\n")

    print(f"La nota más alta és:")
    print(df_score.loc[df_score.Nota==max(df_score.Nota)])

    #6)
    print(f"\n6)\nLa nota más baja és:")
    print(df_score.loc[df_score.Nota==min(df_score.Nota)])

    #7)
    df_score = df_score.sort_values(by="Nota",ascending=False)
    print(f"\n7)\nData Frame ordenado:\n{df_score}\n")
    
    #8)
    sum = 0
    for value in dic_scores.values():
        sum += value
    
    print(f"8)\nLa media de notas és {sum/len(dic_scores)}")


# EJERCICIO 3

"""
Dadas 2 funciones:
Determina cual de ellas ejecuta mas rápido.
Si sabes, hazlo de 2 formas.
función a
def main(): for i in range(10**8): pass
main()
función b
def main(): for i in np.arange(10**8): pass
main()
"""

def func1(): 
    for i in range(10**8): pass

def func2():
    for i in np.arange(10**8): pass

def ejercicio_3():
    print("Calculando tiempo función 1...")
    start_time = time.time()
    func1()
    print(f"La función 1 ha tardado {time.time()- start_time}segundos")
    print("Calculando tiempo función 2...")
    start_time = time.time()
    func2()
    print(f"La función 2 ha tardado {time.time()- start_time}segundos")


# EJERCICIO 4

# Dada:

# Una matriz tal que así:

# A = np.array([[1,2,3], [4,5,6], [7,8,9]])

# se pide:

# 1) Escribe ese código en Python

# 2) Escribe la matriz transpuesta.

    # Nota, puedes usar numpy, si quieres. Si sabes más de una forma puedes usar varias.

# 3) Se pide que hagas lo mismo, pero con un bucle.

def transponer_matriz(a):
    b = np.zeros((len(a[0]),(len(a))),dtype=int)

    ## i = posición de la fila
    for i in range(len(a)):
        ## j = posición de la columna
        for j in range(len(a[0])):
            b[j,i] = a[i,j]
        
    return(b)

def ejercicio_4():
    a = np.array([
        [1,2,3], 
        [4,5,6], 
        [7,8,9]
    ])

    print(a)
    print()
    print(a.T)

    print(f"\nMatriz transpuesta con función:\n{transponer_matriz(a)}")

#MENU Y MAIN

def pintar_menu():
    print("Opcion 1: Calcular longitud")
    print("Opcion 2: Diccionario y data frame")
    print("Opcion 3: Tiempo ejecución")
    print("Opcion 4: Matriz transpuesta")
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