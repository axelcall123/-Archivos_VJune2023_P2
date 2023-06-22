import boto3
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
            nombre_archivo = self.de
            nombre_bucket = '202001574'
            nombreFile=self.getNameFile(self.de)
            ruta_archivo_destino = self.a+nombreFile
            s3_client.copy_object(Bucket=nombre_bucket, CopySource=f'{nombre_bucket}/{nombre_archivo}', Key=ruta_archivo_destino)
        #copy directorio
        else:
            s3_client = boto3.client('s3')
            nombre_bucket = '202001574'
            directorio_origen = self.de
            directorio_destino = self.a+self.de
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


