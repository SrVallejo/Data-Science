'''
Ejercicios
Ejercicio 1:

Calcula la Z score para los siguientes casos:

    µ = 54, s = 12, x = 68
    µ = 25, s = 3.5, x = 20
    µ = 0.01, s = 0.002, x = 0.01

'''

zscore = lambda µ,s,x: round((x - µ)/ s, 2)
print(f"Zscore 1: {zscore(54,12,68)}")
print(f"Zscore 2: {zscore(25,3.5,20)}")
print(f"Zscore 3: {zscore(0.01,0.002,0.01)}")

'''
Ejercicio 2:

El GPA promedio de los estudiantes en una escuela de secundaria local es 3.2 con una desviación estándar de 0.3. 
Jenny tiene GPA de 2.8 ¿A cuántas desviaciones estándar de la media está el GPA de Jenny?

'''
print(f"\nEjercicio 2:\nZscore = {zscore(3.2,0.3,2.8)}" )

'''
Ejercicio 3:

Jenny está tratando de demostrarles a sus padres que le va mejor en la escuela que a su prima. 
Su prima asiste a una escuela de secundaria diferente donde el GPA promedio es 3.4 con una desviación estándar 
de 0.2. El prima de Jenny tiene un GPA de 3.0.
¿se está desempeñando Jenny mejor que su prima según los puntajes estándar?

'''

print(f"\nEjercicio 3:\nZscore = {zscore(3.4,0.2,3.0)}")
print("Jenny está más cerca de la media de su instituto que su prima")

'''
Ejercicio 4:

La puntuación de Kyle en una prueba de matemáticas reciente fue de 2.3 desviaciones estándar 
de la puntuación media del 78%. Si la desviación estándar de los puntajes de la prueba fue del 8%. 
¿Qué puntaje obtuvo kyle en su prueba?
'''

μ = 78
s = 8
z = 2.3
x1 = 78 + 8*2.3
x2= 78 - 8*2.3
print("\nEjercicio 4:")
print(f"La nota de Kyle será de {x1} o de {x2} dependiendo si ha sacado una nota por encima de la media, o por debajo")