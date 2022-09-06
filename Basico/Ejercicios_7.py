import numpy as np
from time import sleep
import os
clear = lambda: os.system('cls')

# EJERCICIO 1

"""
    Dado: "np.arange(2,10)"
    sigue los siguientes pasos:
    1) Escribe esa instrucción y asígnaselo a la variable "a"
"""

# 2) ¿Es equivalente a "np.arange(2,10,1)"?

# 3) Se pide quedarse con aquellos números menores de 5.

    # hazlo con numpy si puedes para la variable "a"

# 4) Hazlo pasando esa información (de "a") a una lista

# 5) En base a los resultados..

    # ¿Es posible recorrer 1 a 1 un array de numpy?

# 6) Haz el mismo proceso programando una sola línea (toma "a" como referencia)

def compare_arrays(array1,array2):
    for i in range(len(array1)):
        if array1[i]!= array2[i]: return False

    return True

def delate_less_than(array, limit):
    pos_del=[]
    for i in range(len(array)):
        if array[i]>= limit: pos_del.append(i)

    return np.delete(array,pos_del)

def ejercicio_1():
    #1)
    a = np.arange(2,10)

    #2)
    b = np.arange(2,10,1)

    print(f"2)\nArray a:\n{a}\nArray b:\n{b}")
    if len(a) == len(b):
        if compare_arrays(a,b): print("Son iguales")
        else: print("No tienen los mismos valores")
    else: print("No tienen el mismo tamaño")

    print()

    #3)
    a = delate_less_than(a,5)
    print(f"3)\nSolo números menores de 5\n{a}\n")

    #4)
    a = np.arange(2,10)
    list = []
    for i in range(len(a)):
        if a[i] < 5:
            list.append(a[i])

    print(f"4)\nLista solo números menores de 5\n{list}\n")

    #6)
    a = np.arange(2,5)
    print(f"6)\nArray solo números menores de 5\n{a}\n")



# EJERCICIO 2

"""
    Para estos valores (v de valores por abreviar):
    v1 = 4
    v2 = 5
    v3 = 7
    v4 = 8
    El objetivo será calcular la media de estos valores
    Para ello sigue los siguientes pasos:
"""

# 1) Imprime los valores de esas variables v1,v2,v3,v4

# 2) Descomenta las 2 líneas siguientes para aprender..

    # que es posible asignar varios valores en la misma línea

    # Y la asignación de valores a variables se hace de forma consecutiva.

#3) Descomenta la línea siguiente para aprender una posible forma de calcular la media.

    #  Usamos nuevamente numpy..

# 4) Calcula la media sin usar numpy

    # Si el resultado no sale bien, razona cómo debería hacerse..

def mean_list(list):
    sum = 0
    for e in list:
        sum += e
    
    return sum/len(list)

def ejercicio_2():

    num_list =[4,5,7,8]
    print(f"La media es:\n{mean_list(num_list)}")

# EJERCICIO 3

"""
    Factorial de un número
    Nota:
    El Factorial de 5, por ejemplo:
    5! = 5 * 4 * 3 * 2 * 1 = 120
    y el de 3:
    3! = 3 * 2 * 1 = 6
    y así para todos..
    PASOS A SEGUIR Y COSAS A TENER EN CUENTA
    Pide por teclado el número del cual quieres calcular el factorial.
    Para que no sea muy grande te recomendamos:
    3,4 o 5 (para hacer las pruebas)
    si ya no lo recuerdas o nunca lo viste, no te preocupes..
    3! es: 3 * 2 * 1 = 6
    4! es: 4 * 3 * 2 * 1 = 24
    5! es: 5 * 4 * 3 * 2 * 1 = 120
    (esto es lo que se pide, en esencia)
"""
def factorial(num):
    if num == 1: return 1
    else: return num*factorial(num-1)

def ejercicio_3():
    num = int(input("Introduce un valor para calcular el factorial: "))
    print(f"{num}! = {factorial(num)}")


# EJERCICIO 4

"""
    Haz un cronómetro en Python:
    Obviamente:
    Horas - Minutos - Segundos
    Debes usar lo siguiente (from time import sleep)
    NOTA: Si quieres puedes usar sleep(0.000001)
    en vez de sleep(1) -> 1 segundo
    (para no esperar 1 segundo a ver los cambios)
    Para poder pararlo en poco tiempo,
    imprime mientras horas<2, cuando llegue a 2 debería parar la ejecución.
    Debería ejecutarse en unos 2 minutos aprox.
"""

def ejercicio_4():
    horas = 0
    minutos = 0
    segundos = 0
    cero_segundos = "0"
    cero_minutos = "0"
    cero_horas = "0"

    while True:
        clear()
        print(f"{cero_horas}{horas}:{cero_minutos}{minutos}:{cero_segundos}{segundos}")
        sleep(0.000001)
        segundos += 1
        if segundos > 59:
            segundos = 0
            minutos +=1
            
            if minutos >59:
                minutos = 0
                horas +=1
                if horas > 23: horas = 0
                if horas < 10: cero_horas = "0"
                else: cero_horas = ""
            
            if minutos <10: cero_minutos = "0"
            else: cero_minutos = ""

        if segundos <10: cero_segundos = "0"
        else: cero_segundos = ""

#MENU Y MAIN

def pintar_menu():
    print("Opcion 1: Arrays")
    print("Opcion 2: Media")
    print("Opcion 3: Factorial")
    print("Opcion 4: Reloj")
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