import pandas as pd
import os
clear = lambda: os.system('cls')

# Ejercicio 1

"""
    Desarrolla el siguiente ejercicios de POO:
   * Alumnos  -> Es la clase.
   * __init__ -> Es el método init
   * nombre, edad, asignatura y nota son las propiedades
   * Instanciamos..
   * los posibles alumnos (alumno1, alumno2, alumno3..) --> son los "objetos"
   * y el.__init__ los inicializa
   A continuación muestra la edad del alumno 2 y el alumno 3 y sus notas
"""


class Alumnos:
    def __init__(self,nombre,edad,asignatura,nota):
        self.nombre = nombre
        self.edad = edad
        self.asignatura = asignatura
        self.nota = nota

    def get_name (self):
        return self.nombre

    def get_score (self):
        return self.nota

    def get_age (self):
        return self.edad
    
    def get_course(self):
        return self.asignatura

    
    
def imprimir_lista_alumnos(lista_alumnos):
    for i in range(len(lista_alumnos)):
        nombre = lista_alumnos[i].get_name()
        edad = lista_alumnos[i].get_age()
        asignatura = lista_alumnos[i].get_course()
        nota = lista_alumnos[i].get_score()
        print(f"Alumno {i+1}: {nombre}, {edad} años: {asignatura} = {nota}")

def ejercicio_1():
    lista_alumnos = []
    alumno = Alumnos("Ahmad", 21,"Derecho romano",9.25)
    lista_alumnos.append(alumno)
    alumno = Alumnos("Anastasia", 45,"Electromecánica",6.7)
    lista_alumnos.append(alumno)
    alumno = Alumnos("Federica", 19,"Latín",4.2)
    lista_alumnos.append(alumno)
    imprimir_lista_alumnos(lista_alumnos)


# Ejercicio 2

"""
    Escribir un programa que pregunte al usuario su edad
    y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def print_numbers(n):
    for i in range(1,n+1):
        print(i,end="")
        if i < n:
            print(", ",end="")
        else:
            print()

def ejercicio_2():
    age = input("Dime tu edad: ")
    print_numbers(int(age))


# Ejercicio 3

"""
    Escribir un programa que pida al usuario una palabra y
    luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

def inverse_word(word):
    for i in range(len(word)-1,-1,-1):
        print(f"{word[i]} ",end="")
    print()

def ejercicio_3():
    word = input("Dime una palabra: ")
    inverse_word(word)

# Ejercicio 4

"""
    Escribir un programa que pregunte el nombre completo del usuario en la consola y
    después muestre por pantalla el nombre completo del usuario tres veces,
    una con todas las letras minúsculas,
    otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
    El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
def upper_first_letter(word):
    put_upper = True
    new_word = ""
    for letter in word:
        if put_upper:
            letter = letter.upper()
            put_upper = False
        elif letter == " ":
            put_upper = True
        else:
            letter = letter.lower()

        new_word += letter
    
    return new_word


def ejercicio_4():
    name = input("Introduce tu nombre completo: ")
    print(name.lower())
    print(name.upper())
    print(upper_first_letter(name))



# Ejercicio 5

"""
    Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
    y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
    Escribir un programa que pregunte por un número de teléfono con este formato
    y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
def divide_phone_number(phone_number):
    divided_phone = phone_number.split("-")
    return divided_phone[0],divided_phone[1],divided_phone[2]

def ejercicio_5():
    phone_number = input("Introduce un número de telefono con el formato +pp-nnnnnnnnn-xx: ")
    try:
        prefix,number,extension = divide_phone_number(phone_number)
        print(f"Prefijo: {prefix} Número: {number} Extensión: {extension}")
    except:
        print("Wrong phone format")
    
# Ejercicio 6

"""
    Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
    y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
def text_letter_upper(sentence,letter):

    new_text = ""
    letter = letter.lower()
    for c in sentence:
        if c == letter: c = c.upper()
        new_text += c

    return new_text


def ejercicio_6():
    sentence = input("Introduce una frase: ")
    vowel = input("Introduce una vocal: ")
    print(text_letter_upper(sentence,vowel))

# Ejercicio 7

"""
    Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
    y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
def divide_decimals(x):
    n = int(x)
    d = round(x - n,2)
    while d!=int(d): d *= 10
    return n,int(d)


def ejercicio_7():
    price = input("Introduce el precio de un producto, con el formato xxxx.xx: ")
    euros, cents = divide_decimals(float(price))
    print(f"El precio es de {euros} € y {cents} centimos")

# Ejercicio 8

"""
    Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
    Mes Ventas Gastos
    Enero 30500 22000
    Febrero 35600 23400
    Marzo 28300 18100
    Abril 33900 20700
"""

def ejercicio_8():

    Months = ["Enero","Febrero","Marzo","Abril"]
    Sales = [30500,35600,28300,33900]
    Expenses = [22000,23400,18100,20700]

    df_balance = pd.DataFrame({"Mes": Months, "Ventas": Sales, "Gastos": Expenses})
    print(df_balance)

# Ejercicio 9

"""
    Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
    una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.
"""
def balance(sales_list, expenses_list):

    if len(sales_list) != len(expenses_list): return False

    list_balance = []
    for i in range(len(sales_list)):
        list_balance.append(sales_list[i]-expenses_list[i])
    return list_balance

def prepare_df_ejercicio_9():
    Months = [
        "Enero","Febrero","Marzo",
        "Abril","Mayo","Junio",
        "Julio","Agosto","Septiembre",
        "Octubre","Noviembre","Diciembre"
    ]
    Sales = [
        30500,35600,28300,
        33900,30600,40000,
        25000,22000,39000,
        37000,32400,31700
    ]
    Expenses = [
        22000,23400,18100,
        20700,18000,17500,
        16900,22500,25800,
        30000,34000,19000
    ]

    df_balance = pd.DataFrame({"Mes": Months, "Ventas": Sales, "Gastos": Expenses})
    balance_list = balance(df_balance["Ventas"].tolist(),df_balance["Gastos"].tolist())
    df_balance = df_balance.assign(Balance=balance_list)

    return df_balance

def ejercicio_9():
    df_balance = prepare_df_ejercicio_9()
    print(df_balance)

    print("Elige meses de entre los de la lista, acaba en enter:")
    print(df_balance["Mes"].tolist())
    month = " "
    month_list = []
    while month != "":
        month = input()
        month_list.append(month)
    clear()


    total_balance = 0
    for m in month_list:
        total_balance += df_balance[df_balance.Mes==m]["Balance"].sum()
    
    print(f"La suma del balance de esos meses es de {total_balance}")



    

# Ejercicio 10

"""
    Escribir un programa que almacene las asignaturas de un curso
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
    pregunte al usuario la nota que ha sacado en cada asignatura,
    y después las muestre por pantalla con el mensaje "Has sacado ASIGNATURA la nota de NOTA"
    donde es cada una de las asignaturas de la lista y cada una de las correspondientes notas introducidas por el usuario.
"""

def ask_score(courses_list):
    scores_list = []
    clear()
    for course in courses_list:
        scores_list.append(float(input(f"Que nota has sacado en {course}: ")))
        clear()
    
    return scores_list


def ejercicio_10():
    asignaturas = [

        "Matemáticas", "Física", "Química",
        "Historia", "Lengua Castellana", "Ingles",
        "Educación Fisica"
    ]
    notas = ask_score(asignaturas)
    for i in range(len(notas)): print(f"Has obtenido un {notas[i]} en {asignaturas[i]}")
    if all(n >= 5 for n in notas): print("Felicidades, has aprobado todas")
    else: print("Te toca recuperar")

#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Clase Alumnos")
    print("Opcion 2: Edad impresa")
    print("Opcion 3: Inversión palabra")
    print("Opcion 4: Nombre mayusculas/minusculas")
    print("Opcion 5: Número de teléfono")
    print("Opcion 6: Frase y vocal mayusculas")
    print("Opcion 7: Dividir precio")
    print("Opcion 8: Data frame ventas")
    print("Opcion 9: Data frame balance")
    print("Opcion 10: Preguntar notas")
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

        elif option == "4":
            ejercicio_4()
            input("Continuar...")

        elif option == "5":
            ejercicio_5()
            input("Continuar...")
        
        elif option == "6":
            ejercicio_6()
            input("Continuar...")

        elif option == "7":
            ejercicio_7()
            input("Continuar...")

        elif option == "8":
            ejercicio_8()
            input("Continuar...")

        elif option == "9":
            ejercicio_9()
            input("Continuar...")

        elif option == "10":
            ejercicio_10()
            input("Continuar...")

        
        elif option == "-1":
            print("Gracias por usar este menú")
            break

        else:
            print("La opción introducida no es valida")
            input("Vuelve a intentarlo")


if __name__ == "__main__":
    main()