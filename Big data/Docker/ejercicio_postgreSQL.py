import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from MenuClass import menu

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

'''         FUNCIONES QUE LANZAN QUERYS A LA BASE DE DATOS    '''

def create_table_edicion(cur):
    try:
        cur.execute("CREATE TABLE edicion(id SERIAL PRIMARY KEY, numero varchar(80) NOT NULL);")
        return True
    except psycopg2.Error as e:
        print("Error crear la tabla: %s" % str(e))
        return False

def create_table_notas(cur):
    try:
        query = "CREATE TABLE notas "
        query += "(id SERIAL PRIMARY KEY, "
        query += "name varchar(80) NOT NULL, "
        query += "edad int, "
        query += "notas real NOT NULL, "
        query += "ID_Edicion int references edicion(id) ON DELETE SET NULL);"
        cur.execute(query)
        return True
    except psycopg2.Error as e:
        print("Error crear la tabla: %s" % str(e))
        return False


def insert_edicion(cur, num):
    try:
        cur.execute("INSERT INTO edicion (numero) VALUES('{0}');".format(num))
        return True
    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))
        return False

def insert_notas(cur,name,edad,notas,id_ed):

    try:
        cur.execute("INSERT INTO notas (name,edad,notas,id_edicion) VALUES(%s, %s, %s,%s);", 
                    (name,edad,notas,id_ed))
        return True

    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))
        return False


def print_table(cur,table):
    try:
        cur.execute("SELECT * FROM {0}".format(table))
        table = cur.fetchall()
        for row in table:
            print(row)
        print("\n")
        return True
        
    except psycopg2.Error as e:
        print("Error seleccionar registros: %s" % str(e))
        return False


def update_table(cur,table,field, id, value):

    try:
        cur.execute("UPDATE {0} SET {1} = {2} WHERE id = {3};".format(table,field,value,id))
        return True

    except psycopg2.Error as e:
        print("Error crear registro: %s" % str(e))
        return False

def select_query(cur,table,condition):
    try:
        cur.execute("SELECT * FROM {0} WHERE {1}".format(table,condition))
        query = cur.fetchall()
        for row in query:
            print(row)
        return True
    except psycopg2.Error as e:
        print("Error al realizar la consulta: %s" % str(e))
        return False
    
def delete_row(cur,table,id):
    try:
        cur.execute("DELETE FROM {0} WHERE id = {1}".format(table,id))
        return True

    except psycopg2.Error as e:
        print("Error eliminar registro: %s" % str(e))
        return False



def drop_tables(cur,table):
    try:
        cur.execute("DROP TABLE {0}".format(table))
        return True

    except psycopg2.Error as e:
        print("Error eliminar tabla: %s" % str(e))
        return False



'''         FUNCIONES DEL MENÚ          '''

'''Creación de tablas'''

def create_tables(cur):
    if create_table_edicion(cur) & create_table_notas(cur):
        print("Tablas creadas correctamente")
    


'''Inserción de valores'''
def insertar_valores_iniciales(cur):
    error = False
    ediciones = ['Uno','Dos','Tres']

    for num in ediciones:
        if not insert_edicion(cur,num):
            print ("Error edicion")
            error = True
        

    notas = [
        ["Isabel Maniega", 30, 5.6, 1],
        ["José Manuel Peña", 30, 7.8, 1],
        ["Pedro López", 25, 5.2, 2],
        ["Julia García", 22, 7.3, 1],
        ["Amparo Mayora", 28, 8.4, 3],
        ["Juan Martínez", 30, 6.8, 3],
        ["Fernando López", 35, 6.1, 2],
        ["María Castro", 41, 5.9, 3]
    ]

    for fila in notas:
        if(not insert_notas(cur, fila[0],fila[1],fila[2],fila[3])):
            print("Error notas")
            error = True
    
    if not error: print("Todos los registros ingresados correctamente")

    
''' Pintar tablas'''
def imprimir_tablas(cur):
    print_table(cur,"edicion")
    print_table(cur,"notas") 


'''Actualizar nota con id'''

def actualizar_nota_id(cur):
    try:
        id = int(input("Introduzca el id del alummo que quiere modificar: "))
        nota = float(input("Introduzca la nueva nota: "))
        if (update_table(cur,"notas","notas",id,nota)): print("Nota actualizada correctamente")

    except:
        print("Error: id o nota incorrectos")


'''Querys'''

def consultas_notas(cur):
    condition = input("SELECT FROM notas WHERE ")
    select_query(cur,"notas",condition)
    
def ejemplo_join(cur):
    try:
        query = "SELECT * FROM notas INNER JOIN edicion ON edicion.id=notas.ID_Edicion "
        query += "WHERE numero = 'Dos'"
        cur.execute(query)
        query = cur.fetchall()
        for row in query:
            print(row)
        return True
    except psycopg2.Error as e:
        print("Error al realizar la consulta: %s" % str(e))
        return False

'''Eliminar Registro'''
def eliminar_alumno(cur):
    try:
        id = int(input("Introduzca el id del alummo que quiere eliminar: "))
        if delete_row(cur,"notas",id): print("Alumno borrado correctamente")
    except:
        print("Error: id incorrecto")



'''Eliminar las tablas'''

def eliminar_tablas(cur):
    if drop_tables(cur,"notas") & drop_tables(cur,"edicion"): print("Tablas eliminadas correctamente")



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
    
    funciones =[
        create_tables, insertar_valores_iniciales, actualizar_nota_id,
        consultas_notas, ejemplo_join, imprimir_tablas, 
        eliminar_alumno, eliminar_tablas,
    ]

    opciones = [
        "Crear tablas edición y notas","Insertar Valores Iniciales","Actualizar nota alumno",
        "Consultas Notas", "Ejemplo de JOIN", "Imprimir Tablas",
        "Eliminar Alumno", "Eliminar las tablas"
    ]

    my_menu = menu(funciones,opciones)

    while True:
        function = my_menu.select_menu()
        if function == -1: break
        else: function(cur)
        input("Continue...")
    input("Thanks for using this menu")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()


