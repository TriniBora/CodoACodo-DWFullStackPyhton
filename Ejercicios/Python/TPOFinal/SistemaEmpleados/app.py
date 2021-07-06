# incluimos todo lo necesario para hacer el renderizado de
# template y uso de flask

from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL

app=Flask(__name__)  # aca creamos la aplicacion (objeto de Flask)

mysql = MySQL()#instanciamos un objeto de la clase MySql

#configuramos el objeto de flask
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER']  ='root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_Db']='sistema'
mysql.init_app(app)


@app.route('/')     # cuando el usuario escriba / se va a buscar el archivo index.html
def index():
    sql="INSERT INTO `sistema`.`empleados` (`nombre`, `correo`,`foto`) VALUES ('juan', 'juan@gmail.com','foto.jpg');"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template('empleados/index.html')

@app.route('/create')
def create():
    return render_template('empleados/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']

    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`,`foto`) VALUES (NULL, %s, %s, %s);"

    datos=(_nombre, _correo, _foto.filename)

    conn =mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return render_template('empleados/index.html')

if __name__=='__main__':    # para que python pueda interpretar  como
# empezar a correr la aplicacion
    app.run(debug=True)     # va ejecurar la aplicacion y en modo debug