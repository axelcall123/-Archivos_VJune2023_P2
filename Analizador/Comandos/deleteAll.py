import boto3
import Analizador.Comandos._general as _G
from Analizador.Comandos.varDef import *
import os
class DeleteAll:
    def __init__ (self):
        self.tipo=""


    def type (self,tipo):
        self.tipo=tipo

    def borrarBucket(self):
        s3_client = boto3.client('s3')
        nombre_bucket = '202001574'
        response = s3_client.list_objects_v2(Bucket=nombre_bucket)
        for obj in response['Contents']:
            s3_client.delete_object(Bucket=nombre_bucket, Key=obj['Key'])
        print('Todos los directorios y archivos han sido eliminados.')




















    #mine
    def borrarServer(self):
        for item in os.listdir(rutaSer):
            _G.deleteSever(f'{rutaSer}/{item}')
        return 'todos los archivos y directorios han sido eliminados'
