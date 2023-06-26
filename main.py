from Analizador.gramar import gramarMain
from Analizador.Comandos.esencial import Leer
from Analizador.Aplicacion.SingIn import Login
from Analizador.Comandos.cripto import decrypt_hex_string
from Analizador.Aplicacion.variablesGlobales import listaUsuarios
import tkinter as tk
#pruebas
#resultado = gramarMain()
#analizar = Leer()
#analizar.comando(resultado)
#archivo=input()
archivo = "miausuarios.txt"
#contiene todos los usuarios con sus respectivas contraseñas

class Main():
    def __init__(self,):
        pass

    def login(self):
        pass
        root = tk.Tk()
        app = Login(root)
        root.mainloop()

    #Agregando a la lista usuarios
    def listaUsuariosFuction(self, string):
        leer = string.split("\n")
        contador = 0
        usuario = ""
        password = ""
        for element in leer:
            #identificando Usuario
            if (contador % 2 == 0):
                usuario = element
            #identificando Usuario contraseña
            elif (contador % 2 == 1):
                #desencriptando contraseñas
                #password = decrypt_hex_string(b"miaproyecto12345", bytearray.fromhex(element))
                password = decrypt_hex_string(b"miaproyecto12345", element)
                usuarios = {
                    "UserName": usuario,
                    "Password": password
                }
                print(usuarios)
                global listaUsuarios
                listaUsuarios.append(usuarios)
            contador = contador+1
        #Ejecutando login
        self.login()

    def test(self):
        resultado = gramarMain()
        analizar = Leer()
        for res in resultado:
            print(res)
        analizar.comando(resultado)

    #Obteniendo String del archivo de usuarios
    def leerUsuarios(self):
        f = open("./"+archivo, "r")  # abriendo y creando
        input = f.read()
        self.listaUsuariosFuction(input)

a=Main()
a.leerUsuarios()