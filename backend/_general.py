import os

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
