from flask import Flask, redirect, url_for, request,jsonify
import boto3
from Analizador.Comandos.create import Create
from Analizador.Comandos.delete import Delete
from Analizador.Comandos.copy import Copy


    


app=Flask(__name__)
@app.route("/")
def index():
    return {"hola":"hola mundo"}



#pos put path 
@app.route('/create',methods = ['POST'])
def create():
    create=Create()
    if(request.json['type']=="bucket"):
        create.nombre=request.json['name']
        create.contenido=request.json['body']
        create.ruta=request.json['path']
        create.creacionBucket()
     
    return {"Creacion":"Archivo-Bucket"}


@app.route('/delete',methods = ['POST'])
def delete():
    delete=Delete()
    if(request.json['type']=="bucket"):
        delete.nombre=request.json['name']
        delete.ruta=request.json['path']
        delete.borrarBucket()
    return {"Eliminacion":"Archivo-Bucket"}


@app.route('/copy',methods = ['POST'])
def copy():
    copy=Copy()
    if(request.json['type_from']=="bucket")and(request.json['type_to']=="bucket"):
        copy.de=request.json['from']
        copy.a=request.json['to']
        copy.copiarBucketToBucket()
    return {"copy":"Archivo-Bucket-Bucket"}



if __name__== "__main__":
    app.run(debug=True,port=3000)



