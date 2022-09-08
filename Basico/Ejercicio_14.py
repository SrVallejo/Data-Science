import pandas as pd
import os
clear = lambda: os.system('cls')

#EJERCICIO 1

'''Lista de fibonacci

los n primeros números'''

def fibo_list_n(n):
    fibo = []
    if n > 0: fibo.append(0)
    if n > 1: fibo.append(1)

    for i in range(2,n):
        fibo.append(fibo[-1]+fibo[-2])

    return fibo

def ejercicio_1():
    n = int(input("Números de la lista de fibonacci requeridos: "))
    print(fibo_list_n(n))

#EJERCICIO 2

def fibo_between(start,end):
    if start > end: return None

    fibo = []
    prev = 0
    last = 1
    if prev >= start: fibo.append(prev)
    if end <= last >= start: fibo.append(last)

    while (prev+last <= end):
        if prev+last >= start: fibo.append(prev+last)
        last = prev + last
        prev = last - prev
    
    return fibo

def ejercicio_2():
    start = 200
    end = 100000
    print(f"Números de fibonacci entre {start} y {end}:")
    print(fibo_between(start,end))


#EJERCICIO 3

'''Se pide crear un NUEVO dataframe para cada uno de los siguientes casos planteados y que están relacionados con el Titanic DataSet (antes debéis de cargar el archivo como df)

1) Leer el archivo train.csv del titanic dataset

2) Crear un dataframe de nombre df_sobreviven refiriéndose a un dataframe en el que todos los pasajeros sobreviven
NOTA: si al principio no estás seguro del resultado, puedes usar value_counts() para comprobar tu resultado

3) Crear un dataframe de nombre df__no_sobreviven refiriéndose a un dataframe en el que NINGUNO de los pasajeros sobrevive

4) DataFrame de hombres que no sobrevivieron en el titanic

5) DataFrame de hombres que si sobrevivieron en el titanic

6) DataFrame de mujeres que no sobrevivieron en el titanic

7) DataFrame de mujeres que si sobrevivieron en el titanic'''

def ejercicio_3():
    #1)
    df = pd.read_csv(r"Data Sets\train.csv")
    print(f"1) Data frame train.csv:\n{df}")
    #2)
    df_survived = df.loc[df.Survived==1]
    print(f"\n2) Data frame survived:\n{df_survived}")
    #3)
    df_no_survived = df.loc[df.Survived==0]
    print(f"\n3) Data frame no survived:\n{df_no_survived}")
    #4)
    df_men_no_survived = df.loc[(df.Survived==0)&(df.Sex=="male")]
    print(f"\n4) Data frame men no survived:\n{df_men_no_survived}")
    #5)
    df_men_survived = df.loc[(df.Survived==1)&(df.Sex=="male")]
    print(f"\n5) Data frame men survived:\n{df_men_survived}")
    #6)
    df_women_no_survived = df.loc[(df.Survived==0)&(df.Sex=="female")]
    print(f"\n6) Data frame women no survived:\n{df_women_no_survived}")
    #7)
    df_women_survived = df.loc[(df.Survived==1)&(df.Sex=="female")]
    print(f"\n7) Data frame women survived:\n{df_women_survived}")

#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Fibonacci n números")
    print("Opcion 2: Fibonacci entre 2 números")
    print("Opcion 3: Data Frames")
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