import sqlite3
import os
from flask import Flask, send_from_directory, render_template, request, redirect, url_for
# import threading
# from werkzeug.local import LocalProxy

# Configurar la conexión a la base de datos SQLite
def get_db_connection(DATABASE):
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    # conn.row_factory = sqlite3.Row
    return conn

    # conn = getattr(threading.local(), 'conn', None)
    # if conn is None:
    #     conn = sqlite3.connect(DATABASE)
    #     conn.row_factory = sqlite3.Row
    #     threading.local().conn = conn
    # return conn
    # if not hasattr(Flask, 'db'):
    #     Flask.db = LocalProxy(sqlite3.connect(DATABASE))
    #     Flask.db.row_factory = sqlite3.Row
    #     # create_tables()  # Crear las tablas si no existen
    # return Flask.db
    # if not hasattr(threading.current_thread(), 'db_connection'):
    #     threading.current_thread().db_connection = sqlite3.connect(DATABASE)
    #     threading.current_thread().db_connection.row_factory = sqlite3.Row
    #     # create_tables()  # Crear las tablas si no existen
    # return threading.current_thread().db_connection
    
    # if 'db_connection' not in g:
    #     g.db_connection = sqlite3.connect(DATABASE)
    #     g.db_connection.row_factory = sqlite3.Row
    # return g.db_connection


# Crear la tablas para cada tipo de productos si no existe
def create_table(table_name):
    # with app.app_context():
    conn = get_db_connection(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        imagen VARCHAR(255)
    );
    ''')
    conn.commit()
    cursor.close()
    conn.close()
# Verificar si la base de datos existe, si no, crearla y crear la tabla
def create_database(table_name):
    conn = sqlite3.connect(DATABASE) # crea la DB
    conn.close()
    create_table(table_name)
# Crear la base de datos y la tabla si no existen
DATABASE    = 'carrusel.db'
table_names = ["sabores", "postres", "paletas"]
if not os.path.exists(DATABASE):
    for table_name in table_names:
        create_database(table_name=table_name)
# if not os.path.exists(DATABASE):
#     for table_name in table_names:
#         create_database(table_name=table_name)
"""
### testear creación de las tablas
import pandas as pd
cnx = sqlite3.connect('carrusel.db') # Create your connection.
df  = pd.read_sql_query(f"SELECT * FROM `{table_names[0]}`", cnx) # setear indice en 0, 1 o 2
"""
class CarruselImagenes:
    def __init__(self, tipo_producto, db_connection):
        self.tipo_producto = tipo_producto
        self.db_connection = db_connection


    def obtener_productos(self):
        try:
            cursor = self.db_connection.cursor()
            consulta = f"SELECT * FROM {self.tipo_producto}"
            cursor.execute(consulta)
            productos = cursor.fetchall()
            cursor.close()
            return productos
        except self.db_connection.Error as e:
            print(f"Error al obtener los productos: {e}")
            return []

    def agregar_producto(self, id_producto, nombre, archivo):
    # def agregar_producto(self, nombre, archivo):
        try:
            cursor = self.db_connection.cursor()
            # consulta = f"INSERT INTO {self.tipo_producto} (id, nombre, imagen) VALUES {id_producto}, {nombre}, {archivo}" #(?, ?, ?)"
            consulta = f"INSERT INTO {self.tipo_producto} (id, nombre, imagen) VALUES (?, ?, ?)"
            cursor.execute(consulta, (id_producto, nombre, archivo.filename))
            # consulta = f"INSERT INTO {self.tipo_producto} (nombre, imagen) VALUES (?, ?)"
            # cursor.execute(consulta, (nombre, archivo.filename))
            self.db_connection.commit()
            cursor.close()
            return True
        except self.db_connection.Error as e:
            print(f"Error al agregar el producto: {e}")
            return False

    def eliminar_producto(self, id_producto):
        try:
            cursor = self.db_connection.cursor()
            consulta = f"DELETE FROM {self.tipo_producto} WHERE id = {id_producto}" # uso format string en vez de ?
            cursor.execute(consulta, (id_producto,))
            self.db_connection.commit()
            cursor.close()
            return True
        except self.db_connection.Error as e:
            print(f"Error al eliminar el producto: {e}")
            return False


app = Flask(__name__, static_url_path='/static')
# Configuración de la base de datos
db_connection = get_db_connection(DATABASE)

@app.route('/')
def index():
    return render_template('index.html')#, sabores=sabores, postres=postres, paletas=paletas)

@app.route('/static/uploads/<path:filename>')
def get_uploaded_file(filename):
    return send_from_directory('uploads', filename)

@app.route('/sabores')
def sabores():
    carrusel_sabores = CarruselImagenes('sabores', db_connection)
    sabores = carrusel_sabores.obtener_productos()
    # Verificar los datos de la variable postres
    print("Datos de sabores:", sabores)
    return render_template('index.html', titulo='Sabores de Helados', productos=sabores)

@app.route('/postres')
def postres():
    carrusel_postres = CarruselImagenes('postres', db_connection)
    postres = carrusel_postres.obtener_productos()
    # Verificar los datos de la variable postres
    print("Datos de postres:", postres)
    return render_template('index.html', titulo='Postres', productos=postres)

@app.route('/paletas')
def paletas():
    carrusel_paletas = CarruselImagenes('paletas', db_connection)
    paletas = carrusel_paletas.obtener_productos()
    # Verificar los datos de la variable postres
    print("Datos de paletas:", paletas)
    return render_template('index.html', titulo='Paletas', productos=paletas)

@app.route('/producto/agregar_producto', methods=['POST'])
def agregar_producto():
    tipo_producto = request.form['tipo_producto']
    id_producto = request.form['id_producto']
    nombre = request.form['nombre']
    archivo = request.files['imagen']
    # archivo.save('static/uploads/' + archivo.filename)
    archivo.save(os.path.join('static/uploads', archivo.filename))
    
    carrusel = CarruselImagenes(tipo_producto, db_connection)
    if carrusel.agregar_producto(id_producto, nombre, archivo):
    # if carrusel.agregar_producto(nombre, archivo):
        return redirect(url_for(tipo_producto))
    else:
        return "Error al agregar el producto"

@app.route('/producto/eliminar/<int:id_producto>', methods=['POST'])
def eliminar_producto(id_producto):
    tipo_producto = request.form['tipo_producto']
    
    carrusel = CarruselImagenes(tipo_producto, db_connection)
    if carrusel.eliminar_producto(id_producto):
        return redirect(url_for(tipo_producto))
    else:
        return "Error al eliminar el producto"
app.template_folder = 'templates'
app.static_folder = 'static'
if __name__ == '__main__':
    # with app.app_context():
    #     if not os.path.exists(DATABASE):
    #         for table_name in table_names:
    #             create_database(table_name=table_name)
    app.run()