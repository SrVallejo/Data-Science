import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
import matplotlib.pyplot as plt
import os
clear = lambda: os.system('cls')


def estadisticos_mes(df,mes:str):
    media = df[mes].mean()
    mediana = df[mes].median()
    moda = df[mes].mode()
    print(f"Parametros estadisticos de los beneficios de {mes}")
    print(f"Media: {media}\nMediana: {mediana}\nModa: {moda}\n")
    input("Ver grafico...")

    columna = df[mes]
    mu, sigma = stats.norm.fit(columna)
    x_hat = np.linspace(min(columna), max(columna), num=100)
    y_hat = stats.norm.pdf(x_hat, mu, sigma)

    # Gráfico
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x_hat, y_hat, linewidth=2, label="normal")
    ax.plot(columna, np.full_like(columna, -0.01), "|k", markeredgewidth=1)
    ax.set_title(f"Distribución {mes}")
    ax.set_xlabel("Valores")
    ax.set_ylabel("Densidad de probabilidad")
    ax.legend()
    plt.show()

df_income = pd.DataFrame({"Enero": [2500, 2650, 2740, 2500],
                     "Febrero": [3000, 3225, 3000, 3100],
                     "Marzo": [2900, 2700, 3400, 2700]})

print(df_income)
mes = input("\nElige un mes para ver los beneficios: ")
clear()
estadisticos_mes(df_income,mes)