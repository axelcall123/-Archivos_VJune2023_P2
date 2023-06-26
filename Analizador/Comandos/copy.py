import boto3
from pathlib import Path
from Analizador.Comandos.varDef import *
import Analizador.Comandos._general as _G
import os
class Copy:
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

    def copiarBucketToBucket(self):
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
        #copy directorio
        else:
            s3_client = boto3.client('s3')
            nombre_bucket = '202001574'
            directorio_origen = "archivos/"+self.de
            directorio_destino = "archivos/"+self.a+self.de
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
            print('Directorio copiado exitosamente.')

    def getNameFile(self,path):
        lista=path.split("/")
        name=""
        for element in lista:
            if(".txt" in element):
                name=element
        return name
    
    def copiarServerToBucket(self):
        if ".txt" in self.de:# si es un archivo 
            s3_client = boto3.client('s3')
            print({"from":"./archivos/"+self.de})
            self.a=self.a.replace('/',  '', 1)
            nombreFile=self.getNameFile(self.de)
            print({"to":"archivos/"+self.a})
            s3_client.upload_file("./archivos/"+self.de, "202001574", "archivos/"+self.a+nombreFile)
        #copy directorio
        else:
            s3_client = boto3.client('s3')
            # Ruta del directorio local que deseas transferir
            directorio_local = './archivos/'+self.de
            print({"from":"./archivos/"+self.de})
            # Nombre del bucket de Amazon S3
            nombre_bucket = '202001574'
            # Recorre el directorio y subdirectorios
            for ruta_archivo_local in Path(directorio_local).rglob('*'):
                    if ruta_archivo_local.is_file():
                            # Obtiene la ruta relativa del archivo
                            ruta_relativa = str(ruta_archivo_local.relative_to(directorio_local))
                            ruta_relativa=ruta_relativa.replace("\\","/")
                            # Carga el archivo local en el bucket de Amazon S3
                            s3_client.upload_file(str(ruta_archivo_local), nombre_bucket, "archivos"+self.a+ruta_relativa)
                            print({"to":"archivos/"+self.a+ruta_relativa})
                    print('Elementos transferidos exitosamente al bucket de Amazon S3.')

    















    def copiarServerToServer(self):
        rs={"from":self.de,"to":self.a}
        return _G.copySever(rutaSer+rs["to"], rutaSer+rs["from"])
    
    def copiarBucketToServer(self):
        s3 = boto3.client('s3')
        name='202001574'
        rs={"from":self.de,"to":self.a}#FIXME cambiar a self.de y self.a
        if not _G.existeBucket(s3, name, f'{rutaB}{rs["from"]}'):
            return 'no existe ruta en el bucket'
        if '.txt' in rs["from"]:  # copio solo un archivo
            #                         ruta nombre                              nombre
            rename = _G.creRenameL(os.path.join(
                rutaSer, rs["to"]), rs['from'].split('/')[-1])
            s3.download_file(name, f'{rutaB}{rs["from"]}', os.path.join(
                rutaSer+rs["to"], rename))  # ubicacion boto,ubicacion local
            return 'copio el archivo'
        else:  # copio una carpeta
            response = s3.list_objects_v2(
                Bucket=name, Prefix=f'{rutaB}{rs["from"]}')  # obtiene todo el listado
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
        return 'copio el folder'
