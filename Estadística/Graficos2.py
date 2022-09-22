import pandas as pd
import matplotlib.pyplot as plt
from MenuClass import menu


df = pd.DataFrame(
    {"x": 
        [1,32,4,23,40,2,2,27,6,18,49,67,46,7,
         20,24,35,33,40,80,26,85,77,11,92,24],
     "y": 
        [31,10,85,25,4,83,32,43,66,18,93,6,42,
         27,21,42,53,32,85,32,42,58,67,17,4,5]})

#Gráficos rápidos
def histograma():
    plt.hist(df.y)
    plt.grid(True)
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de edades 1")
    plt.show()


def histograma_2():
    plt.hist(df.y, bins=10,color="green",histtype="bar",rwidth= 0.25)
    plt.grid(True)
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de edades 2")
    plt.show()

def histograma_3():
    plt.hist(df.y, bins=10,color="purple",histtype="bar",rwidth= 0.75)
    plt.grid(True)
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de edades 3")
    plt.show()

def histograma_4():
    plt.hist(df.y, bins=3,color="red",histtype="bar",rwidth= 0.75)
    plt.grid(True)
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de edades 4")
    plt.show()


def scatter():
    plt.scatter(df.x, df.y)
    plt.show()

def scatter_2():
    x = [
        1, 2, 3, 
        4, 5, 6, 
        7, 8, 9, 
        10
    ]

    y = [
        1, 4, 9, 
        15, 20, 34, 
        62, 78, 84, 
        103
    ]

    plt.scatter(x, y, label="Peatones",color="black",marker="X", s=450)
    plt.xlabel("Accidentes")
    plt.ylabel("Edad")
    plt.title("Accidentes de tráfico en calle montalban")
    plt.legend()
    plt.grid(True)
    plt.show()





#Main
def main():
    funciones =[
        histograma,histograma_2,histograma_3,
        histograma_4,scatter,scatter_2
    ]

    opciones = [
        "Histograma sencillo","Histograma barras finas","Histograma barras más gruesas",
        "Histograma menos divisiones","Gráfico de dispersión sencillo", "Gráfico de dispersión completo"
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

