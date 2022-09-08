import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
clear = lambda: os.system('cls')

#EJERCICIO 1

'''Se pide por tanto:
-1- Leer el archivo train.csv de Titanic dataset con pandas
-2- Imprimir algunas filas de la parte de arriba y otras de la parte del final
-3- Imprimir algunos parámetros estadísticos
-4- Ver si en todas las columnas tenemos el mismo número de datos (solo verlo)
-5- Ver el número de hombres y mujeres que hay
-6- Hacer alguna gráfica con pandas relativa al número de hombres y mujeres que hay
Si quieres hacer alguna cosa más también puedes'''

def ejercicio_1():
    #1)
    df = pd.read_csv("Data Sets\\test.csv")

    #2)
    print("2) Algunas filas del data set")
    print("Primeras 5:")
    print(df.head(5))
    print("\nUltimas 5")
    print(df.tail(5))

    #3)
    print(f"\n3) Describe data frame\n{df.describe()}")
    

    #4)
    print(f"\n4)\n")
    df.info()
    print("NO TIENEN EL MISMO NÚMERO DE DATOS")

    #5)
    total_men = int(df.Sex.loc[df.Sex == "male"].value_counts())
    print(f"\n5)\nTotal hombres: {total_men}")
    total_women = int(df.Sex.loc[df.Sex == "female"].value_counts())
    print(f"Total mujeres: {total_women}")

    #6)
    print("\n6) Gráfica pasajeros por sexo")
    figure = df.Sex.value_counts().plot(kind="bar")
    plt.show()


#EJERCICIO 2

'''Dadas estas matrices:

    m1 = [[1, 10, 20], [30, 40, 50]]
    m2 = [[60, 80, 90,]]
    m3 = [[-2, 3, 5], [8, 6, 2]]

    1) Comprueba si todos los valores de las matrices son mayores de 0
    2) Si en la matriz m2 se encuentra el valor 80
    3) Selecciona de m1 las dos últimas columnas
    4) Concatena la m1 con m2, cuyo nombre de la matriz resultante sea m4
    5) Convierte m1 y m3 en "np.matrix" asignando el nombre de matriz_1 y matriz_3, respectivamente
    6) Realiza la resta, suma y producto de la matriz_1 y matriz_3
    7) Realiza las traza de la matriz de m4
'''

def matrix_is_positive(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]<0: return False

    return True

def m_find_value(m,num):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==num: return True

    return False
def print_matrix_positive(m,name):
    if matrix_is_positive(m): print(f"La matriz '{name}' solo tiene valores positivos")
    else: print(f"La matriz{name} tiene valores negativos")


def ejercicio_2():
    m1 = [
        [1, 10, 20], 
        [30, 40, 50]
    ]

    m2 = [
        [60, 80, 90]
    ]

    m3 = [
        [-2, 3, 5], 
        [8, 6, 2]
    ]

    #1)
    print("1) Valores negativos:")
    print_matrix_positive(m1,"m1")
    print_matrix_positive(m2,"m2")
    print_matrix_positive(m3,"m3")

    #2)
    print("\n2) Encontrar valor:")
    if m_find_value(m2,80): print("En la matriz m2 se encuentra el valor 80")
    else: print("En la matriz m2 NO se encuentra el valor 80")

    #3)
    print("\n3) Ultimas dos columnas de m1:")
    for i in range(len(m1)):
        print("[",end="")
        for j in range(-2,0,1):
            try:
                print(m1[i][j],end="")
                if j!= -1: print(", ",end="")
            except:
                print("Error: Menos de dos columnas")
                break
        print("]")

    #4)
    m4= m1+m2
    print(f"\n4) Concatenación de matrices:\nm1+m2=m4\n{m4}")

    #5)
    matriz1 = np.matrix(m1)
    matriz3 = np.matrix(m3)
    print(f"\n5) Matrices Numpy:\nMatriz 1\n{matriz1}\n\nMatriz 3\n{matriz3}")

    #6)
    print(f"\n6) Operaciones:\nMatriz 1 + Matriz 3 \n{matriz1+matriz3}")
    print(f"\nMatriz 1 - Matriz 3 \n{matriz1-matriz3}")
    print(f"\nMatriz 1 x Matriz 3 \n{matriz1*matriz3.T}")


#EJERCICIO 3

'''
1) Pide por teclado un número y di si es o no primo

2) Escribe los números primos menores de 30

3) Numeros Primos: Crear un listado de los numeros primos menores de 200

4) Números Primos: Haz un listado de números primos entre 50 y 100

5) Numeros Primos: Haz un listado de los 10 primeros números primos
'''

def is_prime(num,i):
    if i <= 1: return True
    
    if num%i == 0: return False
    else: return is_prime(num,i-1)

def primes_list(start = 1, end = 1):
    primes = []
    for i in range(start,end+1):
        if is_prime(i,i-1): primes.append(i)
    return primes


def primes_list_count(total):
    count = 0
    num = 1
    primes=[]

    while count < total:
        if is_prime(num,num-1):
            primes.append(num)
            count +=1
        num +=1
    
    return primes

def ejercicio_3():

    #1)
    num = int(input("1) Introduce un número: "))
    if is_prime(num,num-1): print(f"{num} es un número primo")
    else: print(f"{num} NO es un número primo")

    #2)
    print(f"\n2) Listado primos menores de 30:\n{primes_list(start=1,end=30)}")
    #3)
    print(f"\n3) Listado primos menores de 200:\n{primes_list(start=1,end=200)}")
    #4)
    print(f"\n4) Listado primos entre 50 y 100:\n{primes_list(start=50,end=100)}")
    #5)
    print(f"\n5) Listado primeros 10 primos:\n{primes_list_count(10)}")


#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Titanic data frame")
    print("Opcion 2: Operaciones con matrices")
    print("Opcion 3: Números primos")
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


        elif option == "-1":
            print("Gracias por usar este menú")
            break

        else:
            print("La opción introducida no es valida")
            input("Vuelve a intentarlo")


if __name__ == "__main__":
    main()
