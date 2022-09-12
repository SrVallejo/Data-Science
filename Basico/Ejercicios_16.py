import pandas as pd
import matplotlib.pyplot as plt
import os
clear = lambda: os.system('cls')

#EJERCICIO 1

'''
1) Lee con pandas el archivo train.csv correspondiente al titanic dataset
2) Hacer un bucle for para automatizar las gráficas de pd.crosstab

Se pide relacionar la columna Survived con Pclass, Sex y Embarked

Nota:

Se pide que dentro del bucle for se encuentre la gráfica requerida.

Entonces, en una sola celda, tenemos 3 gráficas mostradas y todo automatizado.

3) Hacer una función para automatizar las gráficas de pd.crosstab

Se pide relacionar la columna Survived con Pclass, Sex y Embarked

NOTA:

Se pide definir una función (1 vez por ello)

y hacer llamadas a la función (3 en este caso, para: Pclass, Sex, Embarked)
'''

def graphic_cross(df,column1, column2):
    figure = pd.crosstab(df[column1],df[column2]).plot(kind="bar")
    plt.show()

def ejercicio_1():
    df = pd.read_csv(r"Data Sets\train.csv")

    columns = ["Pclass","Sex","Embarked"]
    i = 1
    for name in columns:
        print(f"Gráfico {i}")
        i+=1
        graphic_cross(df,name,"Survived")

#EJERCICIO 2

'''
Ejercicio de obtener los valores que muestra el pd.crosstab de Sex y Pclass sin usar el propio pd.crosstab

1) Imprime nuevamente los primeros 5 valores
2) Usando value_counts() observa cuantos hombres y mujeres hay

(No hace falta plotear, simplemente mostrar los números de cada)
3) Sin usar value_counts() observa cuantos hombres y mujeres hay

(con un algoritmo)

4) Ahora haz lo mismo de otra forma

En esta ocasión se pide que:

crees un dataframe con el formato del original,

bajo la permisa que sea un dataframe con todo hombres (primeramente)

y con todo mujeres (a continuación)

(2 DataFrames por tanto)

Y observes si el número de filas de ambos nuevos DataFrames coincide con los valores anteriores

'''

def ejercicio_2():
    df = pd.read_csv(r"Data Sets\train.csv")
    #1)
    print(f"1)\n{df.loc[:4]}")

    #2)
    female_total = int(df.loc[df["Sex"]=="female","Sex"].value_counts())
    male_total = int(df.loc[df["Sex"]=="male","Sex"].value_counts())
    print(f"\n2) Con value counts\nTotal mujeres: {female_total}\nTotal hombres: {male_total}")

    #3)
    female_total = 0
    male_total = 0
    nulls = 0

    df_sex = df["Sex"]

    for row in df_sex:
        if row == "female": female_total += 1
        elif row == "male": male_total += 1
        else: nulls +=1
    print(f"\n3) Con algoritmo\nTotal mujeres: {female_total}\nTotal hombres: {male_total}\nValores nulos: {nulls}")

    df_females = df["Sex"].loc[df.Sex == "female"]
    print(f"\n4)\nData frame mujeres:\n{df_females.describe()}")

    df_males = df["Sex"].loc[df.Sex == "male"]
    print(f"\nData frame hombres:\n{df_males.describe()}")


#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Función para plot")
    print("Opcion 2: Total de mujeres y hombres en Data Frame")
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

