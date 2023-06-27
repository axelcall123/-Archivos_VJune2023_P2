import boto3
from pathlib import Path
import os
from Analizador.Comandos.copy import Copy
import Analizador.Comandos._general as _G
from Analizador.Comandos.varDef import *
import requests
import json
class Backup:
    def __init__ (self):
        self.tipoA=""
        self.tipoDe=""
        self.ip=""
        self.port=""
        self.name=""

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

    def backupservertobucket(self):
        print(self.name)
        s3_client = boto3.client('s3')
        # Ruta del directorio local que deseas transferir
        directorio_local = './archivos/'
        # Nombre del bucket de Amazon S3
        nombre_bucket = '202001574'
        # Recorre el directorio y subdirectorios
        for ruta_archivo_local in Path(directorio_local).rglob('*'):
            if ruta_archivo_local.is_file():
                # Obtiene la ruta relativa del archivo
                ruta_relativa = str(ruta_archivo_local.relative_to(directorio_local))
                ruta_relativa=ruta_relativa.replace("\\","/")
                # Carga el archivo local en el bucket de Amazon S3
                s3_client.upload_file(str(ruta_archivo_local), nombre_bucket, self.name+"/"+ruta_relativa)
            
        return "Backup para bucket Nombre: "+self.name
    

    




    
    
    
    
    
    
    
    
    
    #mine
    def backupbuckettoserver(self):
        copy = Copy()
        copy.de = '/'
        copy.a = f'/{self.name}/'
        copy.copiarBucketToServer()

    def backupSend(self):
        if self.tipoDe=="server":#recorre en modo server
            res = _G.listadoJsonServer(rutaSer)
            print("json:",res)
            res = requests.get(
                url=f"http://{self.ip}:{self.port}/respuestaT",  # URL METODO
                json={"type_to": self.tipoA, "tyep_from": self.tipoDe, "name": self.name,
                      "archivos": _G.listadoJsonServer(rutaSer)}  # LO QUE ENVIO
            )
            print(res.text)
        elif self.tipoDe=="bucket":#recorro en modo bucket
            res = _G.listadoJsonBucket('/')
            print("json:", res)
            res = requests.get(
                url=f"http://{self.ip}:{self.port}/respuestaT",  # URL METODO
                json={"type_to": self.tipoA, "tyep_from": self.tipoDe, "name": self.name,
                      "archivos": _G.listadoJsonBucket('/')}  # LO QUE ENVIO
            )
            print(res.text)
        
    def backupReceive(self):#FIXME: falta la opcion 
        if self.tipoDe=="server":
            _G.recorrerJsonServer(f'{rutaSer}/{self.name}',self.archivos,self.tipoA)
        elif self.tipoDe == "bucket":
            _G.recorrerJsonBucket(
                f'{rutaSer}/{self.name}/', self.archivos, self.tipoA)
