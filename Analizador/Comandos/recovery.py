import os
import boto3
from Analizador.Comandos.copy import Copy
import Analizador.Comandos._general as _G
from Analizador.Comandos.varDef import *
import requests
import json
class Recovery:
    def __init__ (self):
        self.tipoA=""
        self.tipoDe=""
        self.ip=""
        self.port=""
        self.name=""
        self.archivos={}#FIXME:only test

    def typeTo(self,tipoDe):
        if('"' in tipoDe):
            self.tipoDe=tipoDe.replace("\"", "" )
        else:
            self.tipoDe=tipoDe

    def typeFrom(self,tipoA):
        if('"' in tipoA):
            self.tipoA=tipoA.replace("\"", "" )
        else:
            self.tipoA=tipoA

    def Ip(self,ip):
        self.ip=ip

    def Port(self,port):
        self.port=port

    def Name(self,name):
        if('"' in name):
            self.name=name.replace("\"", "" )
        else:
            self.name=name

    def recoveryBuckettoServer(self):
        # Crea una instancia del cliente de Amazon S3
        s3_client = boto3.client('s3')
        # Nombre del bucket de Amazon S3
        nombre_bucket = '202001574'
        # Ruta del directorio en el bucket que deseas descargar
        ruta_directorio_s3 = self.name
        # Directorio local donde se guardarán los archivos descargados
        directorio_local = './archivos/'+self.name
        # Recorre los archivos y subdirectorios dentro del directorio en el bucket
        response = s3_client.list_objects_v2(Bucket=nombre_bucket, Prefix=ruta_directorio_s3)
        for obj in response['Contents']:
            # Obtiene la ruta relativa del archivo en el bucket
            ruta_relativa = os.path.relpath(obj['Key'], ruta_directorio_s3)
            # Crea el directorio local si no existe
            directorio_local_archivo = os.path.join(directorio_local, ruta_relativa)
            os.makedirs(os.path.dirname(directorio_local_archivo), exist_ok=True)
            # Descarga el archivo desde el bucket
            s3_client.download_file(nombre_bucket, obj['Key'], directorio_local_archivo)
            print('Directorio descargado exitosamente desde el bucket de Amazon S3.')

        

















    #mine
    def recoveryServertobucket(self):
        copy = Copy()
        copy.de = '/'
        copy.a = f'/{self.name}/'
        copy.copyservetobucket()
        print()

    def recoveryReceive(self):# here<--------------------
        if self.tipoDe == "server":
            res = requests.get(
                url=f"http://{self.ip}:{self.port}/backupg",  #URL METODO
                json={"type_to": self.tipoA, "tyep_from": self.tipoDe,
                      "name": self.name, "archivos": self.archivos}  #LO QUE ENVIO
            )
            # _G.recorrerJsonServer(f'{rutaSer}/{self.name}',self.archivos,self.tipoA,self.name) #only tests FIXME:cambiar depues del test
            #{rutaSer}/{self.name} | {rutaSer}
            _G.recorrerJsonServer(f'{rutaSer}/{self.name}',res["archivos"],self.tipoA,self.name) #original
            return res.text
        elif self.tipoDe == "bucket":
            res = requests.get(
                url=f"http://{self.ip}:{self.port}/backupg",  # URL METODO
                json={"type_to": self.tipoA, "tyep_from": self.tipoDe,
                      "name": self.name, "archivos": self.archivos}  # LO QUE ENVIO
            )
            # _G.recorrerJsonBucket(f'{rutaSer}/', self.archivos, self.tipoA,self.name) #only tests
            _G.recorrerJsonBucket(f'{rutaSer}/', self.archivos, self.tipoA,self.name) #original
            return res.text
    def recoverySend(self):
        if self.tipoDe == "server":  
            res = _G.listadoJsonServer(rutaSer+'/'+self.name)
            return json.loads("{"+res+"}")
        elif self.tipoDe == "bucket":  
            res = _G.listadoJsonBucket(f'{self.name}/')
            return json.loads("{"+res+"}")