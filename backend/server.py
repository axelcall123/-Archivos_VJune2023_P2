from flask import Flask, jsonify, request, Response
# import boto3
# from ..Test.key import *
from varDef import *
import _general as _G
import os
import shutil
app = Flask(__name__)

# s3 = boto3.client(
#     's3',
#     aws_access_key_id=acces_key,
#     aws_secret_access_key=secret_acces_key
# )


@app.route('/')
def index():
    return 'Welcome to Flask'


@app.route('/create', methods=['GET','POST'])
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


@app.route('/create', methods=['GET', 'DELETE'])
def archivoD():
    rs = request.get_json()  # json
    ruta=rutaEspecifica+rs["ruta"]
    if "nombre" in rs:
        ruta=ruta+rs["nombre"]
    if (os.path.exists(ruta)):  # existe ruta
        print('E')
        shutil.rmtree(ruta)
        return jsonify({'mensaje': 'archivo eliminado', })
    else:
        print('N E')
        return jsonify({'mensaje': 'ruta no encontrada', })
    

if __name__ == '__main__':
    # debug modo solo sirve para que se acutalice automaticamente
    app.run(host='0.0.0.0', port=1000, debug=True)
    #FIXME:cambiar puerto a 5000 en el server