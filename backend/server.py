from flask import Flask, jsonify, request, Response
# from ..Test.key import *
from varDef import *
import _general as _G
import os
import boto3
from key import *
import json
app = Flask(__name__)
s3 = boto3.client(
    's3',
    aws_access_key_id=acces_key,
    aws_secret_access_key=secret_acces_key
)
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
    os.makedirs(rutaSer+rs["ruta"], exist_ok=True)  # creo por si no existe
    # renombro si existe
    reName = _G.creRenameL(rutaSer+rs["ruta"], rs["nombre"])
    f = open(rutaSer+rs["ruta"]+reName, "a+")  # abriendo y creando
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
    ruta=rutaSer+rs["ruta"]
    if "nombre" in rs:
        ruta=ruta+rs["nombre"]
    return jsonify({'mensaje': _G.deleteSever(ruta)})
    
@app.route('/copy', methods=['POST'])  # copiar archivo server->server; bucket->server
def copySB():
    '''{
    "comando":"b->s",|"s->s"
    "from":"/A/a.txt","/","/hola.txt","/a/b/"
    "to":"/B/"
    }'''
    rs = request.get_json() # json
    if rs["comando"]=='s->s':# de server a server
        
        return jsonify({'mensaje': _G.copySever(rutaSer+rs["to"], rutaSer+rs["from"])})
    elif rs["comando"] == 'b->s':  # de bucket a server
        if not _G.existeBucket(s3, name, f'{rutaB}{rs["from"]}'):
            return jsonify({'mensaje': 'no existe ruta en el bucket'})
        if '.txt' in rs["from"]:#copio solo un archivo
            #                         ruta nombre                              nombre
            rename = _G.creRenameL(os.path.join(rutaSer, rs["to"]), rs['from'].split('/')[-1])
            s3.download_file(name, f'{rutaB}{rs["from"]}', os.path.join(
                rutaSer+rs["to"], rename))  # ubicacion boto,ubicacion local
            return jsonify({'mensaje': 'copio el archivo'})
        else:#copio una carpeta
            response = s3.list_objects_v2(Bucket=name,Prefix=f'{rutaB}{rs["from"]}')#obtiene todo el listado
            for obj in response['Contents']:
                print(obj['Key'])
                if not obj['Key'].endswith('/'):  # solo files
                    relativePath = _G.listado(obj['Key'])# obtengo la ruta del bucket sin el nombre
                    relativePath = relativePath.replace(f'{rutaB}{rs["from"]}', '')# quito la parte de la ruta del bucket, que me causa problemas
                    relativePath = os.path.join(rutaSer+rs["to"], relativePath) # agrego la ruta del server
                    os.makedirs(relativePath, exist_ok=True)#creo la carpeta
                    rename = _G.creRenameL(relativePath, obj['Key'].split('/')[-1])#renombro
                    #                         ruta nombre                              nombre
                    s3.download_file(name,obj["Key"], os.path.join(relativePath, rename))#ubicacion boto,ubicacion local     
        return jsonify({'mensaje': 'copio el folder'})

@app.route('/copy', methods=['GET'])# listado de los archivos del server
def copyLS():
    '''{
    "to":"/B/"
    }'''
    rs = request.get_json()  # json
    if 'to' in rs:  # de server a bucket
        txt="{"+_G.listadoJson(rutaSer+rs["to"])+"}"
        return jsonify({'mensaje': json.loads(txt)})

@app.route('/transfer', methods=['POST'])# tranfiere archivo server->server; bucket->server
def tranferSB():
    '''{
    "comando":"b->s",|"s->s"
    "from":"/A/a.txt","/","/hola.txt","/a/b/"
    "to":"/B/"
    }'''
    rs = request.get_json()  # json
    if rs["comando"]=='s->s':  # de server a server
        return jsonify({'mensaje': _G.transferSersver(rutaSer+rs["to"], rutaSer+rs["from"])})
    elif rs["comando"] == 'b->s':  # de bucket a server
        if not _G.existeBucket(s3, name, f'{rutaB}{rs["from"]}'):
            return jsonify({'mensaje': 'no existe ruta en el bucket'})
        if '.txt' in rs["from"]:  # copio solo un archivo
            #                         ruta nombre                              nombre
            rename = _G.creRenameL(os.path.join(
                rutaSer, rs["to"]), rs['from'].split('/')[-1])
            s3.download_file(name, f'{rutaB}{rs["from"]}', os.path.join(rutaSer+rs["to"], rename))  # ubicacion boto,ubicacion local
            s3.delete_object(name, f'{rutaB}{rs["from"]}')#extra borrar file
            return jsonify({'mensaje': 'transfirio el archivo'})
        else:  # copio una carpeta
            response = s3.list_objects_v2(Bucket=name, Prefix=f'{rutaB}{rs["from"]}')  # obtiene todo el listado
            folders=[]
            for obj in response['Contents']:
                print(obj['Key'])
                if not obj['Key'].endswith('/'):  # solo files
                    # obtengo la ruta del bucket sin el nombre
                    relativePath = _G.listado(obj['Key'])
                    # quito la parte de la ruta del bucket, que me causa problemas
                    relativePath = relativePath.replace(
                        f'{rutaB}{rs["from"]}', '')
                    # agrego la ruta del server
                    relativePath = os.path.join(rutaSer+rs["to"], relativePath)
                    os.makedirs(relativePath, exist_ok=True)  # creo la carpeta
                    rename = _G.creRenameL(relativePath, obj['Key'].split('/')[-1])  # renombro
                    #                         ruta nombre                              nombre
                    s3.download_file(name, obj["Key"], os.path.join(relativePath, rename))  # ubicacion boto,ubicacion local
                    s3.delete_object(Bucket=name, Key=obj["Key"])  # extra borrar file
                else:
                    folders.append(obj['Key'])
            for i in reversed(folders):#borrar todos los folders
                if  i!=f'{rutaB}{rs["from"]}':
                    s3.delete_object(Bucket=name, Key=i)
        return jsonify({'mensaje': 'tranfiero json'})# FIXME:
    
    return jsonify({'mensaje': 'que paso?'})

@app.route('/transfer', methods=['GET'])  # listado de los archivos del server
def transferLS():
    rs = request.get_json()  # json
    if 'to' in rs:  # de server a bucket
        txt = "{"+_G.listadoJson(rutaSer+rs["to"])+"}"
        for file in os.listdir(rutaSer+rs["to"]):
            _G.deleteSever(os.path.join(rutaSer+rs["to"],file))
        return jsonify({'mensaje': json.loads(txt)})

@app.route('/rename', methods=['PUT'])
def rename():
    '''{
    "ruta":"/A/a.txt",
    "nombre":"c.txt"
    }'''
    rs = request.get_json()
    ruta=rutaSer+rs["ruta"]
    nuevaRuta = _G.listado(ruta)
    if os.path.exists(ruta):
        if os.path.exists(nuevaRuta+rs["nombre"]):
            return jsonify({'mensaje': 'ya existe el archivo'})
        else:
            os.rename(ruta, nuevaRuta+rs["nombre"])
            return jsonify({'mensaje': 'fuer renombrado'})
    else:
        return jsonify({'mensaje': 'no existe ruta'})
            
@app.route('/modify', methods=['PUT'])
def modify():
    '''{
    "ruta":"/A/a.txt",
    "cuerpo":"hola xd no se que poner"",
    }'''
    rs = request.get_json()
    if os.path.exists(rutaSer+rs["ruta"]):
        f = open(rutaSer+rs["ruta"], "w")
        f.write(rs["cuerpo"])
        f.close()
        return jsonify({'mensaje': 'archivo modificado'})

if __name__ == '__main__':
    # debug modo solo sirve para que se acutalice automaticamente
    app.run(host='0.0.0.0', port=1000, debug=True)
    #FIXME:cambiar puerto a 5000 en el server