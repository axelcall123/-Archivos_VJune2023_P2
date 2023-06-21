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
        print(self.contenido)
        print(self.ruta)
        print(self.tipo)