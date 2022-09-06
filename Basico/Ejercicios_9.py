
import os
clear = lambda: os.system('cls')
#EJERCICIO 1

'''

Dado este listado de números:

-3, 150, 0, 499, 500, 1200, -350, 0, 750, 25

Haz un pequeño algoritmo que haga lo siguiente:

    Si el número es negativo debe imprimir lo siguiente el valor es negativo
    Si es 0 debe imprimir un mensaje que indique: 0
    Si se encuentra entre 0 (no incluido) y 200 (si incluido), imprime 0,200
    Si se encuentra entre 200 (no incluido) y 500 (no incluido), debe imprimir (200, 500)
    Si es 500 debe continuar sin hacer nada
    Si se encuentra entre 500 (no incluido) y 1000 (no incluido) debe saltar automaticamente y dejar de testear (parar)
    Para el resto de números, debe decir: valor demasiado grande, desde 1000, en adelante

'''

def ejercicio_1():
    num_list = [
        -3, 150, 0, 
        499, 500, 1200, 
        -350, 0, 750, 
        25
    ]
    print(num_list)

    for num in num_list:
        if num < 0: print("El valor es negativo")
        elif num == 0: print("0")
        elif num <= 200: print("(0 - 200]")
        elif num <500: print ("(200 - 500)")
        elif num == 500: pass
        elif num <1000: break
        else: print("Demasiado grande")
    
#EJERCICIO 2

'''
Dada la lista de nombre "listado" y de valores: 10, 20, 20, 30, 40, 40, 40

1) Crea la lista e imprimela
2) Haz un set de esa lista
3) Trata de buscar los números NO REPETIDOS de esa lista (sin usar set)
'''

def eliminate_duplicates(data):
    new_data = []
    for value in data:
        if value not in new_data: new_data.append(value)

    return new_data

def unique_values(data):
    unique_data =[]
    for value in data:
        if data.count(value) == 1: unique_data.append(value)
    
    return unique_data

def ejercicio_2():
    num_list = [
        10, 20, 20, 
        30, 40, 40, 
        40
    ]
    print (num_list)

    print(f"Eliminar duplicados con set: {set(num_list)}")
    print(f"Eliminar duplicados con función propia: {eliminate_duplicates(num_list)}")
    print(f"Valores unicos con función propia: {unique_values(num_list)}")

#EJERCICIO 3

'''
Dados estos clientes:

    Usando el continue/break

Trata de averiguar si un cliente concreto se encuentra en la BBDD (Base de Datos)

"Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"

'''

def find_element(data,element):
    for value in data:
        if value == element: return True
    return False

def ejercicio_3():
    employees = [
        "Ana Pérez", "Juan García", "Andres Álvarez", 
        "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", 
        "Alberto Delgado", "Susana Castro", "Luis González"
    ]
    print(employees)
    name = input("¿Que empleado quieres buscar? ")
    if find_element(employees,name): print(f"La empleada {name} trabaja en la empresa")
    else: print(f"La empleada {name} NO trabaja en la empresa")


#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Condicionales lista números")
    print("Opcion 2: Valores únicos y eliminar duplicados")
    print("Opcion 3: Encontrar empleados")
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
