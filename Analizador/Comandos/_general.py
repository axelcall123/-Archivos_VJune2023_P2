from Analizador.Aplicacion.variablesGlobales import temporalFile
import json

def getTxt(texto):
    global temporalFile
    if texto=='!':#elimina
        temporalFile == ""
        return 'delete'
    elif texto=='$':# retorna el texto
        return temporalFile
    else:  # agrega
        temporalFile += texto + "\n"
        return 'add'

def getTJson(repuesta):
    jsoN = json.loads(repuesta.text)
    for a in jsoN:
        getTxt(jsoN[a])