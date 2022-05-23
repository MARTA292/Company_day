from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

#rutas
@app.route('/')
def Inicio():
    return render_template('index.html')

@app.route('/inscripcion')
def inscripcion():
    return render_template('formulario.html')


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)