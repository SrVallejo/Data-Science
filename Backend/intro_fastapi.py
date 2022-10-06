from fastapi import FastAPI, status, HTTPException
import pandas as pd
import json
import csv
import os
from pydantic import BaseModel


irisapp = FastAPI()
IRIS_ROUTE = r"../Data Sets/iris.csv"
@irisapp.get("/test/")
async def test_1():
    return "Bienvenido a FastAPI"

@irisapp.get("/iris/")
async def iris():
    # Crear el dataframe con la información de iris:
    df = pd.read_csv(IRIS_ROUTE)
    #print(df)
    # lo transformamos a json para poder gestionarlo desde el front:
    data = df.to_json(orient="index")
    # cargar la información con formato Json:
    data = json.loads(data)
    return data


# Modelo de datos:
class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str

@irisapp.post("/insertData/", status_code=201)
async def insertData(item: Iris):
# leemos el archivo iris.csv e
# insertar en la última línea los campos a insertar
    with open(IRIS_ROUTE, "a", newline="") as csvfile:
    # Nombres de los campos:
        fieldnames = ['sepal_length', 'sepal_width',
        'petal_length', 'petal_width', 'species']
        # escribimos el csv:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #insertamos los valores en la última fila:
        writer.writerow({
            "sepal_length": item.sepal_length,
            "sepal_width": item.sepal_width,
            "petal_length": item.petal_length,
            "petal_width": item.petal_width,
            "species": item.species
        })
    #retornamos los valores que comprende la ultima fila añadida
    return item

@irisapp.put("/UpdateData/")
async def insertData(item_id: int, item: Iris):
    df = pd.read_csv(IRIS_ROUTE)
    df.loc[df.index[item_id], "sepal_length"] = item.sepal_length
    df.loc[df.index[item_id], "sepal_width"] = item.sepal_width
    df.loc[df.index[item_id], "petal_length"] = item.petal_length
    df.loc[df.index[item_id], "petal_width"] = item.petal_width
    df.loc[df.index[item_id], "species"] = item.species
    df.to_csv(IRIS_ROUTE, index = False)

    return {"item_id":item_id, **item.dict()}

    

