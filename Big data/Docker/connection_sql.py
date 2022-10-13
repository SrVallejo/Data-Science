import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(user = "LuisVallejo", password="Contrasenya",
                        host = "localhost", port=5433)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

def createDatabase(cur):

    try:
        cur.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier("test")))
    except psycopg2.Error as e:
        print("Error al crear la base de datos: %s" % str(e))


def createTable(cur):
    try:
        cur.execute("CREATE TABLE gatos(name varchar(80), age int, color text);")
    except psycopg2.Error as e:
        print("Error crear la tabla: %s" % str(e))

def insert(cur,name,age,color):
    try:
        cur.execute("INSERT INTO gatos VALUES(%s, %s, %s);", (name,age,color))
        #cur.execute("INSERT INTO notas VALUES(%s, %s, %s, %s);", ('Jose Perez', 215, 8.6, '07/07/2022'))
    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))
    
#createTable(cur)

insert(cur,"Maga","3","Siames")

cur.close()
conn.close()