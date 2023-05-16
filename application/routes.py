from application import app
from flask import render_template, url_for, redirect,flash, get_flashed_messages,request
from application import Controladores
import pandas as pd



@app.route('/')
def index():
    return render_template('index.html')

# Root endpoint
@app.get('/')
def upload():
    return render_template('upload-excel.html')
 
#Ver el PDF version chapi muy chapi
#Nota desinstalar openpyxl
@app.post('/view')
def view():
 
    # Read the File using Flask request
    file = request.files['file']
    # save file in local directory
    file.save(file.filename)
 
    # Parse the data as a Pandas DataFrame type
    data = pd.read_excel(file)
 
    # Return HTML snippet that will render the table
    return data.to_html()

@app.post('/guardar_datos')
def guardar_datos(): 
    file = request.files['file']
    data = Controladores.guardar_datos_excel(file)
    context = {
        'mensaje' : "Se guradaron los datos",
        'data' : data
    } 
    
    data = data
    return render_template('index.html',**context)

'''



@app.route('/alumno')
def alumno():
    alumnos = Controladores.mostrar_alumno()
    return render_template('alumno.html',alumnos = alumnos)

@app.route('/grafica')
def grafica():
    docentes_la_paz = Controladores.docentes_ciudad('La Paz')
    docentes_el_alto = Controladores.docentes_ciudad('El Alto')
    doc_mas, est_mas = Controladores.doc_est_gen('Masculino')
    doc_fem, est_fem = Controladores.doc_est_gen('Femenino')
    context = {
        'docentes_la_paz' : docentes_la_paz,
        'docentes_el_alto' : docentes_el_alto,
        'doc_mas' : doc_mas,
        'est_mas' : est_mas,
        'doc_fem' : doc_fem,
        'est_fem' : est_fem
    } 
    return render_template('graficas.html', **context)


@app.route('/nuevo_alumno')
def nuevo_alumno():
    return render_template('nuevo_alumno.html')

@app.route('/guardar_alumno', methods=["POST"])
def guardar_alumno():
    id_alum = request.form['id_alum']
    tutor_1 = request.form['tutor_1']
    celular_1 = request.form['celular_1']
    tutor_2 = request.form['tutor_2']
    celular_2 = request.form['celular_2']
    Controladores.nuevo_alumno(id_alum,tutor_1,celular_1,tutor_2,celular_2)
    return redirect('/alumno')

@app.route("/editar_alumno/<int:id>")
def editar_alumno(id):
    al = Controladores.mostrar_alumno_por_id(id)
    return render_template("editar_alumno.html", al=al) 

@app.route('/actualizar_alumno',methods =["POST"])
def actualizar_alumno():
    id_alum = request.form['id_alum']
    tutor_1 = request.form['tutor_1']
    celular_1 = request.form['celular_1']
    tutor_2 = request.form['tutor_2']
    celular_2 = request.form['celular_2']
    Controladores.actualizar_alumno(id_alum,tutor_1,celular_1,tutor_2,celular_2)
    return redirect("/alumno")


@app.route("/eliminar_alumno", methods=["POST"])
def eliminar_alumno():
    Controladores.eliminar_alumno(request.form["id"])
    return redirect("/alumno")
    '''
