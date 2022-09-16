from MenuClass import menu
from ComplexNum import Complex

'''
Ejercicios

1) Crearemos un nuevo tipo llamado NumeroComplejo. 
Este tipo tiene un atributo x para la coordenada en x e y para la coordenada en y. 
Representa un número complejo de la forma (x, y).

2) Ahora defina dentro de la clase NumeroComplejo un función imprimir donde muestre los valores de x e y.

3) Define la función str para la clase NumeroComplejo para poder imprimir usando la función print.

4) definie una función que compara dos números complejos, 
ya que si dos objetos distintos tienen sus atributos iguales, no se consideran iguales.

5) Realiza un método que sume dos numeros complejos sin modificiar los objetos originales, 
ya que se retorna un nuevo numero NumeroComplejo.


'''

def numeros_complejos():
    c1 = Complex(3,2)
    c2 = Complex(1,-2)
    print(f"{c1} y {c2}")
    print(f"{c1} + {c2} = {c1+c2}")
    print(f"{c1} - {c2} = {c1-c2}")
    print(f"{c1} * {c2} = {c1*c2}")
    print(f"{c1} / {c2} = {c1/c2}")
    if c1 == c2: print("Son iguales")
    else: print("Son diferentes")

    print("\nSegunda comparación")
    c1 = Complex(10,14)
    c2 = Complex(10,14)
    print(f"{c1} y {c2}")
    if c1 == c2: print("Son iguales")
    else: print("Son diferentes")

#MENU
def main():
    funciones =[
        numeros_complejos
    ]

    opciones = [
        "Números Complejos"
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
