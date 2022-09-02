import os
clear = lambda: os.system('cls')

# EJERCICIO 1

"""
    Crear un pequeño programa que calcule la multiplicación de 2 números (x, y)
    x = 3, y = 5
    x = 7, y = 3
"""

# a) Con una función (por ejemplo funcion_multiplicar)

# b) Con la función lambda (Tal vez puedes ir a repasarlo)

# c) Realizarlo con entrada de teclado (input)

def multiplication(x,y):
    return x*y

multi = lambda x,y:x*y

def ejercicio_1():
    print("Introduce los números a multiplicar:")
    x = int(input("Primer número: "))
    clear()
    print("Introduce los números a multiplicar:")
    y = int(input("Segundo número: "))

    clear()
    print(f"Función multiplicar:\nEl resultado de {x} x {y} es: {multiplication(x,y)}\n")

    print(f"Función lambda:\nEl resultado de {x} x {y} es: {multi(x,y)}")

# EJERCICIO 2

"""
    -A-
        Dado un string:
        "Level"
        ¿Es un palíndromo?
"""

"""
    -B-
        ¿Y este string?
        "level"
        Nota: "Es un palíndromo si se invierte el orden del string, el resultado es exactamente el mismo"
"""

def palindrom(text):
    text = text.replace(" ","")
    text = text.lower()

    start = 0
    end = len(text)-1

    while start < end:
        if text[start]!= text[end]: break
        else:
            start +=1
            end -=1

    return start >= end


def ejercicio_2():
    text = input("Introduce el texto que quieres saber si es palindromo:\n")
    if palindrom(text): print("Es palíndromo")
    else: print("No es palíndromo")




# EJERCICIO 3

"""
    Dado 2 strings:
    S1 = "Hi!"
    S2 = "Hello!"
    Imprimir las letras que son comunes
"""

def same_letters(text1, text2):
    text1 = text1.upper()
    text2 = text2.upper()
    letters = []
    for c in text1:
        if c in text2 and c not in letters: letters.append(c)
    
    return letters

def ejercicio_3():
    print("Introduce 2 palabras:")
    text1= input("Primera: ")
    text2= input("Segunda: ")
    clear()
    print(f"Ambas palabras tienen estas letras en común:")
    print(same_letters(text1,text2))


#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Función multiplicación")
    print("Opcion 2: Palíndromo")
    print("Opcion 3: Mismas letras")
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
