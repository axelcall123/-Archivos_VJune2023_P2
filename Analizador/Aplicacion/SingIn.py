import tkinter.font as tkFont
from tkinter import messagebox as MessageBox
import tkinter as tk
import tkinter.font as tkFont
from Analizador.Aplicacion.variablesGlobales import listaUsuarios#, temporalFile
from Analizador.Aplicacion.mainWindow import MainWindow
import tempfile

class Login:
    def __init__(self, root):

        self.root=root
        #setting title
        self.root.title("Login")
        #setting window size
        width = 452
        height = 411
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        GLabel_529 = tk.Label(self.root)
        GLabel_529["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_529["font"] = ft
        GLabel_529["fg"] = "#333333"
        GLabel_529["justify"] = "center"
        GLabel_529["text"] = ""
        GLabel_529.place(x=60, y=40, width=300, height=323)

        GLabel_788 = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_788["font"] = ft
        GLabel_788["fg"] = "#333333"
        GLabel_788["justify"] = "center"
        GLabel_788["text"] = "Sign In"
        GLabel_788.place(x=80, y=50, width=70, height=25)

        GLabel_695 = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_695["font"] = ft
        GLabel_695["fg"] = "#333333"
        GLabel_695["justify"] = "center"
        GLabel_695["text"] = "User Name:"
        GLabel_695.place(x=80, y=100, width=70, height=25)

        GLabel_740 = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_740["font"] = ft
        GLabel_740["fg"] = "#333333"
        GLabel_740["justify"] = "center"
        GLabel_740["text"] = "Password:"
        GLabel_740.place(x=80, y=170, width=70, height=25)

        GButton_691 = tk.Button(self.root)
        GButton_691["anchor"] = "center"
        GButton_691["bg"] = "#40b840"
        GButton_691["borderwidth"] = "0px"
        GButton_691["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=10)
        GButton_691["font"] = ft
        GButton_691["fg"] = "#ffffff"
        GButton_691["justify"] = "center"
        GButton_691["text"] = "SIGN IN"
        GButton_691.place(x=170, y=260, width=70, height=25)
        GButton_691["command"] = self.GButton_691_command

        self.inputUserName = tk.Entry(self.root)
        self.inputUserName["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.inputUserName["font"] = ft
        self.inputUserName["fg"] = "#333333"
        self.inputUserName["justify"] = "center"
        self.inputUserName["text"] = "user"
        self.inputUserName.place(x=130, y=130, width=152, height=30)

        self.inputPassword = tk.Entry(self.root)
        self.inputPassword["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.inputPassword["font"] = ft
        self.inputPassword["fg"] = "#333333"
        self.inputPassword["justify"] = "center"
        self.inputPassword["text"] = "pass"
        self.inputPassword.place(x=130, y=210, width=146, height=30)


    def GButton_691_command(self):
        #self.root.destroy()
        #self.test()
        #self.login()
        if((self.inputUserName.get()!="")&(self.inputPassword.get()!="")):   
                #llenando los campos 
                usuarioLogin= {
                "UserName": self.inputUserName.get(),
                "Password": self.inputPassword.get()
                }
                self.root.destroy()
                self.comprobandoCredenciales(usuarioLogin)
                self.login()
        else:
            MessageBox.showerror("Error!", "Llena todos los campos")

    def test(self):
        self.root=tk.Tk()
        MainWindow(self.root)
        self.root.mainloop()

    def login(self):
        root=tk.Tk()
        app = Login(root)
        root.mainloop()

    
    
    def comprobandoCredenciales(self,loginUser):
        global listaUsuarios
        contador=0
        #bitacora<<<<>>>>>
        for element in listaUsuarios:
            if((element.get("UserName")==loginUser.get("UserName"))):
                if((element.get("Password")==loginUser.get("Password"))):
                    #obteniendo usuario logeado
                    global usuarioActual
                    usuarioActual ={
                        "UserName": element.get("UserName"),
                        "Password": element.get("Password")
                    }
                    MessageBox.showinfo("", "Usuario logeado con exito")
                    #bitacora<<<<>>>>>
                    self.root=tk.Tk()
                    MainWindow(self.root)
                    self.root.mainloop()
                    break
                else:
                    #bitacora<<<<>>>>>
                    MessageBox.showinfo("Error!", "Contraseña incorrecta")
                    break
            contador=contador+1
            if(len(listaUsuarios)==contador):
                #bitacora<<<<>>>>>
                MessageBox.showerror("Error!", "No se encontro ese nombre de usuario")

                


