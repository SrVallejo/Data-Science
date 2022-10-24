from ast import Break
import pymongo
from datetime import datetime
from MenuClass import menu




def insertar_valores_iniciales(db):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dict_list = [
        {"nombre": "Pedro López", "edad": 25, "email": "pedro@fei.com", "nota": 5.2, "date": dt_string}, 
        {"nombre": "Julia García", "edad": 22, "email": "julia@fei.com", "nota": 7.3, "date": dt_string},
        {"nombre": "Amparo Mayoral", "edad": 28, "email": "amparo@fei.com", "nota": 8.4, "date": dt_string},
        {"nombre": "Juan Martinez", "edad": 30, "email": "juan@fei.com", "nota": 6.8, "date": dt_string},
    ]
    db.notas.insert_many(dict_list)
    print("Datos insertados")

def actualizar_nota_name (db):
    name = input("Introduce el nombre completo del alumno: ")
    try:
        nota = float(input("Introduce la nueva nota: "))
    
    except:
        print("Error: nota incorrecta")
        return False

    datos = db.notas.find({})
    for dato in datos:
        if dato["nombre"] == name:
            idMongo = dato["_id"]
            db.notas.update_one({"_id": idMongo}, {"$set":{"nota": nota}})
            print("Datos del alumno actualizados")
            return True

    print("Error: No se encuentra ese nombre en la base de datos")
    return False


def imprimir_datos(db):
    datos = db.notas.find({})
    vacia = True
    for dato in datos:
        vacia = False
        print(dato)

    if vacia: print("No hay datos")

def filtrar_datos(db):
    datos = db.notas.find({ "nota" : { "$gt" :  7, "$lt" : 7.5}})
    print("Valores de notas entre 7 y 7.5")
    for dato in datos:
        print(dato)


def eliminar_alumno(db):
    name = input("Introduce el nombre completo del alumno a eliminar: ")
    datos = db.notas.find({})
    for dato in datos:
        if dato["nombre"] == name:
            idMongo = dato["_id"]
            db.notas.delete_one({"_id": idMongo})
            print("Datos del alumno eliminados")
            return True

    print("Error: No se encuentra ese nombre en la base de datos")
    return False

def eliminar_datos(db):
    datos = db.notas.find({})
    for dato in datos:
        idMongo = dato["_id"]
        db.notas.delete_one({"_id": idMongo})
    print("Datos eliminados")

def main():

    ''' Conexión con la base de datos'''
    
    try:
        cliente = pymongo.MongoClient("localhost", 27017)
        db = cliente.actividad
    except pymongo.Error as e:
        print("Error en la conexión a la base de datos: %s" % str(e))
        return "Error"
    
    funciones =[
        insertar_valores_iniciales, actualizar_nota_name, imprimir_datos,
        filtrar_datos, eliminar_alumno, eliminar_datos
    ]

    opciones = [
        "Insertar valores iniciales","Actualizar nota", "Imprimir Datos",
        "Filtrar notas", "Eliminar Alumno", "Eliminar los datos"
    ]

    my_menu = menu(funciones,opciones)

    while True:
        function = my_menu.select_menu()
        if function == -1: break
        else: function(db)
        input("Continue...")
    input("Thanks for using this menu")


if __name__ == "__main__":
    main()