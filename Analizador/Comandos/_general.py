import os
import shutil
import json
import boto3
from Analizador.Comandos.varDef import *

def endPath(string):
    if string.endswith('/') and not ".txt" in string:#solo sea /a/b/c/ | /a/b/c
        return string
    else:
        return string+'/'

def creRenameL(idFolderRaiz: str, nombre: str) -> str:
    # FIXME: para no reahacerlo se puede poner otro parametro par unirlo con navacion carpetas, se puede optimizar
    if os.path.exists(idFolderRaiz+'/'+nombre):  # existe nombre
        array = nombre.split(".")
        if len(array) == 1:  # para folder
            nombre = nombre+'(1)'
        else:  # para extension
            nombre = array[0]+'(1).'+array[1]
        return creRenameL(idFolderRaiz, nombre)
    else:  # no existe nombre, retorno el nombre
        return nombre


def deleteSever(ruta):
    if (os.path.exists(ruta)):  # existe ruta
        if '.txt' in ruta:  # es archivo
            os.remove(ruta)
        else:  # es carpeta
            shutil.rmtree(ruta)
        return 'archivo eliminado'
    else:
        return 'ruta no encontrada'

def createSever(nombre,contenido,ruta):
    os.makedirs(ruta, exist_ok=True)  # creo por si no existe
    # renombro si existe
    reName = creRenameL(ruta, nombre)
    f = open(ruta+reName, "a+")  # abriendo y creando
    f.write(f.read()+contenido)
    f.close()  # siempre cerrar

def copySever(urlTo, urlFrom):
    if not (os.path.exists(urlTo) and os.path.exists(urlFrom)):  # existe es carpeta
        return 'ruta no existe'
    if '.txt' in urlFrom:
        rename = creRenameL(urlTo, urlFrom.split('/')[-1])
        nuevoUrl = os.path.join(urlTo, rename)  # renombro por si existe
        shutil.copy(urlFrom, nuevoUrl)
        return 'archivo copiado'

    for item in os.listdir(urlFrom):
        url1 = os.path.join(urlTo, item)
        url2 = os.path.join(urlFrom, item)
        if os.path.exists(url1) and not '.txt' in item:  # existe es carpeta
            copySever(url1, url2)
        elif not os.path.exists(url1) and not '.txt' in item:  # no existe es carpeta
            shutil.copytree(url2, url1)
        else:  # no existe es archivo
            rename = creRenameL(urlTo, item)
            nuevoUrl = os.path.join(urlTo, rename)  # renombro por si existe
            shutil.copy(url2, nuevoUrl)
    return 'archivos copiados'


def transferSersver(urlTo, urlFrom):
    if not (os.path.exists(urlTo) and os.path.exists(urlFrom)):  # existe es carpeta
        return 'ruta no existe'
    if '.txt' in urlFrom:
        rename = creRenameL(urlTo, urlFrom.split('/')[-1])
        nuevoUrl = os.path.join(urlTo, rename)  # renombro por si existe
        shutil.move(urlFrom, nuevoUrl)
        return 'archivo tranferido'
    for item in os.listdir(urlFrom):
        url1 = os.path.join(urlTo, item)
        url2 = os.path.join(urlFrom, item)
        if os.path.exists(url1) and not '.txt' in item:  # existe es carpeta
            transferSersver(url1, url2)
        elif not os.path.exists(url1) and not '.txt' in item:  # no existe es carpeta
            shutil.copytree(url2, url1)  # copio
            shutil.rmtree(url2)  # elimino tree
        else:  # no existe es archivo
            rename = creRenameL(urlTo, item)
            nuevoUrl = os.path.join(urlTo, rename)  # renombro por si existe
            shutil.move(url2, nuevoUrl)
    return 'archivos transferidos'


def readTxt(url):
    f = open(url, 'r')
    file_content = f.read()
    f.close()
    return file_content


def listadoJsonServer(url) -> json:  # posicion es para saber si es el primero, subcarpeta
    listado = os.listdir(url)
    txtJson = ''
    for iI in range(len(listado)):
        if '.txt' in listado[iI]:  # es archivo
            if iI < len(listado)-1:  # ultimo item
                txtJson += '"'+listado[iI]+'":"' + \
                    readTxt(os.path.join(url, listado[iI]))+'",'
            else:
                txtJson += '"'+listado[iI]+'":"' + \
                    readTxt(os.path.join(url, listado[iI]))+'"'
                return txtJson
        else:  # es carpeta
            if iI < len(listado)-1:  # ultimo item
                txtJson += '"' + \
                    listado[iI] + \
                    '":{'+listadoJsonServer(os.path.join(url, listado[iI]))+'},'
            else:
                txtJson += '"' + \
                    listado[iI] + \
                    '":{'+listadoJsonServer(os.path.join(url, listado[iI]))+'}'
                return txtJson
    return ''


def listadoJsonBucket(pathOrigen) -> json:
    s3 = boto3.client('s3')
    name = '202001574'
    response = s3.list_objects_v2(Bucket=name, Prefix=pathOrigen)
    jsonTxt=''
    conteo=0
    for obj in response['Contents']:
        contenido=''
        if not obj['Key'].endswith('/'):  # solo files
            respuesta = s3.get_object(Bucket=name, Key=obj['Key'])
            contenido = respuesta['Body'].read().decode('utf-8')  # contenido
            #             ruta          carpetas,array           ,     nombre
            if conteo==0:
                jsonTxt += '"'+obj["Key"]+'":"'+contenido+'"'
            else:
                jsonTxt += ',"'+obj["Key"]+'":"'+contenido+'"'
            conteo+=1
    return jsonTxt


def listado(url):  # listado sin el txt
    array = url.split('/')
    txt = ''
    for a in range(len(array)):
        if array[a] == '':
            array.pop(a)
    for a in range(len(array)-1):
        if array[a] == '':
            continue
        else:
            txt += array[a]+'/'
    return txt


def existeBucket(s3, name, f_key):
    try:
        s3.head_object(Bucket=name, Key=f_key)
        return True
    except:
        return False


def recorrerJsonServer(ruta, aJson,tipo,nombre):#FIXME:testear
    for aA in aJson:  # NORMAL
        if '.txt' in aA:  # txt
            if tipo=="server":
                createSever(aA, aJson[aA], ruta+'/')
            elif tipo=="bucket":
                # print(ruta, '>>', aA, '<>', aJson[aA])
                s3=boto3.resource('s3')
                s3.Object('202001574', ruta+aA).put(Body=aJson[aA])
        else:  # folder
            if tipo == "server":#esta dentro asi que
                os.makedirs(f'{ruta}/{aA}', exist_ok=True)  # creo por si no existe
                recorrerJsonServer(f'{ruta}/{aA}', aJson[aA],tipo,nombre)
            elif tipo=="bucket":
                # s3 = boto3.resource('s3')
                # s3.Object('202001574', f'{nombre}/{aA}/')
                recorrerJsonServer(f'{ruta}{aA}/', aJson[aA], tipo, nombre)


def recorrerJsonBucket(ruta,aJson,tipo,nombre):
    for aA in aJson:  # NORMAL
        if '.txt' in aA:  # txt
            urlSintxt = listado(aA)  # obtengo url sin el txt
            # urlSintxt = urlSintxt.replace(aA.split('/')[0]+'/','') # obteno nombre archivos/.../nombre.txt> .../nombre.txt
            if tipo=="server":
                createSever(aA.split('/')[-1], aJson[aA], ruta+nombre+"/"+urlSintxt)
            elif tipo=="bucket":
                s3 = boto3.resource('s3')
                s3.Object('202001574', aA).put(Body=aJson[aA])

