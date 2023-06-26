import requests
################################################################################
url='http://3.15.29.9:3000'
class Leer:
    def __init__(self,):
        pass

    def comando(self, arreglo):
        for element in arreglo:
            for comando in element:
                if (comando == "create"):  # !Comando Create
                    #creando objeto 
                    myobjCreate = {'name': '',
                             'body': '',
                             'path': '',
                             'type': ''}
                    for parametros in element:
                        if (parametros != "create"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-name->"):
                                    myobjCreate['name']=elementos2[1]
                                elif (elementos2[0] == "-path->"):
                                    myobjCreate['path']=elementos2[1]
                                elif (elementos2[0] == "-body->"):
                                    myobjCreate['body']=elementos2[1]
                                else:
                                   myobjCreate['type']=elementos2[1]
                            #Enviando peticion Create
                            #Creando direccion (Cambiar url si se llega a cambiar la IP de la instacia)
                            comandoUrl = url+"/create"
                            # "x" tiene el return de la peticion enviada
                            x = requests.post(comandoUrl, json = myobjCreate)
                            #imprimiendo json
                            print(myobjCreate)
                            #imprimiendo return
                            print(x)
                if (comando == "delete"):  # !Comando delete
                    myobjDelete = {'name': '',
                                    'path': '',
                                    'type': ''}
                    for parametros in element:
                        if (parametros != "delete"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    myobjDelete['path']=elementos2[1]
                                elif (elementos2[0] == "-name->"):
                                    myobjDelete['name']=elementos2[1]
                                else:
                                    myobjDelete['type']=elementos2[1]
                            comandoUrl = url+"/delete"
                            x = requests.post(comandoUrl, json = myobjDelete)
                            print(myobjDelete)
                            print(x)
                if (comando == "copy"):  # !Comando copy
                    myobjCopy = {'from': '',
                                'to': '',
                                'type_to': '',
                                'type_from': ''}
                    for parametros in element:
                        if (parametros != "copy"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-from->"):
                                    myobjCopy['from']=elementos2[1]
                                elif (elementos2[0] == "-to->"):
                                    myobjCopy['to']=elementos2[1]
                                elif (elementos2[0] == "-type_to->"):
                                    myobjCopy['type_to']=elementos2[1]
                                else:
                                    myobjCopy['type_from']=elementos2[1]
                            comandoUrl = url+"/copy"
                            x = requests.post(comandoUrl, json = myobjCopy)
                            print(myobjCopy)
                            print(x)
                if (comando == "transfer"):  # !Comando trasnfer
                    myobjTransfer = {'from': '',
                                'to': '',
                                'type_to': '',
                                'type_from': ''}
                    for parametros in element:
                        if (parametros != "transfer"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-from->"):
                                    myobjTransfer['from']=elementos2[1]
                                elif (elementos2[0] == "-to->"):
                                    myobjTransfer['to']=elementos2[1]
                                elif (elementos2[0] == "-type_to->"):
                                    myobjTransfer['type_to']=elementos2[1]
                                else:
                                    myobjTransfer['type_from']=elementos2[1]
                            comandoUrl = url+"/transfer"
                            x = requests.post(comandoUrl, json = myobjTransfer)
                            print(myobjTransfer)
                            print(x)
                if (comando == "rename"):  # !Comando rename
                    myobjRename = {'path': '',
                                'name': '',
                                'type': ''}
                    for parametros in element:
                        if (parametros != "rename"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    myobjRename['path']=elementos2[1]
                                elif (elementos2[0] == "-name->"):
                                    myobjRename['name']=elementos2[1]
                                else:
                                    myobjRename['type']=elementos2[1]
                            comandoUrl = url+"/rename"
                            x = requests.post(comandoUrl, json = myobjRename)
                            print(myobjRename)
                            print(x)
                if (comando == "modify"):  # !Comando modify
                    myobjModify = {'path': '',
                                'body': '',
                                'type': ''}
                    for parametros in element:
                        if (parametros != "modify"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    myobjModify['path']=elementos2[1]
                                elif (elementos2[0] == "-body->"):
                                    myobjModify['body']=elementos2[1]
                                else:
                                    myobjModify['type']=elementos2[1]
                            comandoUrl = url+"/modify"
                            x = requests.post(comandoUrl, json = myobjModify)
                            print(myobjModify)
                            print(x)
                if (comando == "backup"):  # !Comando backup
                    myobjBackup = {'type_to': '',
                                'type_from': '',
                                'ip': '',
                                'name': '',
                                'port': ''}
                    for parametros in element:
                        if (parametros != "backup"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-type_to->"):
                                    myobjBackup['type_to']=elementos2[1]
                                elif (elementos2[0] == "-type_from->"):
                                    myobjBackup['type_from']=elementos2[1]
                                elif(elementos2[0] == "-ip->"):
                                    myobjBackup['ip']=elementos2[1]
                                elif(elementos2[0] == "-port->"):
                                    myobjBackup['port']=elementos2[1]
                                else:
                                    myobjBackup['name']=elementos2[1]
                            comandoUrl = url+"/backup"
                            x = requests.post(comandoUrl, json = myobjBackup)
                            print(myobjModify)
                            print(x)
                if (comando == "recovery"):  # !Comando add
                    myobjRecovery = {'type_to': '',
                                'type_from': '',
                                'ip': '',
                                'name': '',
                                'port': ''}
                    for parametros in element:
                        if (parametros != "recovery"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-type_to->"):
                                    myobjRecovery['type_to']=elementos2[1]
                                elif (elementos2[0] == "-type_from->"):
                                   myobjRecovery['type_from']=elementos2[1]
                                elif(elementos2[0] == "-ip->"):
                                    myobjRecovery['ip']=elementos2[1]
                                elif(elementos2[0] == "-port->"):
                                    myobjRecovery['port']=elementos2[1]
                                else:
                                    myobjRecovery['name']=elementos2[1]
                            comandoUrl = url+"/recovery"
                            x = requests.post(comandoUrl, json = myobjRecovery)
                            print(myobjRecovery)
                            print(x)
                if (comando == "delete_all"):  # !Comando exec
                    myobjDelete_all = {'type': ''}
                    for parametros in element:
                        if (parametros != "delete_all"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-type->"):
                                    myobjDelete_all['type']=elementos2[1]
                            comandoUrl = url+"/delete_all"
                            x = requests.post(comandoUrl, json = myobjDelete_all)
                            print(myobjDelete_all)
                            print(x)
                if (comando == "open"):  # !Comando Open
                    #self.local=False
                    myobjOpen = {'ip': '',
                                'port': '',
                                'name': '',
                                'type': ''}
                    for parametros in element:
                        if (parametros != "open"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-type->"):
                                    myobjOpen['type']=elementos2[1]
                                elif(elementos2[0] == "-ip->"):
                                    myobjOpen['ip']=elementos2[1]
                                elif(elementos2[0] == "-port->"):
                                    myobjOpen['port']=elementos2[1]
                                else:
                                    myobjOpen['name']=elementos2[1]
                            comandoUrl = url+"/open"
                            x = requests.post(comandoUrl, json = myobjOpen)
                            print(myobjOpen)
                            print(x)


                      