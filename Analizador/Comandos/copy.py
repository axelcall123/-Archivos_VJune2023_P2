import os
import shutil
import tempfile
#from Aplicacion.variablesGlobales import temporalFile
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
        print(self.de)
        print(self.a)
        print(self.tipoDe)
        print(self.tipoA)