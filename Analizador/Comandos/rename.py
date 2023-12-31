import boto3
class Rename:
    def __init__ (self,):
        self.ruta=""
        self.nombre=""
        self.tipo=""

    def path (self,ruta):
        
        if('"' in ruta):
            self.ruta=ruta.replace("\"", "" )
        else:
            self.ruta=ruta
            

    def name(self,nombre):
        if('"' in nombre):
            self.nombre=nombre.replace("\"", "" )
        else:
            self.nombre=nombre
    
    def type (self,tipo):
        self.tipo=tipo

    def renombrarBucket(self):
        print(self.ruta)
        print(self.nombre)
        print(self.tipo)
        #limpiando path
        self.ruta=self.ruta.replace('/',  '', 1)
        #renombrando archivo
        if ".txt" in self.ruta:
            s3_client = boto3.client('s3')
            nombre_archivo_actual = "archivos/"+self.ruta
            print(nombre_archivo_actual)
            ruta=self.getRuta(self.ruta)
            nombre_archivo_nuevo = "archivos/"+ruta+self.nombre
            print(nombre_archivo_nuevo)
           
            nombre_bucket = '202001574'
            s3_client.copy_object(Bucket=nombre_bucket, CopySource={'Bucket': nombre_bucket, 'Key': nombre_archivo_actual}, Key=nombre_archivo_nuevo)
            s3_client.delete_object(Bucket=nombre_bucket, Key=nombre_archivo_actual)
            print('Archivo renombrado exitosamente.')
        #renombrando directorio
        else:
            s3_client = boto3.client('s3')
            nombre_bucket = '202001574'
            directorio_actual = "archivos/"+self.ruta
            print({"nombre_archivo_actual":self.ruta})
            ruta=self.getRuta(self.ruta)
            self.nombre=self.nombre.replace('/',  '', 1)
            directorio_nuevo = "archivos/"+ruta+self.nombre
            print({"nombre_archivo_nuevo":ruta+self.nombre})
            response = s3_client.list_objects_v2(Bucket=nombre_bucket, Prefix=directorio_actual)
            for obj in response['Contents']:
                nombre_objeto_actual = obj['Key']
                nombre_objeto_nuevo = nombre_objeto_actual.replace(directorio_actual, directorio_nuevo)
                s3_client.copy_object(Bucket=nombre_bucket, CopySource=f'{nombre_bucket}/{nombre_objeto_actual}', Key=nombre_objeto_nuevo)
                s3_client.delete_object(Bucket=nombre_bucket, Key=nombre_objeto_actual)
            print('Directorio renombrado exitosamente.')

    def getRuta(self,path):
        list=path.split("/")
        nuevoPath=""
        if ".txt" in path:
            for element in list:
                if(element==list[-1]):
                    break
                nuevoPath=nuevoPath+element+"/"
            print(nuevoPath)
            return nuevoPath
        else:
            for element in list:
                if(element==list[-2]):
                    break
                nuevoPath=nuevoPath+element+"/"
            print(nuevoPath)
            return nuevoPath


