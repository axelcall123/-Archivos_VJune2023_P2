import os
import boto3
class Recovery:
    def __init__ (self):
        self.tipoA=""
        self.tipoDe=""
        self.ip=""
        self.port=""
        self.name=""

    def typeTo(self,tipoDe):
        self.tipoDe=tipoDe

    def typeFrom(self,tipoA):
        self.tipoA=tipoA

    def Ip(self,ip):
        self.ip=ip

    def Port(self,port):
        self.port=port

    def Name(self,name):
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

        