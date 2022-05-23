from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

from forms import SignupForm

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

@app.route('/')
def Index():
    return render_template('formulario.html')

# routes
@app.route('/login/<idEmpresa>', methods=['POST'])
def Login(id):
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

    return render_template('sign_up_form.html', contact = data)

@app.route('/inicio')
def Inicio():
    return render_template('index.html')

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)