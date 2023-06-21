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