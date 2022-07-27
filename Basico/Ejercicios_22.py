import os
clear = lambda: os.system('cls')

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

# EJERCICIO 2

"""
    Escribir una función que reciba otra función y una lista,
    y devuelva otra lista con el resultado de aplicar
    la función dada a cada uno de los elementos de la lista.
"""

def aplica_funcion_lista(funcion, lista):
    for i in range(len(lista)):
        lista[i] = funcion(lista[i])
    return lista

def cuadrado(n):
    return n*n

# EJERCICIO 3

"""
    Escribir una función que reciba una frase y
    devuelva un diccionario con las palabras que contiene y su longitud.
    Ejemplo: "Hola Mundo" --> {"Hola": 4, "Mundo": 5}
"""

def contar_palabras(texto):
    palabras = {}
    palabra = ""
    filtro =[".", ",", ";","?","¿","!","!","'",'"']


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


#EJERCICIO 4

'''
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones 
correspondientes a esas notas.
'''

def traduccion_notas(num):
    if num > 0 and num < 5: return "Suspenso"
    elif num < 6: return "Suficiente"
    elif num < 7: return "Bien"
    elif num < 9: return "Notable"
    elif num <=10: return "Excelente"
    return "Nota incorrecta"

def calificaciones(lista):
    dict_calificaciones = {}

    for num in lista:
        dict_calificaciones[num] = traduccion_notas(num)
    
    return dict_calificaciones


#EJERCICIO 5

'''
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas
en mayúsculas y las calificaciones correspondientes a las notas.
'''

def correccion_notas(dict_notas):
    dict_nuevo = {}
    for key in dict_notas.keys():
        dict_nuevo[key.upper()] = traduccion_notas(dict_notas[key])
    
    return dict_nuevo

'''Menu'''
def pintar_menu():
    print("Opcion 1: Cesta de la compra")
    print("Opcion 2: Funcion a lista")
    print("Opcion 3: Contar palabras")
    print("Opcion 4: Notas")
    print("Opcion 5: Correción notas")
    print("Opcion -1: Salir")



def main():

    while True:
        clear()
        pintar_menu()
        option = input("Elige una opción: ")
        clear()

        if option == "1":
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
                else:
                    print("Funcion incorrecta")
            
            clear()
            print(f"El precio final es de {price_basket(basket,funcion)} dolares")
            input("Continuar...")



        elif option == "2":
            numeros = []
            print("Introduce una lista de numeros, termina la lista con un enter")
            while True:
                num = input()
                if num == '': break
                else: numeros.append(int(num))
            
            numeros = aplica_funcion_lista(cuadrado,numeros)
            clear()
            print("Tu lista con la función cuadrado aplicada:")
            print(numeros)
            input("Continuar...")

        elif option == "3":
            clear()
            texto = input("Introduce un texto: ")
            print(contar_palabras(texto))
            input("Continuar...")

        elif option == "4":
            notas = []
            print("Introduce una lista de notas, termina la lista con un enter")
            while True:
                num = input()
                if num == '': break
                else: notas.append(float(num))
            
            print(f"La lista de clasificaciones es: ")
            print(calificaciones(notas))
            input("Continuar...")

        
        elif option == "5":
            dict_notas = {"Algebra": 3.2, "Trigonometria": 10, "Lógica":7.8}
            print("Las notas corregidas son:")
            print(correccion_notas(dict_notas))
            input("Continuar...")
            
        elif option == "-1":
            print("Gracias por usar este menú")
            input()
            clear()
            break

        else:
            print("La opción introducida no es valida")
            input("Vuelva a intentarlo")


if __name__ == "__main__":
    main()


