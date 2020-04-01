from flask import Flask, render_template, request,  redirect, url_for, flash, session
import pymysql
import mysql.connector

"""from flask_mysqldb import MySQL"""
from flask_login import LoginManager

""" RUTAS """
app=Flask(__name__)


conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="que_como")

"""for fila in cursor1:"""




@app.route("/")
def home():
    return render_template('home.html')

@app.route("/buscar-receta")
def buscar_receta():
    return render_template('buscar_receta.html')

@app.route("/cambiar-premium")
def cambiar_premuim():
    return render_template('cambiar_premium.html')

@app.route("/contactanos-usuarios")
def contactanos_usuarios():
    return render_template('contactanos_usuarios.html')

@app.route("/contactanos")
def contactanos():
    return render_template('contactanos.html')

@app.route("/crear-receta")
def crear_receta():
    return render_template('crear_receta.html')

""" Conexion cargar registro receta a BD """
"""mysql= MySQL(app)"""
@app.route("/cargar-registro-receta", methods=['POST'])
def cargar_registro_receta():
    if request.method == 'POST':
       recipe_name = request.form['recipe_name']
       total_time = request.form['total_time']
       cook_time = request.form['cook_time']
       cooking_method = request.form['cooking_method']
       nutrition = request.form['nutrition']
       recipe_category = request.form['recipe_category']
       suitable_for_diet = request.form['suitable_for_diet']
       yields = request.form['yields']
       estimated_cost = request.form['estimated_cost']
       recipe_ingredients = request.form['recipe_ingredients']
       recipe_instructions = request.form['recipe_instructions']
       comments= request.form['comments']
       author= request.form['author']
       cursor1 = conexion1.cursor()
       cursor1.execute (' INSERT INTO receta (recipe_name, total_time, cook_time, cooking_method, nutrition, recipe_category, suitable_for_diet, yields, estimated_cost, recipe_ingredients, recipe_instructions, comments, author) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (recipe_name, total_time, cook_time, cooking_method, nutrition, recipe_category, suitable_for_diet, yields, estimated_cost, recipe_ingredients, recipe_instructions, comments, author))
       conexion1.commit()
       return render_template('crear_receta.html')


@app.route("/home-cocinero")
def home_cocinero():
    return render_template('home_cocinero.html')

@app.route("/home-nutricionista")
def home_nutricionista():
    return render_template('home_nutricionista.html')

@app.route("/home-usuario")
def home_usuario(filtro='general'):
    filtro=request.args.get('filtro', filtro)

    cursor1=conexion1.cursor()
    cursor1.execute("SELECT * FROM menu where filtro='{}'".format(filtro))
    menu_data = cursor1.fetchall() 

    cursor1=conexion1.cursor()
    cursor1.execute("SELECT filtro FROM menu")
    menu_data_filtro = cursor1.fetchall() 

    return render_template('home_usuario.html', menu = menu_data, filtro = menu_data_filtro)
    
    

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/mensajeria")
def mensajeria():
    return render_template('mensajeria.html')

@app.route("/olvido-contraseña")
def olvido_contraseña():
    return render_template('olvido_contraseña.html')

@app.route("/quienes-somos")
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route("/preguntas-frecuentes")
def preguntas_frecuentes():
    return render_template('preguntas_frecuentes.html')

@app.route("/registro")
def registro():
    return render_template('registro.html')

@app.route("/guardar_registro", methods=['POST'])
def guardar_registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        celular = request.form['celular']
        fna = request.form['fna']
        
        altura = request.form['altura']
        peso = request.form['peso']
        email = request.form['email']
        cursor1 = conexion1.cursor()
        cursor1.execute('INSERT INTO usuarios (nombre, direccion, telefono, fecha_nacimiento, mail) VALUES (%s,%s, %s, %s, %s)', (nombre, direccion, celular, fna, email ))
        conexion1.commit()     
        return redirect(url_for('home_usuario'))

@app.route('/processLogin', methods=['GET', 'POST'])
def processLogin():
       missing = []
       fields = ['email', 'passwd', 'login_submit']
       for field in fields:
              value = request.form.get(field, None)
              if value is None:
                  missing.append(field)
       if missing:
              return "Warning: Some fields are missing"

       return redirect(url_for('home_usuario'))      


@app.route("/terminos-condiciones")
def terminos_condiciones():
    return render_template('terminos_condiciones.html')





if __name__=="__main__":
    app.run(debug=True)



