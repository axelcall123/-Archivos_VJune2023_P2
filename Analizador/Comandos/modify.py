import boto3
class Modify:
    def __init__ (self,):
        self.contenido=""
        self.ruta=""
        self.tipo=""

    def body (self,contenido):
        if('"' in contenido):
            self.contenido=contenido.split("\"")[1]
        else:
            self.contenido=contenido
            

    def path(self,ruta):
        if('"' in ruta):
            self.ruta=ruta.replace("\"", "" )
        else:
            self.ruta=ruta
    
    def type (self,tipo):
        self.tipo=tipo

    def modificarBucket(self):
        self.ruta=self.ruta.replace('/',  '', 1)
        self.contenido=self.contenido.replace('"',  '')
        s3_client = boto3.client('s3')
        nombre_archivo = "archivos/"+self.ruta
        nombre_bucket = '202001574'
        contenido_modificado = self.contenido 
        s3_client.put_object(Body=contenido_modificado, Bucket=nombre_bucket, Key=nombre_archivo)
        print('Archivo modificado exitosamente.')