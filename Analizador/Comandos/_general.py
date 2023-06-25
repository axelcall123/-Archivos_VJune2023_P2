import os
import shutil
import json


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


def listadoJson(url) -> json:  # posicion es para saber si es el primero, subcarpeta
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
                    '":{'+listadoJson(os.path.join(url, listado[iI]))+'},'
            else:
                txtJson += '"' + \
                    listado[iI] + \
                    '":{'+listadoJson(os.path.join(url, listado[iI]))+'}'
                return txtJson
    return ''


def listado(url):  # listado sin el txt
    array = url.split('/')
    txt = ''
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
