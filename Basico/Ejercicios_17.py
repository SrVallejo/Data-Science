import os
clear = lambda:os.system('cls')

#EJERCICIO 17

'''
Crea la clase "matematicas" y dentro de esa clase crea las funciones suma y resta, 
en dichas funciones nos deberán devolver el resultado de la suma y de la resta, 
siguiendo los siguientes pasos:'''

class matematicas:

    def sum(n1,n2):
        return n1+n2
    
    def sub(n1,n2):
        return n1-n2


def ejercicio_1():
    n1 = 32
    n2 = 14
    print(f"Suma: {n1} + {n2} = {matematicas.sum(n1,n2)}")

    n1,n2 = 10, 48
    print(f"Resta: {n1} - {n2} = {matematicas.sub(n1,n2)}")


#EJERCICIO 2

'''
Crea dos clases una llamala "libros" y otra clase "materias".

A la clase libros declara una función con nombre "tipos" y dentro de clase materias 
declara una función con nombre "asignaturas".

A la función tipos retorne el valor name = "Data Science" y la función asignaturas retorne nombre = "Big Data"

1) Prueba a retornar el resultados de la clase libros y la función tipos

2) Prueba a retornar el resultados de la clase materias y la función asignaturas

3) Prueba a retornar el resultados de la clase materias y la función tipos
'''

class libros:
    def tipos():
        return "Data Science"

class materias:
    def asignaturas():
        return "Big Data"

def ejercicio_2():

    print(f"1) Clase libros (tipo): {libros.tipos()}")
    print(f"2) Clase materias (asignatura): {materias.asignaturas()} ")
    print("3) Da error")


#MENU Y MAIN

'''Menu'''
def pintar_menu():
    print("Opcion 1: Clase matemáticas")
    print("Opcion 2: Clase materias y libros")
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


        elif option == "-1":
            print("Gracias por usar este menú")
            break

        else:
            print("La opción introducida no es valida")
            input("Vuelve a intentarlo")


if __name__ == "__main__":
    main()

