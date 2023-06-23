import os
import tempfile
import boto3
#from Aplicacion.variablesGlobales import temporalFile
class Delete:
    def __init__ (self,):
        self.ruta=""
        self.nombre=""
        self.tipo=""

    def path (self,ruta):
        if('"' in ruta):
            self.ruta=ruta.replace("\"", "" )
        else:
            self.ruta=ruta

    def name(self,nombre):
        if('"' in nombre):
            self.nombre=nombre.replace("\"", "" )
        else:
            self.nombre=nombre
    def type(self,tipo):
        self.tipo=tipo

    def borrarBucket(self):
        print(self.ruta)
        print(self.nombre)
        print(self.tipo)
        #limpiando path
        self.ruta=self.ruta.replace('/',  '', 1)
        #eliminando archivo
        if self.nombre!="":
            s3 = boto3.resource('s3')
            archivo_objeto = s3.Object("202001574", "Archivos/"+self.ruta+self.nombre)
            # Elimina el archivo del bucket
            archivo_objeto.delete()
            print("Archivo eliminado al bucket")
        #eliminado directorio
        else:
            client = boto3.client('s3')
            #todos los objetos en directorio
            allobjets=client.list_objects(Bucket="202001574")
            for a in allobjets['Contents']:
                if "Archivos/"+self.ruta in a['Key'] and a['Key'] != "Archivos/"+self.ruta:
                    #eliminando todos los objetos (al quedar vacio se elimina)
                    client.delete_object(Bucket='202001574', Key=a['Key'])
        



        
            

        
        
    

