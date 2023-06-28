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
    create.name(request.json['name'])
    create.body(request.json['body'])
    create.path(request.json['path'])
    if(request.json['type']=="bucket"):
        create.creacionBucket()
        return {"Creacion": "Archivo-Bucket"}
    elif(request.json['type']):
        create.creacionServer()
        return {"Creacion": "Archivo-Server"}
    return {"Creacion": "f"}
    


@app.route('/delete',methods = ['POST'])
def delete():
    delete=Delete()
    delete.name(request.json['name'])
    delete.path(request.json['path'])
    if(request.json['type']=="bucket"): 
        return {"Eliminacion":delete.borrarBucket()}
    elif(request.json['type']):
        return {"Eliminacion": delete.borrarServer()}
    return {"Eliminacion":"f"}


@app.route('/copy',methods = ['POST'])
def copy():
    copy=Copy()
    copy.desde(request.json['from'])
    copy.to(request.json['to'])
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
    trasfer.desde(request.json['from'])
    trasfer.to(request.json['to'])
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
    rename.path(request.json['path'])
    rename.name(request.json['name'])
    if(request.json['type']=="bucket"):
        rename.renombrarBucket()
        return {"rename":"Archivo-Bucke"}
    elif(request.json['type']=='server'):
        return {"rename": rename.renombrarServer()}

@app.route('/modify',methods = ['POST'])
def modify():
    modify=Modify()
    modify.path(request.json['path'])
    modify.body(request.json['body'])
    if(request.json['type']=="bucket"):
        modify.modificarBucket()
        return {"modify":"Archivo-Bucke"}
    elif(request.json['type']=='server'):
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
    backup.Name(request.json['name'])
    if (request.json['ip'] != '') and (request.json['port'] != ''):  # sent
        backup.Ip(request.json['ip'])
        backup.Port(request.json['port'])
        backup.typeTo(request.json['type_to'])
        backup.typeFrom(request.json['type_from'])
        if (request.json['type_to'] == "server"):  # envio a su server
            #listado de todo el server
            # backup.backupSend()  # FIXME:HERE
            return {"backUpS": backup.backupSend()}  # envio a su bukcet
        elif (request.json['type_to'] == "bucket"):
            #listado de todo el bucket
            # backup.backupSend()  # FIXME:HERE
            return {"backUpB": backup.backupSend()}
    elif (request.json['type_from'] == "server") and (request.json['type_to'] == "bucket"):  # ready
        backup.backupservertobucket()
        return {"backUp": "Servidor to bucket"}
    elif (request.json['type_from'] == "bucket") and (request.json['type_to'] == "server"):  # mine<ready
        backup.backupbucketrtoserver()
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
    recovery.Name(request.json['name'])
    if (request.json['ip'] != '') and (request.json['port'] != ''):  # sent
        recovery.Ip(request.json['ip'])
        recovery.Port(request.json['port'])
        recovery.typeTo(request.json['type_to'])
        recovery.typeFrom(request.json['type_from'])
        # recovery.archivos=request.json['archivos'] #only tests FIXME:cambiar depues del test
        if (request.json['type_from'] == "server"):  # viene de server
            recovery.recoveryReceive()
            return {"recoveryS": "se recuperaron los archivos existentes"}  # viene de bucket
        elif (request.json['type_from'] == "bucket"):
            recovery.recoveryReceive()
            return {"recoveryB": "se recuperaron los archivos existentes"}
    elif (request.json['type_from'] == "bucket") and (request.json['type_to'] == "server"):  # ready
        recovery.recoveryBuckettoServer()
        return {"recovery": "bucket to Servidor"}
    elif (request.json['type_from'] == "server") and (request.json['type_to'] == "bucket"):  # mine
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
    backup.Name(request.json['name'])
    backup.typeTo(request.json['type_to'])
    backup.typeFrom(request.json['type_from'])
    backup.archivos = request.json['archivos']
    if request.json['type_from'] == "server":  # viende de server
        backup.backupReceive()
        return {"backUp": "Servidor to bucket"}
    elif request.json['type_from'] == "bucket":  # viene de bucket
        backup.backupReceive()
        return {"backUp": "Servidor to bucket"}


@app.route('/recoveryO', methods=['POST'])  # bucket de los demas
def recoveryO():
    recovery = Recovery()
    recovery.Name(request.json['name'])
    recovery.typeTo(request.json['type_to'])
    recovery.typeFrom(request.json['type_from'])
    if request.json['type_from'] == "server":
        return jsonify({
                        "type_to": request.json['name']
                        , "type_from": request.json['type_from']
                        , "name": request.json['name']
                        , "archivos": recovery.recoverySend()
                        })
        # return {"backUp": "Servidor to bucket"}
    elif request.json['type_from'] == "bucket":
        return jsonify({
            "type_to": recovery.tipoA
            , "type_from": recovery.tipoDe
            , "name": recovery.name
            , "archivos": recovery.recoverySend()
        })
        # return {"backUp": "Servidor to bucket"}


@app.route('/respuestaT', methods=['POST'])
def responseT():
    res = request.json
    return {"respuesta": request.json}
    

@app.route('/open',methods = ['POST'])
def openS():
    opeN=Open()
    opeN.Name(request.json['name'])
    if (request.json['ip'] != '') and (request.json['port'] != ''):  # sent
        opeN.type(request.json['type'])
        opeN.Ip(request.json['ip'])
        opeN.Port(request.json['port'])
        array=opeN.openRecive()
        return {"open":f'nombre:{array[0]}, contenido:{array[1]}'}
    if(request.json['type']=="bucket"):
        return {"openB":f'retono en open>>{opeN.openBucket()}'}
    elif(request.json['type']=="server"):
        return {"openS": f'retono en open>>{opeN.openServer()}'}


@app.route('/openO', methods=['POST'])
def openO():
    opeN = Open()
    opeN.type(request.json['type'])
    opeN.Name(request.json['name'])
    if (request.json['type'] == "bucket"):
        return {"name":opeN.name,"contenido": opeN.openSend()}
    elif (request.json['type'] == "server"):
        return {"name": opeN.name, "contenido": opeN.openSend()}


if __name__== "__main__":
    app.run(host='0.0.0.0',debug=True, port=3000)



