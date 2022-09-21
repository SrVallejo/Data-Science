import pandas as pd
import matplotlib.pyplot as plt
from MenuClass import menu


df = pd.DataFrame({"X": [10, 20, 30, 40, 50], "Y":[15, 5, 10, 8, 6]})
df2 = pd.DataFrame({"X": [10, 20, 30, 40, 50, 60, 70, 80],"Y": [10, 20, 10, 40, 20, 30, 20, 10]})

#Gráficos rápidos
def grafico_rapido():
    df.plot()
    plt.show()


def grafico_barras():
    df.plot(kind= "bar")
    plt.show()

def grafico_apilado():
    df.plot(kind="bar", stacked=True)
    plt.show()

def grafico_con_rejilla():
    df.plot(kind="bar", stacked=True, grid = True, title= "Gráfica de ejemplo con pandas")
    plt.show()

def grafico_value_counts():
    df2.Y.value_counts().plot(kind="bar",color=["green","blue","red","orange"])
    plt.show()


#Main
def main():
    funciones =[
        grafico_rapido, grafico_barras,grafico_apilado,
        grafico_con_rejilla,grafico_value_counts
    ]

    opciones = [
        "Gráfico rápido","Gráfico de barras", "Gráfico de barras apilado",
        "Gráfico con rejilla y titulo","Gráfico de frecuencia con Value Counts"
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

