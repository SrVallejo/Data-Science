from MenuClass import menu
import os
clear = lambda: os.system('cls')
# EJERCICIO 1

'''Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.
Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400'''

def bisiesto(año):
    #Si el año es divisible por 4, podemos comprobar si es bisiesto
    if año%4 == 0:
        #Si el año no es divisible por 100, seguro que es bisiesto, devolvemos true
        if año%100 != 0: return True
        #Si el año es divisible por 100 y por 400, es bisiesto, devolvemos true
        elif año%400 == 0: return True

    #Salimos del if, sabiendo que o bien no es divisible por 4, o bien es divisible por 100 y no por 400,
    #Devolvemos false.
    return False

def ejercicio_1():
    año = int(input("Introduce un año: "))
    if bisiesto(año): print(f"El año {año} es bisiesto")
    else: print(f"El año {año} no es bisiesto")

#EJERCICIO 2

'''Haz un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. 
Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año 
se aplica la tasa de interés introducida. Recordar que uncapital C dolares a un interés del x por cien 
durante n años se convierte en C * (1 + x/100)elevado a n (años). Probar el programa sabiendo que una 
cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.'''

def calcular_interes(dolares, interes, años):
    return dolares * ((1 + interes/100) ** años)


def ejercicio_2():
    dolares = float(input("Introduce una cantidad de dolares inicial: "))
    interes = float(input("Introduce una tasa de interes: "))
    años = int(input("Introduce un número de años: "))
    dolares_finales = round(calcular_interes(dolares,interes,años),2)
    clear()
    print(f"A una tasa del {interes}% en {años} años, sus {dolares} dolares, pasaran a ser {dolares_finales} dolares")



#EJERCICIO 3

'''Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca 
el código de la categoría de la película y posterior a ello pide que el usuario introduzca el número de 
días de atraso, y así se muestra al final el total a pagar.'''

'''"CATEGORIA PRECIO CODIGO RECARGO/DIA DE ATRASO" "FAVORITOS 2.50 1 0.50" "NUEVOS 3.00 2 0.75" 
"ESTRENOS 3.50 3 1.00" "SUPER ESTRENOS 4.00 4 1.50"'''

def calculo_videoclub(codigo, dias):
    if codigo == 1: return 2.50 + (0.50*dias)
    elif codigo == 2: return 3 + (0.75*dias)
    elif codigo == 3: return 3.50 + (1*dias)
    elif codigo == 4: return 4 + (1.50*dias)


def videoclub():
    print("Favoritos: 1")
    print("Nuevos: 2")
    print("Estrenos: 3")
    print("Super Estrenos: 4")
    codigo = int(input("Introduce el codigo de la categoría de tu pelicula: "))
    clear()
    dias = int(input("Introduce el número de días de retraso: "))
    clear()
    print(f"Tendrá que pagar {calculo_videoclub(codigo,dias)} dolares por su pelicula, gracias")



def main():
    funciones =[
        ejercicio_1,ejercicio_2,videoclub,
    ]

    opciones = [
        "Año bisiesto","Calcular interes","Devolver película"
    ]

    my_menu = menu(funciones,opciones)

    while True:
        function = my_menu.select_menu()
        if function == -1: break
        else: function()
        input("Continue...")
    input("Thanks for using this menu")

if __name__ == "__main__":
    main()
