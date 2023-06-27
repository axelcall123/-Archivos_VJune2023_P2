import boto3
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