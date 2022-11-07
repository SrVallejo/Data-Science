import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("Big data\Predicción\Data Sets\Salary_Data.csv")

X = dataset.iloc[:,:1]
y = dataset.iloc[:,1:3]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)


from sklearn import linear_model

lr = linear_model.LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
print("La predicción del modelo tiene una precisión del:")
print(lr.score(X_train, y_train))


input("Ver grafico 1: ")
plt.scatter(X_train, y_train)
plt.title("Regresión Lineal Simple")
plt.xlabel("Años de experiencia")
plt.ylabel("Salario")
plt.show()

input("Ver grafico 2: ")
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, color='red', linewidth=3)
plt.title("Regresión Lineal Simple")
plt.xlabel("Años de experiencia")
plt.ylabel("Salario")
plt.show()