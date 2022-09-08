import pandas as pd
import os
clear = lambda: os.system('cls')

#EJERCICIO 1

'''Se pide por tanto:
-1- Leer el archivo train.csv de Titanic dataset con pandas
-2- Imprimir algunas filas de la parte de arriba y otras de la parte del final
-3- Imprimir algunos parámetros estadísticos
-4- Ver si en todas las columnas tenemos el mismo número de datos (solo verlo)
-5- Ver el número de hombres y mujeres que hay
-6- Hacer alguna gráfica con pandas relativa al número de hombres y mujeres que hay
Si quieres hacer alguna cosa más también puedes'''

df = pd.read_csv('..\Data Sets\train.csv')
print(df)