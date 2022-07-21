import os
clear = lambda: os.system('cls')


'''Ejercicio 1: inversión cadena'''

def invers_string(s):
    new_string = ""
    for i in range(len(s)-1,-1,-1):
        new_string += s[i]
    return new_string

'''Ejercicio 2: Palindromo'''

def palindromo(s):
    s = s.upper()
    s = s.replace(" ","")
    start = 0
    end = len(s)-1
    while (start < end):
        if s[start]!=s[end]: return False
        start +=1
        end -=1
    return True

'''Ejercicio 3: Superposicion '''

def superposicion(s1,s2):

    for a in s1:
        for b in s2:
            if a == b: return True
    
    return False

'''Menu'''
def pintar_menu():
    print("Opcion 1: Inversion cadena")
    print("Opcion 2: Palindromo")
    print("Opcion 3: Superposición")
    print("Opcion -1: Salir")

def main():

    while True:
        clear()
        pintar_menu()
        option = input("Elige una opción: ")
        clear()

        if option == "1":
            s = invers_string(input("Pon el texto que quieres invertir: "))
            print(s)
            input("Continuar...")

        elif option == "2":
            s = input("Pon el texto que quieras comprobar: ")
            if palindromo(s): print(f"{s} es un palindromo")
            else: print(f"{s} no es un palindromo")
            input("Continuar...")

        elif option == "2":
            s = input("Pon el texto que quieras comprobar: ")
            if palindromo(s): print(f'"{s}" es un palindromo')
            else: print(f'"{s}" no es un palindromo')
            input("Continuar...")

        elif option == "3":
            s1 = input("Pon la primera frase: ")
            s2 = input("Pon la segunda frase: ")

            if superposicion(s1,s2): print("Ambas cadenas tienen elementos en común")
            else: print("Ambas cadenas no comparten ningún elemento")
            input("Continuar...")


        elif option == "-1":
            print("Gracias por usar este menú")
            break

        else:
            print("La opción introducida no es valida")
            input("Vuelve a intentarlo")


if __name__ == "__main__":
    main()