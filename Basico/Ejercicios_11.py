import pandas as pd
import matplotlib.pyplot as plt
import os
clear = lambda: os.system('cls')

#EJERCICIO 1
'''

Escribe el código necesario en Python para:

    almacenar con una lista de nombre "clientes" los siguientes nombres:

"Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"

1)Para ese listado de clientes imprime todos 1 a 1

2) Dentro de ese grupo de clientes..

se pide buscar..al cliente de nombre: "Juan García" si es posible

    Si lo encuentra, debería imprimir un mensaje tal que así:

    "el cliente -nombre del cliente- se encuentra en mi Base de Datos de Clientes"

    Si no se le encuentra, debería salir un mensaje tal que así:

    "el cliente -nombre del cliente- NO se encuentra en mi Base de Datos de Clientes"

3)

Crea un DataFrame, de nombre df

con esa información en base a la siguiente relación de clientes y tarifas contratadas (€)

clientes:

Ana Pérez, Juan García, Andrés Álvarez, Luis Ramos, Pedro Cadenas, Estefanía Miguélez, Alberto Delgado, Susana Castro, Luis González

tarifas:

40,50,50,35,45,50,60,50,45

4)

Imprime las primeras 5 filas del DataFrame

de 2 formas distintas

Imprime las últimas 2 líneas del DataFrame

5)

De ese DataFrame, selecciona solamente la columna "tarifas" e imprímela 

6)

Descomenta las siguientes líneas

(algunos trucos y cosas útiles)

1

df.tarifas.value_counts()

df.tarifas.value_counts().plot(kind="bar")

df.tarifas.plot(kind="bar")

7)

De ese DataFrame, selecciona solamente aquellos clientes con tarifa superior a 50 euros

(50 no incluído)

De ese DataFrame, selecciona solamente aquellos clientes con tarifa menor o igual de 30 euros

(30 incluido)

'''

def find_element(data,element):
    for value in data:
        if value == element: return True
    return False

def ejercicio_1():
    clients = ["Ana Pérez", "Juan García", "Andres Álvarez", 
        "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", 
        "Alberto Delgado", "Susana Castro", "Luis González"
    ]

    #1)
    print("1) Lista de clientes")

    for client in clients:
        print(client)

    #2)
    print("\n2) Buscar cliente")
    name = input("Cliente a buscar: ")
    if find_element(clients,name): print(f"el cliente {name} se encuentra en mi Base de Datos de Clientes")
    else: print(f"el cliente {name} NO se encuentra en mi Base de Datos de Clientes")

    #3)
    print("\n3) Data frame")
    rates = [
        40,50,50,
        35,45,50,
        60,50,45
    ]

    df = pd.DataFrame({"Clients":clients,"Rates":rates})
    print(df)

    #4)
    print(f"\n4) Primeras 5 filas:\n{df.head(5)}")
    print(f"\n Primeras 5 filas (otro método):\n{df.loc[:4]}")
    print(f"\nUltimas 2 filas:\n{df.tail(2)}")

    #5)
    print(f"\n5) Solo columna rates:\n{df.Rates}")

    #6)
    print("\n6) Trucos y cosas útiles\nValue counts:")
    print(df.Rates.value_counts())
    figure = df.Rates.value_counts().plot(kind="bar")
    plt.show()
    figure = df.Rates.plot(kind="bar")
    plt.show()

    #7)
    print(f"\n7)Data Frame condicional:\n\nSolo rates > 50:\n{df[df.Rates > 50]}\n")
    print(f"Solo rates <= 30\n{df[df.Rates <= 30]}")


#EJERCICIO 2

'''Número par o impar

Prueba para los números 6 y 3

Realiza un algortimo para saber si son pares o impares
'''

def is_pair(num):
    return num%2 == 0

def ejercicio_2():
    x,y = 6,3

    if is_pair(x): print(f"{x} es un número par")
    else: print(f"{x} es un número impar")

    if is_pair(y): print(f"{y} es un número par")
    else: print(f"{y} es un número impar")


#EJERCICIO 3

'''Intercambio de valores entre variables

Siendo por ejemplo:

    x = 3 e y = 2

Se pide hacer un pequeño algoritmo que me intercambie esos valores.

Y que sea el resultado:

    x = 2 e y = 3

1) Hazlo sin funciones

2) Haz lo mismo con una función

'''
def change_values(x,y):
    return y,x

def ejercicio_3():
    #Sin Función
    x,y = 2,3
    print(f"Antes del cambio: x={x} y={y}")

    x = x+y
    y = x-y
    x = x-y
    print(f"Despues del cambio: x={x} y={y}")

    #Con Función
    x,y = 10,-5
    print(f"Antes del cambio: x={x} y={y}")

    x,y = change_values(x,y)
    print(f"Despues del cambio: x={x} y={y}")

#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Data frame clientes")
    print("Opcion 2: Par/Impar")
    print("Opcion 3: Intercambiar valores")
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
