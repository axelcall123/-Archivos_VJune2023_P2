import tkinter as tk
import tkinter.font as tkFont
import requests
import json
class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_635 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_635["font"] = ft
        GLabel_635["fg"] = "#333333"
        GLabel_635["justify"] = "center"
        GLabel_635["text"] = "label"
        GLabel_635.place(x=70, y=80, width=70, height=25)

        GLabel_168 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_168["font"] = ft
        GLabel_168["fg"] = "#333333"
        GLabel_168["justify"] = "center"
        GLabel_168["text"] = "label"
        GLabel_168.place(x=70, y=150, width=70, height=25)

        GCheckBox_722 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_722["font"] = ft
        GCheckBox_722["fg"] = "#333333"
        GCheckBox_722["justify"] = "center"
        GCheckBox_722["text"] = "CheckBox"
        GCheckBox_722.place(x=160, y=80, width=70, height=25)
        GCheckBox_722["offvalue"] = "0"
        GCheckBox_722["onvalue"] = "1"
        GCheckBox_722["command"] = self.GCheckBox_722_command

        GCheckBox_306 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_306["font"] = ft
        GCheckBox_306["fg"] = "#333333"
        GCheckBox_306["justify"] = "center"
        GCheckBox_306["text"] = "CheckBox"
        GCheckBox_306.place(x=160, y=160, width=70, height=25)
        GCheckBox_306["offvalue"] = "0"
        GCheckBox_306["onvalue"] = "1"
        GCheckBox_306["command"] = self.GCheckBox_306_command

        GButton_400 = tk.Button(root)
        GButton_400["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_400["font"] = ft
        GButton_400["fg"] = "#000000"
        GButton_400["justify"] = "center"
        GButton_400["text"] = "Button"
        GButton_400.place(x=260, y=120, width=70, height=25)
        GButton_400["command"] = self.GButton_400_command

    def GCheckBox_722_command(self):
        print("command1")
        res = requests.request(
            method='PUT',  # PUEDE EXISTAR MAS DE UN METDO EN LA MISMA URL
            url="http://192.168.0.29:1000/uploadS",  # URL METODO
            json={"url": "D:/AXEL/DESCARGAS/p2.jpg", "key": "p2.jpg"}  # LO QUE ENVIO
        )
        print("tkitner>\n\tcomando:\n", json.loads(res.text))

    def GCheckBox_306_command(self):
        print("command2")

    def GButton_400_command(self):
        #click me
        #metodo postman
        #rsp = requests.get("http://192.168.0.29:1000/get_data?url=123456&saludo=abc")
        #print(f"commando res:{rsp.content}")
        res = requests.request(
            method="GET",#PUEDE EXISTAR MAS DE UN METDO EN LA MISMA URL
            url="http://192.168.0.29:1000/get_data",#URL METODO
            json={"txt": "text","hola": "meme"}#LO QUE ENVIO
        )
        print("tkitner>",json.loads(res.text))
        res = requests.get(
            url="http://192.168.0.29:1000/get_data",  # URL METODO
            json={"nel": "miS", "hola": "memeS"}  # LO QUE ENVIO
        )
        print("tkitner>", json.loads(res.text))

        



root = tk.Tk()
app = App(root)
root.mainloop()
