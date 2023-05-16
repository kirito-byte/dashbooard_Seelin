import pandas as pd


def guardar_datos_excel(file):
    f = open("application/Datos Almacenados/"+file.filename+".txt","w")
    data = pd.read_excel(file,usecols=['Nro','Nombre Empresa','Nombre Sistema','Nombre Unidad','Nombre Elementos','N1','N2','N3','fecha inicio','fecha fin'])
    #print(data.columns,data.shape,data.index,data.values)
    #print(data.shape,type(data.shape))
    valores = data.values
    #a=str(valores[0][9])
    #print(a[:10])
    for i in valores:
        k=''
        for j in range(8):
            k+=str(i[j])+',' 
        f1=str(i[8]) 
        k+=f1[:10]+','
        f2=str(i[9])   
        k+=f2[:10]
        f.write(k+'\n')
    f.close()
    return data
'''
def mostrar_alumno()111:
    conexion = db.obtener_conexion()
    alumnos = []
    with conexion.cursor() as cursor:
        cursor.execute("Select * from alumno")
        alumnos = cursor.fetchall()
    conexion.close()
    return alumnos

def nuevo_alumno(id_alum,tutor_1,celular_1,tutor_2,celular_2):
    conexion = db.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO alumno(id_Alum,nombre_tutor_1,celular_tutor_1,nombre_tutor_2,celular_tutor_2) VALUES (%s, %s, %s, %s, %s)",
                       (id_alum,tutor_1,celular_1,tutor_2,celular_2))
        conexion.commit()
        conexion.close()

def eliminar_alumno(id_alumno):
    conexion = db.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM alumno WHERE id_Alum = %s",(id_alumno))
    conexion.commit()
    conexion.close()

def mostrar_alumno_por_id(id_alumno):
    conexion = db.obtener_conexion()
    alumno = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_Alum, nombre_tutor_1,celular_tutor_1,nombre_tutor_2,celular_tutor_2 FROM alumno WHERE id_Alum = %s",
                       (id_alumno))
        alumno = cursor.fetchone()
    conexion.close()
    return alumno

def actualizar_alumno(id_alum,tutor_1,celular_1,tutor_2,celular_2):
    conexion = db.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE alumno SET nombre_tutor_1 = %s, celular_tutor_1 = %s, nombre_tutor_2 = %s, celular_tutor_2 = %s WHERE id_Alum = %s",
                       (tutor_1,celular_1,tutor_2,celular_2,id_alum))
    conexion.commit()
    conexion.close()

def docentes_ciudad(ciudad):
    conexion = db.obtener_conexion()
    alumno = 0
    with conexion.cursor() as cursor:
        cursor.execute("SELECT docente_x_ciudad(%s);", (ciudad))
        alumno = cursor.fetchone()
    conexion.close()
    return alumno

def  doc_est_gen(genero):
    conexion = db.obtener_conexion()
    auxiliar=0
    with conexion.cursor() as cursor:
        cursor.execute("CALL `doc_est_x_genero`(%s, @p0, @p1);",
                       (genero))
        cursor.execute("SELECT @p0, @p1;")
        auxiliar = cursor.fetchall()
    conexion.close()
    return auxiliar[0][0], auxiliar[0][1]
'''