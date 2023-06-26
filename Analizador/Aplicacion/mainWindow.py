import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox as MessageBox
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile

from Analizador.gramar import grammarInput
from Analizador.Comandos.esencial import Leer


from tkinter import *

class MainWindow:
    def __init__(self, root):
        self.root=root
        #setting title
        self.root.title("Consola")
        self.analizar=Leer()
        #setting window size
        width=1000
        height=800
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        bttnCerrar=tk.Button(self.root)
        bttnCerrar["activebackground"] = "#691111"
        bttnCerrar["anchor"] = "center"
        bttnCerrar["bg"] = "#1e90ff"
        bttnCerrar["cursor"] = "arrow"
        bttnCerrar["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        bttnCerrar["font"] = ft
        bttnCerrar["fg"] = "#ffffff"
        bttnCerrar["justify"] = "center"
        bttnCerrar["text"] = "Cerrar sesion"
        bttnCerrar["relief"] = "raised"
        bttnCerrar.place(x=800,y=700,width=150,height=70)
        bttnCerrar["command"] = self.bttnCerrar_command

        self.inputConsole=Text(self.root)
        self.inputConsole["borderwidth"] = "1px"
        self.inputConsole["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        self.inputConsole["font"] = ft
        self.inputConsole["fg"] = "#333333"
        self.inputConsole.place(x=50,y=140,width=720,height=300)

        self.outputConsole=Text(self.root)
        self.outputConsole["borderwidth"] = "1px"
        self.outputConsole["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        self.outputConsole["font"] = ft
        self.outputConsole["fg"] = "#333333"
        self.outputConsole.place(x=50,y=470,width=720,height=300)


        bttnEjecComando=tk.Button(self.root)
        bttnEjecComando["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnEjecComando["font"] = ft
        bttnEjecComando["fg"] = "#ffffff"
        bttnEjecComando["justify"] = "center"
        bttnEjecComando["text"] = "Ejec. Comando"
        bttnEjecComando.place(x=800,y=40,width=150,height=70)
        bttnEjecComando["command"] = self.bttnEjecComando_command

        bttnEjecFile=tk.Button(self.root)
        bttnEjecFile["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        bttnEjecFile["font"] = ft
        bttnEjecFile["fg"] = "#ffffff"
        bttnEjecFile["justify"] = "center"
        bttnEjecFile["text"] = "Cargar archivo"
        bttnEjecFile.place(x=50,y=40,width=720,height=70)
        bttnEjecFile["command"] = self.bttnEjecFile_command

    def bttnCerrar_command(self):
        self.root.destroy()

    def bttnEjecComando_command(self):
        stringInput=self.inputConsole.get("1.0", "end-1c")
        grammarInput(stringInput,self.analizar)

    def bttnEjecFile_command(self):
        file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*')])
        if file:
            content = file.read()
            #contenido de archivo subido
            print(content)
            file.close()
            



