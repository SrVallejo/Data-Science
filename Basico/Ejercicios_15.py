import pandas as pd
import os
clear = lambda: os.system('cls')

#EJERCICIO 1

'''1) Crea una lista de nombre "Concursante" que contenga los siguientes valores:

"Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"

2) Crea una lista de nombre "Resultados" que contenga los siguientes valores:

"20", "30", "50", "20", "10", "5", "60", "40"

3) Crea un diccionario con los concursantes y los resultados.

4) Crea un dataframe vacio y apendiza los concursantes y los resultados mediante el empleo de un bucle for

5) Con ayuda de loc filtra los resultados obtenidos desde pedro hasta Lara.

6) Con ayuda de loc filtra los resultados obtenidos mayores o iguales a 40

7) Muestra el concursante con la mayor puntuación

8) Muestra el concursante con la menor puntuación

9) Modifica con la ayuda de loc los valores 20 por 0

10) Modifica Concursante "Juan" su puntuación por "None" con ayuda de .loc
'''

def ejercicio_1():
    contestants = [
        "Juan", "Pedro", "Andrea", 
        "Luis", "Ana", "Lara", 
        "Jose", "Estefania"
    ]
    
    results = [
        20, 30, 50, 
        20, 10, 5, 
        60, 40
    ]

    dic_contestants = {}
    for i in range(len(contestants)):
        dic_contestants[contestants[i]]=results[i]

    print(f"3)Diccionario concursantes:\n{dic_contestants}\n")
    print(f"4)")

    df = pd.DataFrame(columns=["Name","Result"])
    for key,value in dic_contestants.items():
        newrow = pd.DataFrame({"Name":[key],"Result":[value]})
        df = pd.concat([df,newrow],ignore_index=True)
    print(df)

    print("\n5)")
    print(df.loc[1:5])

    print("\n6)")
    print(df.loc[df.Result>40])

    print("\n7)")
    print(df.loc[df.Result==max(df.Result)])

    print("\n8)")
    print(df.loc[df.Result==min(df.Result)])

    print("\n9)")
    df.loc[df.Result==20,"Result"] = 0
    print(df)

    print("\n10)")
    df.loc[df.Name=="Juan","Result"] = None
    print(df)

#EJERCICIO 3

'''Escribe un programa que pida dos palabras y diga si riman o no. 
Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
'''
#If return 2, they rhyme a little, if return 3 they rhyme. If None, string too short.
#1 or 0, don't rhyme.


def rhyme_words(s1,s2):
    if len(s1) <3 or len(s2) <3: return None
    s1,s2 = s1.upper(), s2.upper()
    count = 0
    for i in range(-1,-4,-1):
        if s1[i] != s2[i]: return count
        count += 1
    
    return count

def ejercicio_3():
    word1 = input("Escribe la primera palabra: ")
    word2 = input("Escribe la segunda palabra: ")
    rhyme = rhyme_words(word1,word2)

    print(f"Las palabras {word1} y {word2} ", end="")
    if rhyme == 3: print("riman de forma consonante.")
    elif rhyme == 2: print("riman un poco de forma consonante.")
    else: print("no riman.")


#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Data frame concursantes")
    print("Opcion 3: Palabras que riman")
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