import os
clear = lambda: os.system('cls')

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

ejercicio_4()

# EJERCICIO 5
"""
    Pendiente
"""

def pintar_menu():
    print("Opcion 1: Mínimo lista")
    print("Opcion 2: Máximo Lista")
    print("Opcion 3: Orden ascendente")
    print("Opcion 4: Orden descendente")
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