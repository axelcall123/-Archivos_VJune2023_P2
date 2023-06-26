from flask import Flask, redirect, url_for, request,jsonify
import boto3
from Analizador.Comandos.create import Create
from Analizador.Comandos.delete import Delete
from Analizador.Comandos.copy import Copy
from Analizador.Comandos.transfer import Transfer
from Analizador.Comandos.rename import Rename
from Analizador.Comandos.modify import Modify
from Analizador.Comandos.deleteAll import DeleteAll
from Analizador.Comandos.backup import Backup
from Analizador.Comandos.recovery import Recovery
from Analizador.Comandos.open import Open


    


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
        return {"Creacion": "Archivo-Bucket"}
    elif(request.json['type']):
        create.nombre = request.json['name']
        create.contenido = request.json['body']
        create.ruta = request.json['path']
        create.creacionServer()
        return {"Creacion": "Archivo-Server"}
    return {"Creacion": "f"}
    


@app.route('/delete',methods = ['POST'])
def delete():
    delete=Delete()
    if(request.json['type']=="bucket"):
        delete.nombre=request.json['name']
        delete.ruta=request.json['path']
        delete.borrarBucket()
        return {"Eliminacion":"Archivo-Bucket"}
    elif(request.json['type']):
        delete.nombre = request.json['name']
        delete.ruta = request.json['path']
        return {"Eliminacion": delete.borrarServer()}
    return {"Eliminacion":"f"}


@app.route('/copy',methods = ['POST'])
def copy():
    copy=Copy()
    copy.de=request.json['from']
    copy.a=request.json['to']
    if(request.json['type_from']=="bucket")and(request.json['type_to']=="bucket"):
        copy.copiarBucketToBucket()
        return {"copy":"Archivo-Bucket-Bucket"}
    elif(request.json['type_from']=="server")and(request.json['type_to']=="bucket"):
        copy.copiarServerToBucket()
        return {"copy":"Archivo-server-Bucket"}
    elif(request.json['type_from']=="bucket")and(request.json['type_to']=="server"):
        return {"copy": copy.copiarBucketToServer()}
    elif(request.json['type_from']=="server")and(request.json['type_to']=="server"):
        return {"copy": copy.copiarServerToServer()}

@app.route('/transfer',methods = ['POST'])
def trasfer():
    trasfer=Transfer()
    trasfer.de=request.json['from']
    trasfer.a=request.json['to']
    if(request.json['type_from']=="bucket")and(request.json['type_to']=="bucket"):
        trasfer.trasferirBucketToBucket()
        return {"trasfer":"Archivo-Bucket-Bucket"}
    elif(request.json['type_from']=="server")and(request.json['type_to']=="bucket"):
        trasfer.trasferirServerToBucket()
        return {"trasfer":"Archivo-server-Bucket"}
    elif(request.json['type_from']=="bucket")and(request.json['type_to']=="server"):
        return {"trasfer": trasfer.trasferirBucketToServer()}
    elif(request.json['type_from']=="server")and(request.json['type_to']=="server"):
        return {"trasfer": trasfer.trasferirServerToServer()}

@app.route('/rename',methods = ['POST'])
def rename():
    rename=Rename()
    if(request.json['type']=="bucket"):
        rename.ruta=request.json['path']
        rename.nombre=request.json['name']
        rename.renombrarBucket()
        return {"rename":"Archivo-Bucke"}
    elif(request.json['type']=='server'):
        rename.ruta = request.json['path']
        rename.nombre = request.json['name']
        return {"rename": rename.renombrarServer()}

@app.route('/modify',methods = ['POST'])
def modify():
    modify=Modify()
    if(request.json['type']=="bucket"):
        modify.ruta=request.json['path']
        modify.contenido=request.json['body']
        modify.modificarBucket()
        return {"modify":"Archivo-Bucke"}
    elif(request.json['type']=='server'):
        modify.ruta = request.json['path']
        modify.contenido = request.json['body']
        return {"modify": modify.modificarServer()}

@app.route('/delete_all',methods = ['POST'])
def deleteAll():
    deleteAll=DeleteAll()
    if(request.json['type']=="bucket"):
        deleteAll.borrarBucket()
        return {"borrar":"borror TODO-Bucket"}
    elif(request.json['type']=='server'):
        return {"borrar": deleteAll.borrarServer()}

@app.route('/backup',methods = ['POST'])
def backUp():
    backup=Backup()
    if(request.json['type_from']=="server")and(request.json['type_to']=="bucket"):
        backup.name=request.json['name']
        backup.backupservertobucket()
        return {"backUp":"Servidor to bucket"}
    
@app.route('/recovery',methods = ['POST'])
def recovery():
    recovery=Recovery()
    if(request.json['type_from']=="bucket")and(request.json['type_to']=="server"):
        recovery.name=request.json['name']
        recovery.recoveryBuckettoServer()
        return {"recovery":"Servidor to bucket"}
    

@app.route('/open',methods = ['POST'])
def open():
    open=Open()
    if(request.json['type']=="bucket"):
        open.name=request.json['name']
        open.openBucket()
        return {"open":" bucket file"}



if __name__== "__main__":
    app.run(debug=True,port=3000)



