from os import getenv
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

load_dotenv()

#Creación de una instancia de la clase Flask
app = Flask(__name__)

client = MongoClient(getenv('MONGO_URI'))

if "escuela" not in client.list_database_names():
    db = client['escuela']
    tabla = db['estudiantes']
    tabla.insert_one({})
else:
    db = client['escuela']
    tabla = db['estudiantes']

@app.route('/', methods=['GET'])

def home():
    return(client.list_database_names())

@app.route('/lista', methods=['GET'])
def lista():
    return (client.list_database_names())

@app.route('/tabla', methods=['GET'])
def tabla():
    documentos = client.escuela.estudiantes.find()
    listado=[]
    for doc in documentos:
        doc['_id'] = str(doc['_id']) 
        listado.append(doc)
    
    # IMPORTANTE: El return debe ir FUERA del for, alineado con el 'for'
    return jsonify(listado)

if __name__ == '__main__':
    app.run()










