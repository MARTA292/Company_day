from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
from sqlalchemy import  create_engine
from flask_wtf import csrf
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
 
Base = declarative_base()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company.sqlite3'
app.config['SECRET_KEY'] = "random string"

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

from forms import SignupForm

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    csrf.generate_csrf()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # SELECT email FROM student WHERE name LIKE 'Amit%';
        # result = session.query(Empresa) \
        # .with_entities(Empresa.email) \
        # .filter(Empresa.name.like(name)).all()

        # VIEW THE ENTRIES IN THE RESULT
        # for r in result:
        #     print("\n", r.email)

        student = company(name, password)
        db.session.add(student)
        db.session.commit()
        flash('Record was successfully added')
        print("hola mundo")
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('show_all'))
    print(form.errors)
    return render_template("sign_up_form.html", form=form)

if __name__ == '__main__':
    #db.create_all()
    app.run(debug = True)