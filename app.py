from flask import Flask, redirect, url_for, request,jsonify
import boto3
from Analizador.Comandos.create import Create
from Analizador.Comandos.delete import Delete


    


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



if __name__== "__main__":
    app.run(debug=True,port=3000)



