import Analizador.ply.lex as lex
import Analizador.ply.yacc as yacc
import re


#LEXICO
reserved = {
    'create':'CREATE',
    'delete':'DELETE',
    'copy':'COPY',
    'transfer':'TRANSFER',
    'rename':'RENAME',
    'modify':'MODIFY',
    'backup':'BACKUP',
    'recovery':'RECOVERY',
    'delete_all':'DELETE_ALL',
    'open':'OPEN',
    'server':'SERVER',
    'bucket':'BUCKET'
    
}
tokens = [
    'NAME',
    'BODY',
    'PATH',
    'TYPE',
    'FROM',
    'TO',
    'TYPE_TO',
    'TYPE_FROM',
    'IP',
    'PORT',

    'ARCHIVO',
    'RUTA',
    'AIP',
    'WORD',
    'APORT',
    'STRING'

] + list(reserved.values())

t_NAME = r'-name->'
t_BODY = r'-body->'
t_PATH = r'-path->'
t_TYPE = r'-type->'
t_FROM = r'-from->'
t_TO = r'-to->'
t_TYPE_TO = r'-type_to->'
t_TYPE_FROM = r'-type_from->'
t_IP = r'-ip->'
t_PORT = r'-port->'

def t_ARCHIVO(t):
    r'(\"(\w|\s)+\.\w+\")|(\w+\.\w+)'
    t.value = t.value.lower()
    return t

def t_RUTA(t):
    r'(\/((\w+(\.\w+)?)|(\"(\w|\s)+(\.\w+)?\")))+\/?'
    t.value = t.value.lower()
    return t

def t_AIP(t):
    r'\d{1,3}(\.\d{1,3}){3}'
    t.value = t.value.lower()
    return t

def t_WORD(t):
    r'\w+'
    t.value = t.value.lower()
    return t


def t_APORT(t):
    r'\d{1,4}'
    t.value = t.value.lower()
    return t

def t_STRING(t):
    r'\"(\w|\s)+\"'
    t.value = t.value.lower()
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter Invalido: '{t.value[0]} ,{t}'")
    t.lexer.skip(1)


lexer = lex.lex(reflags=re.IGNORECASE)

# Parser


def p_inicio(p):
    '''inicio : lexico
    '''
    if p[1] == None:p[0] = ["error"]
    else:p[0] = p[1]


def p_lexico(p):
    '''lexico : lexico comandos
                | comandos
    '''
    if len(p)==3:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = p[1]


def p_comandos(p):
    '''comandos : maincomando subcomando
                | maincomando
    '''
    if len(p) == 3:
        arr = []
        arr.append(p[1])
        arr.append(p[2])
        p[0]=arr
    else:
        arr = []
        arr.append(p[1])
        p[0] = arr


def p_main_comando(p):
    '''maincomando : CONFIGURE 
                | CREATE
                | DELETE
                | COPY
                | TRANSFER
                | RENAME
                | MODIFY
                | BACKUP
                | RECOVERY
                | DELETE_ALL
                | OPEN
    '''
    p[0] = p[1]


def p_subcomando(p):
    '''subcomando : subcomando sub
                    | sub
    '''
    if len(p) == 3:
        arr = p[1]
        arr.append(p[2])
        p[0] = arr
    elif len(p) == 2:
        arr = []
        arr.append(p[1])
        p[0] = arr


def p_sub(p):
    '''sub : TYPE tipo
            | NAME nombre
            | BODY string
            | PATH RUTA
            | FROM RUTA
            | TO RUTA
            | TYPE_TO tipo
            | TYPE_FROM tipo
            | IP AIP
            | PORT APORT
    '''
    arr = []
    arr.append(p[1])
    arr.append(p[2])
    p[0] = arr

def p_tipo(p):
    '''tipo : BUCKET
            | SERVER
    '''
    p[0] = p[1]

def p_nombre(p):
    '''nombre : ARCHIVO
                | STRING
                | WORD
                | RUTA
    '''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Error sintactico en el token '{p.value}', {p.lexer.lineno}")
        print(type(p))
    else:
        print("Error sintactico EOF")


def gramarMain():
    parser = yacc.yacc()
    f = open("Analizador/entradas.txt", "r")
    input = f.read()
    resultado = parser.parse(input.lower())
    return resultado
