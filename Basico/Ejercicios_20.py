import os
clear = lambda: os.system('cls')

# EJERCICIO 1

"""
    Definir una función generar_n_caracteres() que tome un entero n
    y devuelva el caracter multiplicado por n.
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n, c):
    s = ""
    for i in range(n):
        s += c
    return s

# EJERCICIO 2

"""
    Definir un diagrama procedimiento() que tome una lista de números enteros
    e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7])
    debería imprimir lo siguiente:
"""

def procedimiento(lista):
    for num in lista:
        print(generar_n_caracteres(num,'X'))

# EJERCICIO 3

"""
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

def mas_larga(palabras):
    larga = palabras[0]
    for i in range(1,len(palabras),1):
        if len(larga) < len(palabras[i]): 
            larga = palabras[i]
    return larga


# EJERCICIO 4

"""
    Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
    y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras(lista, n):
    filtradas =[]
    for palabra in lista:
        if len(palabra) >= n:
            filtradas.append(palabra)

    return filtradas

# EJERCICIO 5

"""
    Escribir un programa que ingrese una cadena de texto.
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

def c_mayusculas(cadena):
    count = 0
    for c in cadena:
        if c.isupper(): count +=1
    
    return count


# EJERCICIO 6

"""
    Definir una tupla con 10 edades de personas.
        * Imprimir la cantidad de personas con edades superiores a n
"""
def mayores (tup, n):
    count = 0
    for edad in tup:
        if edad >= n: count += 1
    
    return count

# EJERCICIO 7

"""
    Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

def empiezapor(lista, letra):
    count = 0
    for nombre in lista:
        if nombre[0].upper() == letra.upper(): count +=1
    return count

# EJERCICIO 8

"""
    Crear una función contar_vocales(),
    que reciba una palabra y cuente cuantas letras "a" tiene,
    cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.
"""

# Devuelve la palabra en mayusculas y sin tildes
def limpiar_palabra(palabra):
    palabra = palabra.upper()
    palabra = palabra.replace("Á","A")
    palabra = palabra.replace("É","E")
    palabra = palabra.replace("Í","I")
    palabra = palabra.replace("Ó","O")
    palabra = palabra.replace("Ú","U")
    return palabra


def contar_vocales(palabra):
    palabra = limpiar_palabra(palabra)
    vocales = ["A","E","I","O","U"]
    dict_vocales = {}
    for vocal in vocales:
        count = 0
        for letra in palabra:
            if letra == vocal: count += 1
        
        dict_vocales[vocal]= count
    
    return dict_vocales


'''Menu'''
def pintar_menu():
    print("Opcion 1: generar N caracteres")
    print("Opcion 2: Imprimir procedimiento")
    print("Opcion 3: Palabra más larga")
    print("Opcion 4: Filtrar palabras")
    print("Opcion 5: Contar mayusculas")
    print("Opcion 6: Contar edades mayores")
    print("Opcion 7: Contar palabras que empiezan por")
    print("Opcion 8: Contar vocales")

    print("Opcion -1: Salir")



def main():

    while True:
        clear()
        pintar_menu()
        option = input("Elige una opción: ")
        clear()

        if option == "1":
            c = input("¿Qué caracter quieres generar? ")
            n = int(input("¿Cuantas veces?"))

            print(generar_n_caracteres(n,c))
            input("Continuar...")

        elif option == "2":
            numeros = []
            print("Introduce una lista de números, termina la lista con un enter")
            while True:
                num = input()
                if num == '': break
                else: numeros.append(int(num))
            
            procedimiento(numeros)
            input("Continuar...")

        elif option == "3":
            palabras = []
            print("Introduce una lista de palabras, termina la lista con un enter")
            while True:
                palabra = input()
                if palabra == '': break
                else: palabras.append(palabra)
            
            print("La palabra más larga es:")
            print(mas_larga(palabras))
            input("Continuar...")

        elif option == "4":
            palabras = []
            print("Introduce una lista de palabras, termina la lista con un enter")
            while True:
                palabra = input()
                if palabra == '': break
                else: palabras.append(palabra)
            
            n = int(input("Número por el que filtrar: "))
            print(filtrar_palabras(palabras,n))
            input("Continuar...")

        elif option == "5":
            texto = input("Introduce un texto para contar: ")
            print(f"El texto tiene {c_mayusculas(texto)} mayusculas")
            input("Continuar...")

        elif option == "6":
            edades = []
            print("Introduce una lista de edades, termina la lista con un enter")
            while True:
                num = input()
                if num == '': break
                else: edades.append(int(num))
            n = int(input("Edad mínima: "))
            print(f"Hay {mayores(edades,n)} personas mayores de {n} años")
            input("Continuar...")


        elif option == "7":
            palabras = []
            print("Introduce una lista de palabras, termina la lista con un enter")
            while True:
                palabra = input()
                if palabra == '': break
                else: palabras.append(palabra)
            
            c = input("Letra inicial: ")
            print(f"Hay {empiezapor(palabras,c)} palabras que empiezan por {c}")
            input("Continuar...")


        elif option == "8":
            texto = input("Introduce un texto para contar vocales: ")
            print("El texto tiene las siguientes vocales")
            print(contar_vocales(texto))
            input("Continuar...")


        elif option == "-1":
            print("Gracias por usar este menú")
            input()
            clear()
            break

        else:
            print("La opción introducida no es valida")
            input("Vuelve a intentarlo")


if __name__ == "__main__":
    main()

