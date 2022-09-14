import os
clear = lambda: os.system('cls')
from MenuClass import menu

# EJERCICIO 1

"""
    Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
    Escribir una tercera función que reciba un diccionario con los precios
    y porcentajes de una cesta de la compra, y una de las funciones anteriores, 
    y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
    Ejemplo de diccionario: {1000:20, 500:10, 100:1}
"""
def apply_discount(price, discount):
    discounted = (discount/100)*price
    return price - discounted

def apply_IVA(price, percentage):
    return price + (percentage/100)*price

def price_basket(basket, funcion):
    final_price = 0
    for key in basket.keys():
        final_price += funcion(key,basket[key])
    return final_price


def ejercicio_1():
    basket = {}
    print("Introduce precio y seguido su porcentaje, para acabar la lista, introduce enter")        
    while True:
        end = False
        price = input()
        if price == '': break

        percentage = input()
        if percentage == '':
            percentage = 0
            end = True
        basket[int(price)] = int(percentage)
        if end: break
            
    while True:
        clear()
        print("Introduce el numero de la función que quiere realizar:")
        print("1. Aplicar IVA")
        print("2. Aplicar descuento")
        funcion = input()
                
        if funcion == "1":
            funcion = apply_IVA
            break
        elif funcion == "2":
            funcion = apply_discount
            break
        else: print("Funcion incorrecta")
            
    clear()
    print(f"El precio final es de {price_basket(basket,funcion)} dolares")


# EJERCICIO 2

"""
    Escribir una función que reciba otra función y una lista,
    y devuelva otra lista con el resultado de aplicar
    la función dada a cada uno de los elementos de la lista.
"""



def square(n):
    return n*n

def ejercicio_2():
    numeros = []
    print("Introduce una lista de numeros, termina la lista con un enter")
    while True:
        num = input()
        if num == '': break
        else: numeros.append(int(num))
            
    numeros = list(map(square,numeros))
    clear()
    print("Tu lista con la función cuadrado aplicada:")
    print(numeros)

# EJERCICIO 3

"""
    Escribir una función que reciba una frase y
    devuelva un diccionario con las palabras que contiene y su longitud.
    Ejemplo: "Hola Mundo" --> {"Hola": 4, "Mundo": 5}
"""

def count_words(texto):
    palabras = {}
    palabra = ""
    filtro =[".", ",", ";","?","¿","!","¡","'",'"']


    for letra in texto:
        if letra in filtro:
            pass
        elif letra != " ":
            palabra += letra
        else:
            palabras[palabra] = len(palabra)
            palabra = ""

    if len(palabra) > 0:
        palabras[palabra] = len(palabra)
    return palabras

def ejercicio_3():
    clear()
    texto = input("Introduce un texto: ")
    print(count_words(texto))

#EJERCICIO 4

'''
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones 
correspondientes a esas notas.
'''

def translate_scores(num):
    if num > 0 and num < 5: return "Suspenso"
    elif num < 6: return "Suficiente"
    elif num < 7: return "Bien"
    elif num < 9: return "Notable"
    elif num <=10: return "Excelente"
    return "Nota incorrecta"

def calificaciones(lista):
    dict_calificaciones = {}

    for num in lista:
        dict_calificaciones[num] = translate_scores(num)
    
    return dict_calificaciones

def ejercicio_4():
    notas = []
    print("Introduce una lista de notas, termina la lista con un enter")
    while True:
        num = input()
        if num == '': break
        else: notas.append(float(num))
            
    print(f"La lista de clasificaciones es: ")
    print(calificaciones(notas))

#EJERCICIO 5

'''
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas
en mayúsculas y las calificaciones correspondientes a las notas.
'''

def scores_fixing(dict_notas):
    dict_nuevo = {}
    for key in dict_notas.keys():
        dict_nuevo[key.upper()] = translate_scores(dict_notas[key])
    
    return dict_nuevo

def ejercicio_5():
    dict_notas = {"Algebra": 3.2, "Trigonometria": 10, "Lógica":7.8}
    print("Las notas corregidas son:")
    print(scores_fixing(dict_notas))


#EJERCICIO 6
'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e
imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y
minúsculas.'''

def password_menu(user, password):
    clear()
    print(f"Bienvenido {user}")
    count = 3
    while True:
        aux = input("Introduce tu contraseña: ")
        if aux.upper() == password.upper():
            clear()
            print("Contraseña correcta")
            return True
        clear()
        print("Contraseña incorrecta")
        if count == 0: return False
        print(f"Le quedan {count} intentos")
        count -= 1

def ejercicio_6():
    user = input("Elige un nombre de usuario: ")
    password = input("Elige una contraseña: ")

    if password_menu(user,password):
        print("Has acertado la contraseña")
    else:
        print("No has acertado la contraseña")


#MAIN Y MENU
'''Menu'''

def main():
    funciones =[
        ejercicio_1,ejercicio_2,ejercicio_3,
        ejercicio_4,ejercicio_5,ejercicio_6,
    ]

    opciones = [
        "Cesta de la compra","Funcion a lista", "Contar palabras",
        "Notas","Correción notas","Contraseña"
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

