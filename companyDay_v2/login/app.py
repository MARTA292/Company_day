from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
from sqlalchemy import  create_engine
from flask_wtf import csrf
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_mysqldb import MySQL
 
Base = declarative_base()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company.sqlite3'
app.config['SECRET_KEY'] = "random string"

app.config['MYSQL_HOST'] = 'ls-1f80ae49cefab7ccd21eb09611a8ee27e0b295af.cqlmvia8awqd.eu-west-3.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'nothing4free'
app.config['MYSQL_PASSWORD'] = '7^Px$eZ[xPtb8l?[UYfHPRIVMd&>+aus'
app.config['MYSQL_DB'] = 'cumpanyDay2'
mysql = MySQL(app)

#engine = create_engine("mysql+pymysql://nothing4free:7^Px$eZ[xPtb8l?[UYfHPRIVMd&>+aus@ls-1f80ae49cefab7ccd21eb09611a8ee27e0b295af.cqlmvia8awqd.eu-west-3.rds.amazonaws.com/cumpanyDay2")
#engine.connect()
#Session = sessionmaker(bind=engine)
#session = Session()

# class Empresa(Base):
#     __tablename__ = 'empresas'
#     ID_empresa = db.column(int(11), primary_key=True)
#     nombreEmpresa = db.column(db.String(50))
#     direccionLinea1 = db.column(db.String(50))
#     direccionLinea2 = db.column(db.String(50))
#     ciudad = db.column(db.String(50))
#     provincia = db.column(db.String(50))
#     codigoPostal = db.column(db.String(15))
#     pais = db.column(db.String(40))
#     url = db.column(db.String(40))
#     logoRoute = db.column(db.String(40))
#     consentPromo = db.column(db.Boolean)
#     recrouting = db.column(db.Boolean)
#     hashPass = db.column(db.String(60))
#     recovery = db.column(db.String(100))

db = SQLAlchemy(app)

class company(db.Model):
    name = db.Column('company_id', db.String(100), primary_key = True)
    pin = db.Column('pin',db.String(100))

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin

@app.route('/')
def show_all():
   return render_template('show_all.html', company=company.query.all())#company = engine.query.all() )

from forms import SignupForm, LoginForm

@app.route("/login/", methods=["GET", "POST"])
def show_login_form():
    form = LoginForm()
    csrf.generate_csrf()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        
        cur = mysql.connection.cursor()
        print("cur")
        cur.execute("SELECT nombreEmpresa FROM empresas WHERE nombreEmpresa LIKE '"+ name + "' AND hashPass LIKE '" + password + "'")
        mysql.connection.commit()
        print("ha hecho el select")
        if (cur.fetchone() is not None): 
            print("holi")
            cur.close()
            return redirect(url_for('show_all'))
        print("no lo ha encontrado")
        cur.close()
        flash('Record was successfully added')
        print("hola mundo")
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        #return redirect(url_for('show_all'))
    print(form.errors)
    return render_template("login.html", form=form)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    csrf.generate_csrf()
    if form.validate_on_submit():
        nombreEmpresa = form.name.data
        hashPass = form.password.data
        email = form.email.data 
        phone = form.phone.data
        direccionLinea1 = form.direccionLinea1.data
        direccionLinea2 = form.direccionLinea2.data
        poblacion = form.poblacion.data
        provincia = form.provincia.data
        codigoPostal = form.codigo_postal.data
        pais = form.pais.data
        url = form.url.data
        personaContacto =form.persona_contacto.data      
        #logo
        consentPromo = form.consentimiento.data
        recrouting = form.recrouting.data
        recovery = form.recovery.data
        CIF_empresa = form.cif.data

        cur = mysql.connection.cursor()
        print("cur")
        cur.execute("INSERT INTO empresas (nombreEmpresa, personaContacto, email, phone, direccionLinea1, direccionLinea2, poblacion, provincia, codigoPostal, pais, url, consentPromo, recrouting, hashPass, recovery, CIF_empresa) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(nombreEmpresa, personaContacto, email, phone, direccionLinea1, direccionLinea2, poblacion, provincia, codigoPostal, pais, url, consentPromo, recrouting, hashPass, recovery, CIF_empresa))
        mysql.connection.commit()
        print("ha hecho el select")
        if (cur.fetchone() is not None): 
            print("holi")
            return redirect(url_for('show_all'))
        print("no lo ha encontrado")

        # SELECT email FROM student WHERE name LIKE 'Amit%';
        # result = session.query(Empresa) \
        # .with_entities(Empresa.email) \
        # .filter(Empresa.name.like(name)).all()

        # VIEW THE ENTRIES IN THE RESULT
        # for r in result:
        #     print("\n", r.email)

        # student = company(name, password)
        # db.session.add(student)
        # db.session.commit()
        flash('Record was successfully added')
        print("hola mundo")
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        #return redirect(url_for('show_all'))
    print(form.errors)
    return render_template("sign_up_form.html", form=form)


if __name__ == '__main__':
    #db.create_all()
    app.run(debug = True)