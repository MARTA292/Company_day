from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'ls-1f80ae49cefab7ccd21eb09611a8ee27e0b295af.cqlmvia8awqd.eu-west-3.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'nothing4free'
app.config['MYSQL_PASSWORD'] = '7^Px$eZ[xPtb8l?[UYfHPRIVMd&>+aus'
app.config['MYSQL_DB'] = 'cumpanyDay2'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    return render_template('login.html')

@app.route('/inicio')
def Index():
    return render_template('index.html')

#@app.route('/inscripcion_empresas')
#def inscripcion_empresas():
#    return render_template('inscripcion_empresas.html')

@app.route('/empresas')
def inscripcion_empresas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM empresas')
    data = cur.fetchall()
    cur.close()
    return render_template('tabla_empresas.html', empresas = data)

@app.route('/inscripcion', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        nombreEmpresa = request.form['name']
        personaContacto = request.form['person']
        email = request.form['email']
        phone = request.form['phone']
        direccionLinea1 = request.form['direccion']
        poblacion = request.form['poblacion']
        provincia = request.form['provincia']
        codigoPostal = request.form['codigo_postal']
        pais = request.form['pais']
        url = request.form['url']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO empresas (nombreEmpresa, personaContacto, email, phone, direccionLinea1, poblacion, provincia, codigoPostal, pais, url) VALUES (%s, %s, %s, %d, %s, %s, %s, %d, %s, %s)", (nombreEmpresa, personaContacto, email, phone, direccionLinea1, poblacion, provincia, codigoPostal, pais, url))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return render_template('inscripcion_empresas.html')

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)