from flask import Flask, jsonify, request, Response
# from ..Test.key import *
from varDef import *
import _general as _G
import os
import shutil
import json
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Flask'

@app.route('/create', methods=['POST'])#crea archviso
def archivoC():
    '''{
    "ruta":"/ar/",
    "nombre":"a.txt",
    "contenido":"skdjfkls"
    }'''
    rs = request.get_json()#json
    os.makedirs(rutaEspecifica+rs["ruta"], exist_ok=True)  # creo por si no existe
    # renombro si existe
    reName = _G.creRenameL(rutaEspecifica+rs["ruta"], rs["nombre"])
    f = open(rutaEspecifica+rs["ruta"]+reName, "a+")  # abriendo y creando
    f.write(f.read()+rs["contenido"])
    f.close()  # siempre cerrar
    return jsonify({'mensaje': 'archivo creado',})

@app.route('/create', methods=['DELETE'])#elimina archivo
def archivoD():
    '''{
    "ruta":"/ar/",
    "nombre":"a(1).txt" {opcional}
    }'''
    rs = request.get_json()  # json
    ruta=rutaEspecifica+rs["ruta"]
    if "nombre" in rs:
        ruta=ruta+rs["nombre"]
    return jsonify({'mensaje': _G.deleteSever(ruta)})
    
@app.route('/copy', methods=['POST'])  # copiar archivo server->server; bucket->server
def copySB():
    '''{
    "from":"/A/a.txt",
    "to":"/B/"
    }'''
    rs = request.get_json() # json
    if 'from' in rs and 'to' in rs:# de server a server
        _G.copySever(rutaEspecifica+rs["to"],rutaEspecifica+rs["from"])
        return jsonify({'mensaje': 'archivos copiado'})
    elif 'from' in rs:# de bucket a server
        print()
        return jsonify({'mensaje': 'copio json'})#FIXME:

@app.route('/copy', methods=['GET'])# listado de los archivos del server
def copyLS():
    rs = request.get_json()  # json
    if 'to' in rs:  # de server a bucket
        txt="{"+_G.listadoJson(rutaEspecifica+rs["to"])+"}"
        return jsonify({'mensaje': json.loads(txt)})

@app.route('/transfer', methods=['POST'])# tranfiere archivo server->server; bucket->server
def tranferSB():
    '''{
    "from":"/A/a.txt",
    "to":"/B/"
    }'''
    rs = request.get_json()  # json
    if 'from' in rs and 'to' in rs:  # de server a server
        _G.transferSersver(rutaEspecifica+rs["to"], rutaEspecifica+rs["from"])
        return jsonify({'mensaje': 'archivos transferidos'})
    elif 'from' in rs:  # de bucket a server
        print()
        return jsonify({'mensaje': 'tranfiero json'})# FIXME:

@app.route('/transfer', methods=['GET'])  # listado de los archivos del server
def transferLS():
    rs = request.get_json()  # json
    if 'to' in rs:  # de server a bucket
        txt = "{"+_G.listadoJson(rutaEspecifica+rs["to"])+"}"
        for file in os.listdir(rutaEspecifica+rs["to"]):
            _G.deleteSever(os.path.join(rutaEspecifica+rs["to"],file))
        return jsonify({'mensaje': json.loads(txt)})


@app.route('/rename', methods=['PUT'])
def rename():
    '''{
    "ruta":"/A/a.txt",
    "nombre":"c.txt",
    }'''
    rs = request.get_json()
    ruta=rutaEspecifica+rs["ruta"]
    arrayRuta=ruta.split("/")
    for iI in arrayRuta:
        if(iI<len(range)-1):
            nuevaRuta +="/"+arrayRuta[iI]
    if os.path.exists(ruta):
        if os.path.exists(nuevaRuta+rs["nombre"]):
            return jsonify({'mensaje': 'ya existe el archivo'})
        else:
            os.rename(ruta, nuevaRuta+rs["nombre"])
    else:
        return jsonify({'mensaje': 'no existe ruta'})
            

@app.route('/modify', methods=['PUT'])
def modify():
    '''{
    "ruta":"/A/a.txt",
    "cuerpo":"hola xd no se que poner"",
    }'''
    rs = request.get_json()
    if os.path.exists(rutaEspecifica+rs["ruta"]):
        f = open(rutaEspecifica+rs["ruta"], "w")
        f.write(rs["cuerpo"])
        f.close()
        return jsonify({'mensaje': 'archivo modificado'})

if __name__ == '__main__':
    # debug modo solo sirve para que se acutalice automaticamente
    app.run(host='0.0.0.0', port=1000, debug=True)
    #FIXME:cambiar puerto a 5000 en el server