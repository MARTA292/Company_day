from django.forms import BooleanField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TelField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    name = StringField('Nombre de la empresa * ', validators=[DataRequired(), Length(max=50)])
    password = PasswordField('Password * ', validators=[DataRequired()])
    email = StringField('Email * ', validators=[DataRequired(), Email()])

    phone = TelField('Telefono * ', validators=[DataRequired(),Length(max=20)])

    direccionLinea1 = StringField('Direccion 1 *', validators=[DataRequired(),Length(max=50)])
    direccionLinea2 = StringField('Direccion 2', validators=[Length(max=50)])
    poblacion = StringField('Poblacion * ', validators=[DataRequired(),Length(max=50)])
    provincia = StringField('Provincia * ', validators=[DataRequired(),Length(max=50)])
    codigo_postal = IntegerField('Codigo Postal * ', validators=[DataRequired()])
    pais = StringField('Pais * ', validators=[DataRequired(),Length(max=40)])
    url = StringField('Url * ', validators=[DataRequired(),Length(max=40)])
    persona_contacto = StringField('Persona de contacto', validators=[DataRequired(),Length(max=100)])
    
    #logo
    consentimiento = BooleanField('Consentimiento *')
    recrouting = BooleanField('Buscas reclutar gente *')
    recovery = StringField('Frase de recuperación', validators=[DataRequired(),Length(max=100)])
    cif = StringField('CIF de la empresa', validators=[DataRequired(),Length(max=100)])

    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    cif = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesion')