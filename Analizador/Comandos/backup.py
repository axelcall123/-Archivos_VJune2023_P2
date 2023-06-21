
class Backup:
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

    def backupBuckettoBucket(self):
        print("BackupB2B")
        print(self.tipoA)
        print(self.tipoDe)
        print(self.ip)
        print(self.port)
        print(self.name)
