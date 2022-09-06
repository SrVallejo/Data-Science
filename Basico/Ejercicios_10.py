import numpy as np
import os
clear = lambda: os.system('cls')
#EJERCICIO 1

#Programa que cree la matriz identidad

def identity_matrix(n):
    i_matrix = np.zeros((n,n),dtype = int)
    
    for i in range(n):
        i_matrix[i,i]=1
    return i_matrix

def ejercicio_1():
    n = int(input("¿De cuantas filas va a ser la matriz?\n"))
    clear()
    print(f"Matriz identidad de orden {n}x{n}:\n{identity_matrix(n)}")

#EJERCICIO 2

#1) Traspuesta
#2) Tamaño
#3) Dimensiones
#4) Matriz valores menores de 0?
#5) Matriz valores algún valor mayor que 10?
#6) Linspace 5 valores
#7) La matriz contiene el valor 7?
#8) Copia matriz flatten
#9) Flatten a mano con lista
#10) Potencia de 3

def flat_matrix(matrix):
    values = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            values.append(matrix[i,j])
    return values

def power_list(list,power):
    for i in range(len(list)):
        list[i] = pow(list[i],power)
    return list

def ejercicio_2():
    matrix = np.array([
    [3,6,8],
    [20,5,7],
    [10,14,1]
    ])
    print(f"{matrix}\n")

    #1)
    print(f"1) Matriz Transpuesta:\n{matrix.T}\n")

    #2)
    print(f"2) Tamaño: {matrix.size}")

    #3)
    print(f"3) Dimensiones: {matrix.shape}")

    #4)
    if np.any(matrix < 0): print("4) Tiene valores negativos")
    else: print("4) Todos los valores son negativos")

    #5)
    if np.any(matrix > 10): print("5) Tiene valores mayores de 10")
    else: print("5) Todos los valores son menores de 10")

    #6)
    print(f"6) Linspace 5: {np.linspace(matrix.min(),matrix.max(),5)}")

    #7)
    if np.any(matrix == 7): print("7) Contiene el número 7")
    else: print("7) No contiene el número 7")

    #8)
    print(f"\n8) Matriz aplanada flatten:\n{matrix.flatten()}")

    #9)
    print(f"\n9) Matriz aplanada función propia:\n{flat_matrix(matrix)}")

    #10)
    print(f"\n10) Potencia de la matriz:\n{power_list(flat_matrix(matrix),3)}")
    

#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Matriz identidad")
    print("Opcion 2: Funciones de matrices")
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

