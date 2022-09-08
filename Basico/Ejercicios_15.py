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


ejercicio_1()