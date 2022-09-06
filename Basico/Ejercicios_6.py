import os
clear = lambda: os.system('cls')
import pandas as pd
import matplotlib.pyplot as plt

# EJERCICIO 1

# Mínimo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo

# 2) Prueba con min(listado)

# 3) Realiza lo mismo pero con bucles y condicionales
def list_min(list):
    min = list[0]
    for i in range(1,len(list)):
        if min > list[i]: min = list[i]
    
    return min

def ejercicio_1():
    list = [30, 20, 10, 50, 40]
    print(list)
    print(f"Minimo = {list_min(list)}")

# EJERCICIO 2

# Máximo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo

# 2) Prueba con max(listado)

# 3) Realiza lo mismo pero con bucles y condicionales

def list_max(list):
    max = list[0]
    for i in range(1,len(list)):
        if max < list[i]: max = list[i]

    return max


def ejercicio_2():
    list = [30, 20, 10, 50, 40]
    print(list)
    print(f"Máximo = {list_max(list)}")

# EJERCICIO 3

# Ordena de menor a mayor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# Pista: si quieres almacena esos números en una lista de nombre: "listado_ascendente"

# 1) Escribe el listado e ímprimelo

# 2) Prueba a usar sort()

# 3) Realiza lo mismo pero con bucles y condicionales

def sort_list_asc(list):
    sorted_list=[]
    for i in range(len(list)):
        pos_min = 0
        for j in range(1,len(list)):
            if list[pos_min] > list[j]: pos_min = j
        sorted_list.append(list[pos_min])
        del list[pos_min]
    
    return sorted_list

def ejercicio_3():
    list = [30,20,10,50,40]
    print(list)
    print("Orden ascendente")
    list = sort_list_asc(list)
    print(list)

# EJERCICIO 4

# Ordena de mayor a menor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# 1) Escribe el listado e ímprimelo

# 2) Prueba a usar sort()

# 3) Realiza lo mismo pero con bucles y condicionales


def sort_list_desc(list):
    sorted_list=[]
    for i in range(len(list)):
        pos_max = 0
        for j in range(1,len(list)):
            if list[pos_max] < list[j]: pos_max = j
        sorted_list.append(list[pos_max])
        del list[pos_max]
    
    return sorted_list

def ejercicio_4():
    list = [30,20,10,50,40]
    print(list)
    print("Orden descendente")
    list = sort_list_desc(list)
    print(list)

# EJERCICIO 5

# Escribe el código necesario en Python para:

# almacenar con una lista de nombre "modulos" los siguientes materias de un programa de Ciencia de datos:

# Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP.

# 1) Imprime el listado y imprime los valores de uno en uno

# 2) Dentro de ese grupo de materias, existen unas materias que son básicas en todos los programas, y que forman la base de conocimientos inciales para afrontar con éxito el resto de un programa.

# Las mismas son: Python y Algoritmos (aunque en la práctica hay más cosas).

# Se pide almacenar las mismas en un listado secundario, de nombre: "esenciales"

# Imprime ese listado al terminar de almacenarlos

# 3) Crea un Dataframe, de nombre "df" con esa infromación en base a la siguiente relación de módulos y horas de clase.

# módulo: Big Data, Python, Algoritmos, Machine Learning, deep Learning, NLP

# horas: 25, 15, 5, 15, 5, 10

# 4) De ese dataframe, selecciona la columna "horas" e imprimelas

# 5) Muestra el gráfico (plot) para la columna "horas"

# 6) Selecciona solamente las materias aquellas que tienen 20 o más horas de dedicación

# 7) Selecciona solamente las materias aquellas que tienen menos 10 horas de dedicación

# 8) Selecciona solamente las materias (si es posible) aquellas que tienen mas de 26 horas de dedicación

# 9) Apendiza una nueva columna llamada "docente" con el nombre del instructor de la materia. Y cuyos nombres serán: 
# Erique, Susana, Juan, Ana, Laura, Patricia, Pedro

def mas_horas(df,horas):
    df_aux = df[df["Horas"] >= horas]

    if df_aux.size != 0: print(df_aux[["Modulos"]])
    else: print("No hay registros")
    print("")

def ejercicio_5():
    #1)
    modulos = ["Big Data", "Python", "Algoritmos", "Machine Learning", "Deep Learning", "NLP"]
    print(f"1)\nLista modulos:\n{modulos}\n")

    #2)
    esenciales = ["Python","Algoritmos"]
    print(f"2)\nLista esenciales:\n{esenciales}\n")

    #3)
    horas = [25, 15, 5, 15, 5, 10]
    df = pd.DataFrame({"Modulos":modulos,"Horas":horas})
    print(f"2)\nData frame:\n{df}\n")

    #4)
    print(f"4)\nColumna Horas:\n{df.Horas}\n")

    #5)

    figure = df.Horas.plot(kind="bar")
    plt.show()

    #6)
    horas = 20
    print(f"6)\nModulos con más de {horas} horas:\n")
    mas_horas(df,horas)

    #7)
    horas = 10
    print(f"7)\nModulos con más de {horas} horas:\n")
    mas_horas(df,horas)

    #8)
    horas = 26
    print(f"8)\nModulos con más de {horas} horas:\n")
    mas_horas(df,horas)

    #9)
    instructores = ["Erique", "Susana", "Juan", "Ana", "Laura", "Patricia"]
    df["Docentes"] = instructores
    print(f"9)\nColumna apendizada:\n{df}\n")


#MENU Y MAIN

def pintar_menu():
    print("Opcion 1: Mínimo lista")
    print("Opcion 2: Máximo Lista")
    print("Opcion 3: Orden ascendente")
    print("Opcion 4: Orden descendente")
    print("Opcion 5: Data frame")
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

        elif option == "5":
            ejercicio_5()
            input("Continuar...")

        elif option == "-1":
            print("Gracias por usar este menú")
            break

        else:
            print("La opción introducida no es valida")
            input("Vuelve a intentarlo")


if __name__ == "__main__":
    main()