from fastapi import FastAPI, status, HTTPException
import pandas as pd
import json
import csv
import os
from pydantic import BaseModel


irisapp = FastAPI()

@irisapp.get("/test/")
async def test_1():
    return "Bienvenido a FastAPI"

@irisapp.get("/iris/")
async def iris():
    # Crear el dataframe con la información de iris:
    df = pd.read_csv(r"../Data Sets/iris.csv")
    #print(df)
    # lo transformamos a json para poder gestionarlo desde el front:
    data = df.to_json(orient="index")
    # cargar la información con formato Json:
    data = json.loads(data)
    return data