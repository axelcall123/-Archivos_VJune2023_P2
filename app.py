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
        return {"Eliminacion":delete.borrarBucket()}
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


@app.route('/backupN', methods=['POST'])  # buckup solo nuestro
def backUpN():
    backup = Backup()
    if ("ip" in request.json) and ("port" in request.json):  # sent
        backup.ip = request.json['ip']
        backup.port = request.json['port']
        backup.name = request.json['name']
        backup.tipoA = request.json['type_to']
        backup.tipoDe = request.json['type_from']
        if (request.json['type_to'] == "server"):  # envio a su server
            #listado de todo el server
            backup.backupSend()
            return {"backUpS": "envio al otro servidor"}  # envio a su bukcet
        elif (request.json['type_to'] == "bucket"):
            #listado de todo el bucket
            backup.backupSend()
            return {"backUpB": "envio al otro servidor"}
    elif (request.json['type_from'] == "server") and (request.json['type_to'] == "bucket"):  # ready
        backup.name = request.json['name']
        backup.backupservertobucket()
        return {"backUp": "Servidor to bucket"}
    elif (request.json['type_from'] == "bucket") and (request.json['type_to'] == "server"):  # mine<ready
        backup.name = request.json['name']
        backup.backupbuckettoserver()
        return {"backUp": "Bucket to servidor"}
    # elif(request.json['type_from']=="server")and(request.json['type_to']=="server"):
    #     backup.name=request.json['name']
    #     backup.backupservertoserver()
    #     return {"backUp": "Servidor to servidor"}
    # elif(request.json['type_from']=="bucket")and(request.json['type_to']=="bucket"):
    #     backup.name=request.json['name']
    #     backup.backupbuckettobucket()
    #     return {"backUp": "Bucket to bucket"}


@app.route('/recoveryN', methods=['POST'])  # buckup solo nuestro
def recoveryN():
    recovery = Recovery()
    if ("ip" in request.json) and ("port" in request.json):  # sent
        recovery.ip = request.json['ip']
        recovery.port = request.json['port']
        recovery.name = request.json['name']
        recovery.tipoA = request.json['type_to']
        recovery.tipoDe = request.json['type_from']
        if (request.json['type_from'] == "server"):  # viene de server
            recovery.recoveryReceive()
            return {"recoveryS": "envio al otro servidor"}  # viene de bucket
        elif (request.json['type_from'] == "bucket"):
            recovery.recoveryReceive()
            return {"recoveryB": "envio al otro servidor"}
    elif (request.json['type_from'] == "bucket") and (request.json['type_to'] == "server"):  # ready
        recovery.name = request.json['name']
        recovery.recoveryBuckettoServer()
        return {"recovery": "bucket to Servidor"}
    elif (request.json['type_from'] == "server") and (request.json['type_to'] == "bucket"):  # mine
        recovery.name = request.json['name']
        recovery.recoveryServertobucket()
        return {"recovery": "Servidor to bucket"}
    # elif(request.json['type_from']=="bucket")and(request.json['type_to']=="bucket"):
    #     recovery.name=request.json['name']
    #     recovery.recoveryBuckettoBucket()
    #     return {"recovery":"Bucket to bucket"}
    # elif(request.json['type_from']=="server")and(request.json['type_to']=="server"):
    #     recovery.name=request.json['name']
    #     recovery.recoveryServertoserver()
    #     return {"recovery":"Servidor to servidor"}


@app.route('/backupO', methods=['POST'])  # bucket de los demas
def backUpO():
    backup = Backup()
    if request.json['type_from'] == "server":  # viende de server
        backup.name = request.json['name']
        backup.tipoA = request.json['type_to']
        backup.tipoDe = request.json['type_from']
        backup.archivos = request.json['archivos']
        backup.backupReceive()
        return {"backUp": "Servidor to bucket"}
    elif request.json['type_from'] == "bucket":  # viene de bucket
        backup.name = request.json['name']
        backup.tipoA = request.json['type_to']
        backup.tipoDe = request.json['type_from']
        backup.archivos = request.json['archivos']
        backup.backupReceive()
        return {"backUp": "Servidor to bucket"}


@app.route('/recoveryO', methods=['POST'])  # bucket de los demas
def recoveryO():
    recovery = Recovery()
    if request.json['type_from'] == "server":
        recovery.name = request.json['name']
        recovery.tipoA = request.json['type_to']
        recovery.tipoDe = request.json['type_from']
        recovery.archivos = request.json['archivos']
        recovery.recoverySend()
        return {"backUp": "Servidor to bucket"}
    elif request.json['type_from'] == "bucket":
        recovery.name = request.json['name']
        recovery.tipoA = request.json['type_to']
        recovery.tipoDe = request.json['type_from']
        recovery.archivos = request.json['archivos']
        recovery.recoverySend()
        return {"backUp": "Servidor to bucket"}


@app.route('/respuestaT', methods=['POST'])
def responseT():
    res = request.json
    return {"respuesta": request.json}
    

@app.route('/open',methods = ['POST'])
def open():
    open=Open()
    if(request.json['type']=="bucket"):
        open.name=request.json['name']
        return {"open":open.openBucket()}



if __name__== "__main__":
    app.run(debug=True,port=3000)



