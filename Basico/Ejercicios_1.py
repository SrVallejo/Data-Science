import os
clear = lambda: os.system('cls')
import pandas as pd

# EJERCICIO 1

"""
    Decribe una variable con nombre "notas" que tenga el valor -3
    muestra su valor
"""
def ejercicio_1():
    notas = -3
    print(notas)

# EJERCICIO 2

"""
    Imprime los valores de "s" es igual 25, de "y" es igual a 10, poniendo la siguiente salida:
    El valor de "s" es "valor de s" y el valor de y es "valor de y"
"""
def ejercicio_2():
    s = 25
    y = 10
    print(f'el valor de s es {s} y el valor de y es {y}')
    print('el valor de s es ' + str(s) + ' y el valor de y es ' + str(y))
    print('el valor de s es ', s, ' y el valor de y es ', y)
    print(f'el valor de s es %s y el valor de y es %s' %(s, y))

# EJERCICIO 3

"""
    Declarar una variable con nombre "name",
    que tenga el valor de Juan "El profesor"
"""

def ejercicio_3():
    name = 'Juan "El Profesor"'
    print(name)

# EJERCICIO 4

"""
    Concatena las siguientes palabras formando un sola:
    Juan "El profesor"
"""

def ejercicio_4():
    name = 'Juan'
    job = '"El Profesor"'
    print(f"{name} + {job} = {name + ' ' + job}")

# EJERCICIO 5

"""
    Teniendo la siguientes palabras: no cuentes los días, haz que los días cuenten
     · Pon las primeras letras de cada palabra en mayúsculas
     · Pon todas las letras en mayúsculas
     · Pon todas las letras en minúculas
"""

def ejercicio_5():
    sentence = "no cuentes los días, haz que los días cuenten"
    print (sentence.title())
    print (sentence.upper())
    print (sentence.lower())

# EJERCICIO 6

"""
    Realiza la suma de 26 y 35
    Realiza la multiplicación de 26 y 35
    Realiza la operación de 2 + 32 por 10
    Saca el resultado de 3 elevado a 9
    Redondea el resultado anterior a dos decimales
    Muestra de que tipo se trata
"""
def ejercicio_6():
    x = 26
    y = 35

    print(f"{x} + {y} = {x+y}")
    print(f"{x} * {y} = {x*y}")
    print(f"2 + 32 * 10 = {2+32*10}")

    power = 3**9

    print(f"3 elevado a 9 = {power}")

    power = power/10000
    print(f"(3 elevado a 9)/10000 = {power}")
    power = round(power,2)
    print(f"Redondeado a 2 decimales = {power}")

    powerType = type(power)
    powerType = str(powerType)
    powerType = powerType.replace("<class '","")
    powerType = powerType.replace ("'>","")

    print(f"Y es de tipo {powerType}")


# EJERCICIO 7

"""
    Saca el valor absoluto de -32
    Muestra el máximo y el mínimo de (3, -6, 4, -10, 2.6666)
"""

def ejercicio_7():

    list1 = (3, -6, 4, -10, 2.6666)

    print(f"El valor absoluto de -32 es {abs(-32)}")
    print(f"El valor máximo de la lista es {max(list1)}")
    print(f"El valor mínimo de la lista es {min(list1)}")

# EJERCICIO 8

"""
    Tratar de reemplazar los valores que faltan en este listado --> por un -1
    L = [10, None, 8, 5, None, 20]
    1) Hazlo de la forma más fácil posible teniendo en cuenta la posición (index) de esos valores.
    2) Crea un dataframe con esos valores (L = [10, None, 8, 5, None, 20])
"""

def ejercicio_8():

    L = [10, None, 8, 5, None, 20]

    for i in range(len(L)):
        if L[i] == None:
            L[i] = -1

    print(L)

    
    df_list = pd.DataFrame({"L": L})

    print("\n DataFrame:")
    print (df_list)


#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Notas -3")
    print("Opcion 2: Imprimir 25 y 10")
    print("Opcion 3: Nombre con comillas")
    print("Opcion 4: Concatenación de nombre")
    print("Opcion 5: Mayusculas y Minusculas")
    print("Opcion 6: Operaciones")
    print("Opcion 7: Absoluto y Maximo y mínimo")
    print("Opcion 8: None y Data Frame")
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
        
        elif option == "6":
            ejercicio_6()
            input("Continuar...")

        elif option == "7":
            ejercicio_7()
            input("Continuar...")

        elif option == "8":
            ejercicio_8()
            input("Continuar...")

        elif option == "-1":
            print("Gracias por usar este menú")
            break

        else:
            print("La opción introducida no es valida")
            input("Vuelve a intentarlo")


if __name__ == "__main__":
    main()