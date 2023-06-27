from Analizador.Aplicacion.variablesGlobales import temporalFile


def getTxt(texto):
    global temporalFile
    if texto=='!':#elimina
        temporalFile += ""
        return 'delete'
    elif texto=='$':# retorna el texto
        return temporalFile
    else:  # agrega
        temporalFile += texto + "\n"
        return 'add'

def getTJson(json):
    for a in json:
        getTxt(json[a])