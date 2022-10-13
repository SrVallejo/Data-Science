import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

'''Crear la base de datos:'''

def createDataBase():
    conn = psycopg2.connect(user = "LuisVallejo", password="Contrasenya",
                        host = "localhost", port=5433)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    try:
        cur.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier("actividad")))
    except psycopg2.Error as e:
        print("Error al crear la base de datos: %s" % str(e))


#createDataBase()

def create_table_edicion(cur):
    try:
        cur.execute("CREATE TABLE edicion(id SERIAL PRIMARY KEY, numero varchar(80) NOT NULL);")
    except psycopg2.Error as e:
        print("Error crear la tabla: %s" % str(e))

def create_table_notas(cur):
    try:
        query = "CREATE TABLE notas "
        query += "(id SERIAL PRIMARY KEY, "
        query += "name varchar(80) NOT NULL, "
        query += "edad int, "
        query += "notas real NOT NULL, "
        query += "ID_Edicion int references edicion(id) ON DELETE SET NULL);"
        cur.execute(query)
    except psycopg2.Error as e:
        print("Error crear la tabla: %s" % str(e))


def insert_edicion(cur, num):
    try:
        cur.execute("INSERT INTO edicion (numero) VALUES('{0}');".format(num))
    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))

def insert_notas(cur,name,edad,notas,id_ed):

    try:
        cur.execute("INSERT INTO notas (name,edad,notas,id_edicion) VALUES(%s, %s, %s,%s);", 
                    (name,edad,notas,id_ed))

    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))


def update_notas(cur,id,nota):

    try:
        cur.execute("UPDATE notas SET notas = {0} WHERE id = {1};".format(nota,id))

    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))
    
def main():
    ''' Conexión con la base de datos'''

    try:
        conn = psycopg2.connect(database = "actividad", user = "LuisVallejo", password="Contrasenya",
                            host = "localhost", port=5433)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error en la conexión a la base de datos: %s" % str(e))
        return "Error"
    
    '''Creación de tablas'''
    #create_table_edicion(cur)
    #create_table_notas(cur)

    '''Inserción de valores'''

    # ediciones = ['Uno','Dos','Tres']

    # for num in ediciones:
    #     insert_edicion(cur,num)

    # notas = [
    #     ["Isabel Maniega", 30, 5.6, 1],
    #     ["José Manuel Peña", 30, 7.8, 1],
    #     ["Pedro López", 25, 5.2, 2],
    #     ["Julia García", 22, 7.3, 1],
    #     ["Amparo Mayora", 28, 8.4, 3],
    #     ["Juan Martínez", 30, 6.8, 3],
    #     ["Fernando López", 35, 6.1, 2],
    #     ["María Castro", 41, 5.9, 3]
    # ]

    # for fila in notas:
    #     insert_notas(cur, fila[0],fila[1],fila[2],fila[3])

    '''Actualizar notas'''

    # update_notas(cur,3,6.4)
    # update_notas(cur,8,5.2)

    cur.close()
    conn.close()

    


if __name__ == "__main__":
    main()


