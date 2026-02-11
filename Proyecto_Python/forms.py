from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, StringField, SubmitField


class TestForm(FlaskForm):
    titulo = StringField('Titulo de la prueba')
    num_prueba = IntegerField('Numero de la prueba')
    codigo = PasswordField('Clave')
    enviar = SubmitField('Lanzar prueba')



