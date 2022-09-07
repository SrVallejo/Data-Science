import numpy as np
import pandas as pd
import os
clear = lambda: os.system('cls')

#EJERCICIO 1
'''1)

Haz un programa que calcule los múltiplos de 3

    Para ello primero primero debe preguntarse al usuario cuántos múltiplos desea añadir.

    Nota: Puedes usar un bucle while si lo deseas

2)

Haz lo mismo con np.arange
'''
#function that return the quantity of numbers that are multiple of num
def multiples_list(num, quantity):
    multi_list=[]
    for i in range(1,quantity+1):
        multi_list.append(i*num)
    return multi_list

def multiples_numpy(num, quantity):
    a = np.arange(1,quantity+1)
    for i in range(len(a)):
        a[i] = a[i]*num

    return a

def ejercicio_1():
    multiplo = int(input("¿De qué número quieres encontrar múltiplos? "))
    cantidad = int(input("¿Cuantos números quieres? "))
    clear()

    print(f"1) Con lista:\n{multiples_list(multiplo,cantidad)}\n")
    print(f"2) Con numpy:\n{multiples_numpy(multiplo,cantidad)}")

#EJERCICIO 2

'''Dada esta lista de variable "listado" y "valores": 10, 10, 20, 20, 20, 30, 40

Se pide:

1) Crea un DataFrame con esa información e imprímelo

2) Usa value_counts() para determinar cuántas repeticiones hay de cada número en esa columna

3) Haz un ".shape" a esa información del value_counts()

NOTA: Escribe: .shape justo al final


4) A esa misma instrucción con value_counts() escribe al final ".values"

Y veras la información..
pasa esa información a lista si puedes

y guarda ese listado como "repeticiones"



5)

A esa información de value_counts() añade al final ".index"

Y pasa posteriormente a lista esa información

y guarda ese listado con el nombre: "valores"

6)

Crea un DataFrame con 2 columnas,

1 para "valores"

1 para "repeticiones"

llámalo: "df_value_counts" (por ejemplo)

Y observa..

7)

Haz lo siguiente: "df.value_counts()"

8)

Observa si hay diferencias entre: "df" y "df_value_counts"
'''

def ejercicio_2():

    values = [
        10, 10, 20, 
        20, 20, 30, 
        40
    ]
    #1)
    df = pd.DataFrame({"Values":values})
    print(f"1) Data Frame:\n\n{df}\n")

    #2)
    print(f"2) Value Counts:\n\n{df.value_counts()}\n")

    #3)
    print(f"3) Value Counts Shape:\n\n{df.value_counts().shape}\n")

    #4)
    repetitions = df.value_counts().values.tolist()
    print(f"4) Value Counts repetitions into list:\n\n{repetitions}\n")

    #5)
    values = df.Values.value_counts().index.tolist()
    print(f"5) Value Counts values into list:\n\n{values}\n")

    #6)
    df_value_counts = pd.DataFrame({"Values":values,"Repetitions":repetitions})
    print(f"6) DataFrame Value Counts:\n\n{df_value_counts}\n")

ejercicio_2()


#EJERCICIO 3

'''Comparación de matrices

Haz el código que testee si esas 2 matrices son iguales
'''

