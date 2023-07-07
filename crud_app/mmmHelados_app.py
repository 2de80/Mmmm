import sqlite3
from flask import Flask, jsonify, request
import os

# Configurar la conexión a la base de datos SQLite
def get_db_connection(DATABASE):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
# Crear la tabla 'productos' si no existe
def create_table(table_name):
    conn = get_db_connection(DATABASE)
    cursor = conn.cursor()
    if table_name == "producto":
        cursor.execute(f'''
        CREATE TABLE `{table_name}` (
        `idProducto` int(4) NOT NULL,
        `idTipoProducto` int(4) NOT NULL,
        `nombre` varchar(20) DEFAULT NULL,
        `descripcion` varchar(200) DEFAULT NULL,
        `StockTotal` float DEFAULT NULL
        )
        ''')
    elif table_name == "tipodeproducto":
        cursor.execute(f"""
        CREATE TABLE `{table_name}` (
        `idTipoProducto` int(3) NOT NULL,
        `nombre` varchar(30) DEFAULT NULL,
        `descripcion` varchar(200) DEFAULT NULL
        )
        """)  
    elif table_name == "precioxcantidad":
        cursor.execute(f"""
        CREATE TABLE `{table_name}` (
        `idProducto` int(11) NOT NULL,
        `precio` float NOT NULL,
        `fecha` date NOT NULL,
        `cantidad` int(4) NOT NULL
        )
        """)
    conn.commit()
    cursor.close()
    conn.close()
# Verificar si la base de datos existe, si no, crearla y crear la tabla
def create_database(table_name):
    conn = sqlite3.connect(DATABASE) # crea la DB
    conn.close()
    create_table(table_name)
# También predermino los IDs por tipo de producto y sus respectivas descripciones
def insertIdTipoProducto():
    conn = get_db_connection(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
    """
    INSERT INTO `tipodeproducto` (`idTipoProducto`, `nombre`, `descripcion`) VALUES
    (1, 'Sabores', 'Representan el listado de sabores de helados de venta a granel.'),
    (2, 'Postres', 'Nuestros postres son helados y vienen listos para fraccionar en porciones. Rinden hasta 8 porciones.'),
    (3, 'Paletas', 'Barras heladas en palitos');
    """
    )
    conn.commit()
    cursor.close()
    conn.close()

# Implementar esta función para que se seobrescriban las claves y no se dupliquen con cada corrida (no funciona)
# def alterTable():
#     conn = get_db_connection(DATABASE)
#     cursor = conn.cursor()
#     cursor.execute("""
#     ALTER TABLE `tipodeproducto`
#     ADD PRIMARY KEY (`idTipoProducto`),
#     ADD UNIQUE KEY `idTipoProducto` (`idTipoProducto`);
#     """
#     )
#     conn.commit()
#     cursor.close()
#     conn.close()

# Crear la base de datos y la tabla si no existen
DATABASE    = 'inventario.db'
table_names = ["producto", "tipodeproducto", "precioxcantidad"]
if not os.path.exists(DATABASE):
    for table_name in table_names:
        create_database(table_name=table_name)
insertIdTipoProducto()
# alterTable()
"""
### testear creación de las tablas
import pandas as pd
cnx = sqlite3.connect('inventario.db') # Create your connection.
df  = pd.read_sql_query(f"SELECT * FROM `{table_names[0]}`", cnx) # setear indice en 0, 1 o 2
"""
print()
# -------------------------------------------------------------------
# Definimos la clase "TipoProducto"
# -------------------------------------------------------------------
class TipoProducto():
    def __init__(self
                 , idTipoProducto
                 , nombre
                 , descripcion):
        self.idTipoProducto     = idTipoProducto
        self.nombre             = nombre
        self.descripcion        = descripcion
# -------------------------------------------------------------------
# Definimos la clase "Producto"
# -------------------------------------------------------------------
class Producto():
    # Definimos el constructor e inicializamos los atributos de instancia
    def __init__(self
                 , idProducto
                 , idTipoProducto
                 , nombre 
                 , StockTotal
                 , descripcion):
        self.idProducto     = idProducto
        self.idTipoProducto = TipoProducto.idTipoProducto        
        self.nombre         = nombre
        self.descripcion    = descripcion        
        self.StockTotal     = StockTotal

    # Este método permite modificar un producto.
    def modificar(self
                  , nuevo_idProducto
                  , nuevo_idTipoProducto
                  , nuevo_nombre
                  , nuevo_descripcion
                  , nuevo_StockTotal):
        self.idProducto     = nuevo_idProducto # Modifica el id del proucto
        self.idTipoProducto = TipoProducto.idTipoProducto  # Modifica el id del producto
        self.nombre         = nuevo_nombre # Modifica el nombre
        self.descripcion    = nuevo_descripcion # Modifica la descripcion del producto
        self.StockTotal     = nuevo_StockTotal # Modifica el stock total
# -------------------------------------------------------------------
# Definimos la clase "PrecioPorCantidad"
# -------------------------------------------------------------------
class PrecioPorCantidad():
    def __init__(self
                , idProducto
                , precio
                , fecha
                , cantidad): 
        self.idProducto = Producto.idProducto
        self.precio     = precio
        self.fecha      = fecha
        self.cantidad   = cantidad
# -------------------------------------------------------------------
# Definimos la clase "Inventario"
# -------------------------------------------------------------------
class Inventario:
    def __init__(self):
        self.conexion   = get_db_connection() # Me conecto con la DB
        self.cursor     = self.conexion.cursor() # uso esa conexion para generar un cursor 
                                            # encargado de ejecutar sentencias SQL
    def agregar_producto(self
                        , idProducto
                        , idTipoProducto # viene de la clase TipoProducto
                        , nombre
                        , descripcion
                        , stockTotal):
        # Consulto si el producto existe, si es así retorno un msj
        producto_existente = self.consultar_producto(idProducto)
        if producto_existente:
            return jsonify({'message': 'Ya existe un producto con ese código.'}), 400
        nuevo_producto = Producto(idProducto
                                , idTipoProducto
                                , nombre
                                , descripcion
                                , stockTotal)
        self.cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?)",
                        ( idProducto
                        , idTipoProducto
                        , nombre
                        , descripcion
                        , stockTotal))
        self.conexion.commit()
        return jsonify({'message': 'Producto agregado correctamente.'}), 200
    def agregar_precioxcantidad(self
                                , idProducto
                                , precio
                                , fecha
                                , cantidad):
        precioxcantidad = PrecioPorCantidad(idProducto
                                            , precio
                                            , fecha
                                            , cantidad)
        self.cursor.execute("INSERT INTO precioxcantidad VALUES (?, ?, ?, ?)",
                        ( idProducto
                        , precio
                        , fecha
                        , cantidad))
        self.conexion.commit()
        return jsonify({'message': 'Precio x cantidad agregado correctamente.'}), 200