import os
import sys
import tempfile
#from Aplicacion.variablesGlobales import temporalFile
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
        print(self.nombre)
        print(self.contenido)
        print(self.ruta)
        print(self.tipo)