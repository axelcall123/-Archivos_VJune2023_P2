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
        self.name=name

    def openBucket(self):
        print("openBucket")
        print(self.tipo)
        print(self.ip)
        print(self.port)
        print(self.name)
