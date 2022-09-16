from MenuClass import menu
from ClassComplexNum import Complex
from ClassHuman import Human

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
    print("Comparación !=")
    if c1 != c2: print("Son diferentes")
    else: print("Son iguales")

    print("\nComparación ==")
    c1 = Complex(10,14)
    c2 = Complex(10,14)
    print(f"{c1} y {c2}")
    if c1 == c2: print("Son iguales")
    else: print("Son diferentes")

'''
6) Crea una clase persona. Sus atributos deben ser su nombre y su edad. Además crea un método cumpleaños, 
que aumente en 1 la edad de la persona.

7) Para la clase anterior definir el método str. Debe retornar al menos el nombre de la persona.

8) Extender la clase persona agregando un atributo saldo y un método transferencia(self, persona2, monto). 
El saldo representa el dinero que tiene la persona. 
El método transferencia hace que la Persona que llama el método le transfiera la cantidad monto al objeto persona2. 
Si no tiene el dinero suficiente no se ejecuta la acción.
'''

def persona_transferencia():
    persona1 = Human("Luis",31)
    persona2 = Human("Marina",28)

    print(f"Prueba imprimir:\n{persona1} y {persona2}")
    print("Cumpleaños:")
    persona1.aniversary()
    print(persona1)

    print(f"\nTransferencia:")
    persona1.add_money(100)
    persona1.check_money()
    persona2.check_money()
    persona1.transference(persona2,30)
    persona1.check_money()
    persona2.check_money()

    

#MENU
def main():
    funciones =[
        numeros_complejos,persona_transferencia
    ]

    opciones = [
        "Números Complejos","Clase Personas y transferencia"
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
