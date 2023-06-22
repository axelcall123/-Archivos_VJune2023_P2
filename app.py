from flask import Flask, redirect, url_for, request,jsonify
import boto3
from Analizador.Comandos.create import Create
from Analizador.Comandos.delete import Delete
from Analizador.Comandos.copy import Copy
from Analizador.Comandos.transfer import Transfer
from Analizador.Comandos.rename import Rename
from Analizador.Comandos.modify import Modify


    


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

@app.route('/transfer',methods = ['POST'])
def trasfer():
    trasfer=Transfer()
    if(request.json['type_from']=="bucket")and(request.json['type_to']=="bucket"):
        trasfer.de=request.json['from']
        trasfer.a=request.json['to']
        trasfer.trasferirBucketToBucket()
    return {"trasfer":"Archivo-Bucket-Bucket"}

@app.route('/rename',methods = ['POST'])
def rename():
    rename=Rename()
    if(request.json['type']=="bucket"):
        rename.ruta=request.json['path']
        rename.nombre=request.json['name']
        rename.renombrarBucket()
    return {"rename":"Archivo-Bucke"}


@app.route('/modify',methods = ['POST'])
def modify():
    modify=Modify()
    if(request.json['type']=="bucket"):
        modify.ruta=request.json['path']
        modify.contenido=request.json['body']
        modify.modificarBucket()
    return {"modify":"Archivo-Bucke"}



if __name__== "__main__":
    app.run(debug=True,port=3000)



