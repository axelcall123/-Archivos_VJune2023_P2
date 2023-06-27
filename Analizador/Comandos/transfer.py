import boto3
from pathlib import Path
import os
import shutil
from Analizador.Comandos.varDef import *
import Analizador.Comandos._general as _G
class Transfer:
    def __init__ (self,):
        self.de=""
        self.a=""
        self.tipoDe=""
        self.tipoA=""

    def desde (self,de):
        if('"' in de):
            self.de=de.replace("\"", "" )
        else:
            self.de=de

    def to(self,a):
        if('"' in a):
            self.a=a.replace("\"", "" )
        else:
            self.a=a

    def typeTo(self,tipoDe):
        self.tipoDe=tipoDe

    def typeFrom(self,tipoA):
        self.tipoA=tipoA

    def trasferirBucketToBucket(self):
        #limpiando path
        self.de=self.de.replace('/',  '', 1)
        self.a=self.a.replace('/',  '', 1)
        #copy archivo
        if ".txt" in self.de:# si es un archivo 
            s3_client = boto3.client('s3')
            nombre_archivo = "archivos/"+self.de
            nombre_bucket = '202001574'
            nombreFile=self.getNameFile(self.de)
            ruta_archivo_destino = "archivos/"+self.a+nombreFile
            s3_client.copy_object(Bucket=nombre_bucket, CopySource=f'{nombre_bucket}/{nombre_archivo}', Key=ruta_archivo_destino)
            s3_client.delete_object(Bucket=nombre_bucket, Key=nombre_archivo)
        #copy directorio
        else:
            s3_client = boto3.client('s3')
            nombre_bucket = '202001574'
            directorio_origen = "archivos/"+self.de
            directorio_destino = "archivos/"+self.a
            # Obtiene la lista de objetos en el directorio de origen
            response = s3_client.list_objects_v2(Bucket=nombre_bucket, Prefix=directorio_origen)
            # Copia cada objeto dentro del directorio de origen al directorio de destino
            for obj in response['Contents']:
                # Obtiene el nombre del archivo dentro del directorio de origen
                nombre_archivo_origen = obj['Key']
                # Construye el nombre de archivo de destino
                nombre_archivo_destino = directorio_destino + nombre_archivo_origen.replace(directorio_origen, '')
                # Realiza la copia del archivo
                s3_client.copy_object(Bucket=nombre_bucket, CopySource=f'{nombre_bucket}/{nombre_archivo_origen}', Key=nombre_archivo_destino)
                s3_client.delete_object(Bucket='202001574', Key=nombre_archivo_origen)

    def getNameFile(self,path):
        lista=path.split("/")
        name=""
        for element in lista:
            if(".txt" in element):
                name=element
        return name
    
    def trasferirServerToBucket(self):
        if ".txt" in self.de:# si es un archivo
            s3_client = boto3.client('s3')
            print({"from":"./archivos/"+self.de})
            nombreFile=self.getNameFile(self.de)
            print({"to":"archivos/"+self.a+nombreFile})
            s3_client.upload_file("./archivos/"+self.de, "202001574", "archivos/"+self.a+nombreFile)
            #os.remove("./archivos/"+self.de)
        # si es un directorio
        else:
            s3_client = boto3.client('s3')
            # Ruta del directorio local que deseas transferir
            directorio_local = "./archivos/"+self.de
            print({"from":directorio_local})
            # Nombre del bucket de Amazon S3
            nombre_bucket = '202001574'
            # Recorre el directorio y subdirectorios
            for ruta_archivo_local in Path(directorio_local).rglob('*'):
                if ruta_archivo_local.is_file():
                    # Obtiene la ruta relativa del archivo
                    ruta_relativa = str(ruta_archivo_local.relative_to(directorio_local))
                    ruta_relativa=ruta_relativa.replace("\\","/")
                    # Carga el archivo local en el bucket de Amazon S3
                    print({"to":"archivos/"+ruta_relativa})
                    s3_client.upload_file(str(ruta_archivo_local), nombre_bucket, "archivos/"+ruta_relativa)
            for archivo in os.listdir(directorio_local):
                ruta_archivo = os.path.join(directorio_local, archivo)
                # Eliminar el archivo si es un archivo
                if os.path.isfile(ruta_archivo):
                    os.remove(ruta_archivo)
                    # Eliminar el directorio si es un subdirectorio
                elif os.path.isdir(ruta_archivo):
                    shutil.rmtree(ruta_archivo)











    def trasferirBucketToServer(self):
        s3 = boto3.client('s3')
        name="202001574"
        rs={"from":self.de,"to":self.a}
        if not _G.existeBucket(s3, name, f'{rutaB}{rs["from"]}'):
            return 'no existe ruta en el bucket'
        if '.txt' in rs["from"]:  # copio solo un archivo
            #                         ruta nombre                              nombre
            rename = _G.creRenameL(os.path.join(
                rutaSer, rs["to"]), rs['from'].split('/')[-1])
            s3.download_file(name, f'{rutaB}{rs["from"]}', os.path.join(
                rutaSer+rs["to"], rename))  # ubicacion boto,ubicacion local
            s3.delete_object(name, f'{rutaB}{rs["from"]}')  # extra borrar file
            return 'transfirio el archivo'
        else:  # copio una carpeta
            response = s3.list_objects_v2(
                Bucket=name, Prefix=f'{rutaB}{rs["from"]}')  # obtiene todo el listado
            folders = []
            for obj in response['Contents']:
                print(obj['Key'])
                if not obj['Key'].endswith('/'):  # solo files
                    # obtengo la ruta del bucket sin el nombre
                    relativePath = _G.listado(obj['Key'])
                    # quito la parte de la ruta del bucket, que me causa problemas
                    relativePath = relativePath.replace(
                        f'{rutaB}{rs["from"]}', '')
                    # agrego la ruta del server
                    relativePath = os.path.join(rutaSer+rs["to"], relativePath)
                    os.makedirs(relativePath, exist_ok=True)  # creo la carpeta
                    rename = _G.creRenameL(
                        relativePath, obj['Key'].split('/')[-1])  # renombro
                    #                         ruta nombre                              nombre
                    s3.download_file(name, obj["Key"], os.path.join(
                        relativePath, rename))  # ubicacion boto,ubicacion local
                    # extra borrar file
                    s3.delete_object(Bucket=name, Key=obj["Key"])
                else:
                    folders.append(obj['Key'])
            for i in reversed(folders):  # borrar todos los folders
                if i != f'{rutaB}{rs["from"]}':
                    s3.delete_object(Bucket=name, Key=i)
        return 'tranfiero json'

    def trasferirServerToServer(self):
        rs={"from":self.de,"to":self.a}
        return _G.transferSersver(rutaSer+rs["to"], rutaSer+rs["from"])