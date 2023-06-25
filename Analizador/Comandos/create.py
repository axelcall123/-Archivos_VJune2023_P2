import os
import sys
import tempfile
#from Aplicacion.variablesGlobales import temporalFile
import boto3
from varDef import *
import _general as _G
class Create:
    def __init__ (self,):
        self.nombre=""
        self.contenido=""
        self.ruta=""
        self.tipo=""

    def name (self,nombre):
        #posibles cambios necesario al nombre
        if('"' in nombre):
            self.nombre=nombre.replace("\"", "" )
        else:
            self.nombre=nombre
        
        

    def body (self,contenido):
        if('"' in contenido):
            self.contenido=contenido.replace("\"", "" )
        else:
            self.contenido=contenido


    def path (self,ruta):
        #posibles cambios necesario ala ruta
        if('"' in ruta):
            self.ruta=ruta.replace("\"", "" )
        else:
            self.ruta=ruta

    def type (self,tipo):
        self.tipo=tipo

    def creacionBucket(self):
        #limpiando path
        self.ruta=self.ruta.replace('/',  '', 1)
        #Creando archivo o carpeta o ambos
        s3 = boto3.resource('s3')
        print("conectado al buked")
        s3.Object("202001574", "archivos/"+self.ruta+self.nombre).put(Body=self.contenido)
        print("Archivo creado al bucket")
    




















    
    def creacionServer(self):
        rs={"nombre":self.nombre,"contenido":self.contenido,"ruta":self.ruta}
        os.makedirs(rutaSer+rs["ruta"], exist_ok=True)  # creo por si no existe
        # renombro si existe
        reName = _G.creRenameL(rutaSer+rs["ruta"], rs["nombre"])
        f = open(rutaSer+rs["ruta"]+reName, "a+")  # abriendo y creando
        f.write(f.read()+rs["contenido"])
        f.close()  # siempre cerrar