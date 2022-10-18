# Instalación de librería: pip install pymongo
import pymongo

# conexión a base de datos
cliente = pymongo.MongoClient("localhost", 27017)

db = cliente.luis

print(db)

def mostrar(db):
    datos = db.cat.find({})
    for dato in datos:
        print(dato)

def insertDocument(db):
    db.cat.insert_one({"name": "Maul", "age": 12})

#insertDocument(db)
#mostrar(db)

def actualizar(db):
    datos = db.cat.find({})
    for dato in datos:
        if dato["name"] == 'Maul':
            # print(dato["_id"])
            idMongo = dato["_id"]
            db.cat.update_one({"_id": idMongo}, {"$set":{"age": 78}})

#actualizar(db)

def delete(db):
    datos = db.cat.find({})
    for dato in datos:
        if dato["name"] == 'Maul':
            # print(dato["_id"])
            idMongo = dato["_id"]
            db.cat.delete_one({"_id": idMongo})

#delete(db)
#mostrar(db)