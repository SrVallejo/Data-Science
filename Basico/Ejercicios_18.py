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

'''Ejercicio 4: Función vocales'''

def vocal(a):
    return a.lower() in ['a','e','i','o','u','á','é','í','ó','ú']

'''Ejercicio 5: Sumatorio y multiplicación'''

def sumatorio(lista):
    x = 0
    for num in lista:
        x+= num
    return x

def multi_lista(lista):
    x = 1
    for num in lista:
        x*= num
    return x

''' Función main'''

def main():
    print("Primer ejercicio")
    x = int(input("Introduce el primer digito a comparar: "))
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

    print("Cuarto ejercicio")
    a = input("Introduce la letra que quieras comprobar: ")
    if vocal(a): print(f"{a} es una vocal")
    else: print(f"{a} es una consonante")

    print(f"Quinto ejercicio")
    
    lista = [1,2,3,4]
    print(f"La suma de los elementos de la lista da {sumatorio(lista)}")
    print(f"La multiplicación de los elementos de la lista da {multi_lista(lista)}")


if __name__ == "__main__":
    main()