'''Ejercicio 1: Funcion maxima 2 números'''

def num_max_2(x,y):
    if x>y: return x
    else: return y

'''Ejercicio 2: Función max 3 números'''

def num_max_3(x,y,z):
    if x > y and x > z: return x
    elif y > z: return y
    else: return z

'''Ejercicio 3: Funcion longitud'''

def longitud (l):
    i = 0
    while (True):
        try:
            l[i]
            i += 1
        except:
            return i+1

''' Función main'''

def main():
    print("Primer ejercicio")
    x = int(input("Introduce el primer digito Sa comparar: "))
    y = int(input("Introduce el segundo: "))

    print(f"El mayor de los dos es: {num_max_2(x,y)}")

    print("Segundo ejercicio")
    x = int(input("Introduce el primer digito a comparar: "))
    y = int(input("Introduce el segundo: "))
    z = int(input("Introduce el tercero: "))

    print(f"El mayor de los tres es: {num_max_3(x,y,z)}")

    print(f"Tercer ejercicio")
    
    lista = [0,19,18,1,-1]
    print(f"La lista tiene {longitud(lista)} elementos")


if __name__ == "__main__":
    main()