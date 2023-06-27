import boto3
from Analizador.Comandos.varDef import *
import Analizador.Comandos._general as _G
import os
class Open:
    def __init__ (self):
        self.tipo=""
        self.ip=""
        self.port=""
        self.name=""

    def type(self,tipo):
        self.tipo=tipo

    def Ip(self,ip):
        self.ip=ip

    def Port(self,port):
        self.port=port

    def Name(self,name):
        if('"' in name):
            self.name=name.replace("\"", "" )
        else:
            self.name=name

    def openBucket(self):
        if "/" in self.name:
            self.name=self.name.replace('/',  '', 1)
        s3_client = boto3.client('s3')
        nombre_bucket = '202001574'
        ruta_archivo_s3 = 'archivos/'+self.name
        response = s3_client.get_object(Bucket=nombre_bucket, Key=ruta_archivo_s3)
        contenido = response['Body'].read().decode('utf-8')
        return contenido
    


    def openServer(self):
        ruta=""
        if "/" in self.name:
            self.name = rutaSer+ self.name
        else:
            ruta=os.path.join(rutaSer,self.name)
        if os.path.exists(ruta) and '.txt' in self.Name:
            return _G.readTxt(ruta)
        else:
            return 'No existe el archivo, o es un fodler'