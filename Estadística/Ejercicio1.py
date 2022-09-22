import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
import matplotlib.pyplot as plt
import os
clear = lambda: os.system("cls")

nums = [
    15, 16, 17, 
    16, 21, 22, 
    15, 16, 15, 
    17, 16, 22, 
    14, 13, 14, 
    14, 15, 15, 
    14, 15, 16, 
    10, 19, 15, 
    15, 22, 24, 
    25, 15, 16
]

clear()
df = pd.DataFrame({"Numeros":nums})
print(df)

input("\n1) Histograma 1 (Ancho de dos barras): ")
plt.hist(df.Numeros, bins=2,color="purple",histtype="bar",rwidth=0.75)
plt.grid(True)
plt.xlabel("Número")
plt.ylabel("Frecuencia")
plt.title("Histograma Ancho 2")
plt.show()

print(f"\n2) Moda: {df.Numeros.mode()}")

input("\n3) Histograma 2 (Ancho de 5 barras): ")
plt.hist(df.Numeros, bins=5,color="orange",histtype="bar",rwidth=0.75)
plt.grid(True)
plt.xlabel("Número")
plt.ylabel("Frecuencia")
plt.title("Histograma Ancho 5")
plt.show()

input("\n4) Histograma 3 (Ancho de 20 barras): ")
plt.hist(df.Numeros, bins=20,color="green",histtype="bar",rwidth=0.75)
plt.grid(True)
plt.xlabel("Número")
plt.ylabel("Frecuencia")
plt.title("Histograma Ancho 20")
plt.show()

input("\n5) Distribución: ")

columna = df.Numeros
mu, sigma = stats.norm.fit(columna)
x_hat = np.linspace(min(columna), max(columna), num=100)
y_hat = stats.norm.pdf(x_hat, mu, sigma)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x_hat, y_hat, linewidth=2, label="normal")
ax.plot(columna, np.full_like(columna, -0.01), "|k", markeredgewidth=1)
ax.set_title(f"Distribución")
ax.set_xlabel("Valores")
ax.set_ylabel("Densidad de probabilidad")
ax.legend()
plt.show()