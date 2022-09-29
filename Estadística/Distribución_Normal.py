import os
clear = lambda: os.system("cls")

'''
Ejercicio 1:

En 2007-2008, la altura promedio de un jugador de baloncesto profesional fue de 2,00 metros 
con una desviación estándar de 0,02 metros. 
Harrison Barnes es un jugador de baloncesto que mide 2,03 metros. 
¿Qué porcentaje de jugadores son más altos que Barnes?
'''

zscore = lambda µ,s,x: round((x - µ)/ s, 2)
clear()

print("Ejercicio 1:")
zBarnes = zscore(2,0.02,2.03)
print(f"Z score = {zBarnes}")
print("P value = 93.32%")
print(f"El 68% de los jugadores es más alto que barnes")

'''Ejercicio 2

Chris Paul mide 1,83 metros. 
¿Qué proporción de jugadores de baloncesto se encuentran entre las alturas de Paul y Barnes?
'''

print("\nEjercicio 2:")
zPaul = zscore(2,0.02,1.83)
print(f"Z score = {zPaul}")
print("P value = 0%")
print(f"Entre ambas alturas se encuentran el 93.32% de los jugadores")

'''
Ejercicio 3

El 92 % de los candidatos obtuvo una puntuación tan buena o peor que la de Steve. 
Si la puntuación promedio fue 55 con una desviación estándar de 6 puntos, ¿cuál fue el puntuación de Steve?
'''

xvalue = lambda µ,s,z: µ + s*z
print("\nEjercicio 3:")
print("Consultamos la tabla para 92%")
print(f"Z score = 1.4")
print(f"Puntuación de steve = {xvalue(55,6,1.4)} ")
