from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'formulario'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('templates/tabla_empresas.html', empresa = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('formulario_empresa'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('templates/formulario_empresa.html', empresa = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)

''' 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/formulario_empresas/', methods=["GET", "POST"])
def formulario_empresas():
    if request.method == 'POST':
        name = request.form['nombre_empresa']
        persona = request.form['persona_contacto']
        mail = request.form['mail_contacto']
        tlf = request.form['tlf_contacto']
        submit = request.form['submit']
        if submit:
            #return redirect("tabla_empresas.html")
            render_template("tabla_empresas.html")
    return render_template("formulario_empresa.html")

if __name__ == '__main__':
    app.run()
'''
