
from Comandos.create import Create
from Comandos.delete import Delete
from Comandos.copy import Copy
from Comandos.transfer import Transfer
from Comandos.rename import Rename
from Comandos.modify import Modify
from Comandos.backup import Backup
from Comandos.recovery import Recovery
from Comandos.deleteAll import DeleteAll
from Comandos.open import Open


class Leer:
    def __init__(self,):
        pass

    def comando(self, arreglo):
        for element in arreglo:
            # cuales comandos
            for comando in element:
                # Separando comandos
                if (comando == "create"):  # !Comando Create y self.self.local es True
                    #self.local=False
                    comandoCreate = Create()
                    for parametros in element:
                        if (parametros != "create"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-name->"):
                                    comandoCreate.name(elementos2[1])
                                elif (elementos2[0] == "-path->"):
                                    comandoCreate.path(elementos2[1])
                                elif (elementos2[0] == "-body->"):
                                    comandoCreate.body(elementos2[1])
                                else:
                                    comandoCreate.type(elementos2[1])
                            #creando archivo
                            if (comandoCreate.tipo == "bucket"):
                                comandoCreate.creacionBucket()
                            #else:
                            #    comandoCreate.creacionServer()
                if (comando == "delete"):  # !Comando delete
                    #self.local=False 
                    comandoDelete = Delete()
                    for parametros in element:
                        if (parametros != "delete"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoDelete.path(elementos2[1])
                                elif (elementos2[0] == "-name->"):
                                    comandoDelete.name(elementos2[1])
                                else:
                                    comandoDelete.type(elementos2[1])
                            #! Dependiento TYPE
                            if (comandoDelete.tipo == "bucket"):
                                comandoDelete.borrarBucket()
                            #else:
                            #    comandoDelete.borrarCloud()
                if (comando == "copy"):  # !Comando copy
                    #self.local=False
                    comandoCopy = Copy()
                    for parametros in element:
                        if (parametros != "copy"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-from->"):
                                    comandoCopy.desde(elementos2[1])
                                elif (elementos2[0] == "-to->"):
                                    comandoCopy.to(elementos2[1])
                                elif (elementos2[0] == "-type_to->"):
                                    comandoCopy.typeTo(elementos2[1])
                                else:
                                    comandoCopy.typeFrom(elementos2[1])

                            #! Dependiento TYPE
                            if (comandoCopy.tipoA=="bucket")&(comandoCopy.tipoDe=="bucket"):
                                comandoCopy.copiarBucketToBucket()
                            #elif (comandoCopy.tipoA=="server")&(comandoCopy.tipoDe=="server"):
                                #comandoCopy.copiarServerToServer()
                            #elif (comandoCopy.tipoA=="bucket")&(comandoCopy.tipoDe=="server"):
                                #comandoCopy.copiarBuckettoServer()
                            #else:
                                #comandoCopy.copiarServerToBucket()
                if (comando == "transfer"):  # !Comando trasnfer
                    #self.local=False
                    comandoTransfer = Transfer()
                    for parametros in element:
                        if (parametros != "transfer"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-from->"):
                                    comandoTransfer.desde(elementos2[1])
                                elif (elementos2[0] == "-to->"):
                                    comandoTransfer.to(elementos2[1])
                                elif (elementos2[0] == "-type_to->"):
                                    comandoTransfer.typeTo(elementos2[1])
                                else:
                                    comandoTransfer.typeFrom(elementos2[1])
                            #! Dependiento del TYPE
                            if (comandoTransfer.tipoA=="bucket")&(comandoTransfer.tipoDe=="bucket"):
                                comandoTransfer.trasferirBucketToBucket()
                            #elif (comandoTransfer.tipoA=="server")&(comandoTransfer.tipoDe=="server"):
                                #comandoTransfer.copiarServerToServer()
                            #elif (comandoTransfer.tipoA=="bucket")&(comandoTransfer.tipoDe=="server"):
                                #comandoTransfer.copiarBuckettoServer()
                            #else:
                                #comandoTransfer.copiarServerToBucket()
                if (comando == "rename"):  # !Comando rename
                    #self.local=False
                    comandoRenombrar = Rename()
                    for parametros in element:
                        if (parametros != "rename"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoRenombrar.path(elementos2[1])
                                elif (elementos2[0] == "-name->"):
                                    comandoRenombrar.name(elementos2[1])
                                else:
                                    comandoRenombrar.type(elementos2[1])
                            #! Dependiento del type
                            if (comandoRenombrar.tipo == "bucket"):
                                comandoRenombrar.renombrarBucket()
                            #else:
                            #    comandoRenombrar.renombrarserver()

                if (comando == "modify"):  # !Comando modify
                    #self.local=False
                    comandoModificar = Modify()
                    for parametros in element:
                        if (parametros != "modify"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-path->"):
                                    comandoModificar.path(elementos2[1])
                                elif (elementos2[0] == "-body->"):
                                    comandoModificar.body(elementos2[1])
                                else:
                                    comandoModificar.type(elementos2[1])
                            #! Dependiento del configure
                            if (comandoModificar.tipo == "bucket"):
                                comandoModificar.modificarBucket()
                            #else:
                            #    comandoModificar.renombrarserver()
                if (comando == "backup"):  # !Comando backup
                    #self.local=False
                    comandoBackup= Backup()
                    for parametros in element:
                        if (parametros != "backup"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-type_to->"):
                                    comandoBackup.typeTo(elementos2[1])
                                elif (elementos2[0] == "-type_from->"):
                                    comandoBackup.typeFrom(elementos2[1])
                                elif(elementos2[0] == "-ip->"):
                                    comandoBackup.Ip(elementos2[1])
                                elif(elementos2[0] == "-port->"):
                                    comandoBackup.Port(elementos2[1])
                                else:
                                    comandoBackup.Name(elementos2[1])
                            #! Dependiento del configure
                            if (comandoBackup.tipoA == "bucket")&(comandoBackup.tipoDe == "server")&(comandoBackup.ip==comandoBackup.port): #copia de seguridad bucket to server propios
                                comandoBackup.backupBuckettoServer()
                            #else:
                            #    comandoBackup.backupBuckettoBucket()


                if (comando == "recovery"):  # !Comando add
                    #self.local=False
                    comandoRecovery = Recovery()
                    for parametros in element:
                        if (parametros != "recovery"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-type_to->"):
                                    comandoRecovery.typeTo(elementos2[1])
                                elif (elementos2[0] == "-type_from->"):
                                    comandoRecovery.typeFrom(elementos2[1])
                                elif(elementos2[0] == "-ip->"):
                                    comandoRecovery.Ip(elementos2[1])
                                elif(elementos2[0] == "-port->"):
                                    comandoRecovery.Port(elementos2[1])
                                else:
                                    comandoRecovery.Name(elementos2[1])
                            #recovery
                            if (comandoRecovery.tipoA == "bucket")&(comandoRecovery.tipoDe == "server")&(comandoRecovery.ip==comandoRecovery.port): #recovey de seguridad bucket to server propios
                                comandoRecovery.recoveryBuckettoServer()
                            #else:
                            #    comandoAgregar.agregarCloud()
                if (comando == "delete_all"):  # !Comando exec
                    #self.local=False
                    comandoBorrarTodo = DeleteAll()
                    for parametros in element:
                        if (parametros != "delete_all"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-type->"):
                                    comandoBorrarTodo.type(elementos2[1])
                            if (comandoBorrarTodo.tipo == "bucket"):
                                comandoBorrarTodo.borrarBucket()
                            #else:
                            #    comandoBorrarTodo.borrarServer()
                if (comando == "open"):  # !Comando Open
                    #self.local=False
                    comandoOpen= Open()
                    for parametros in element:
                        if (parametros != "open"):
                            for elementos2 in parametros:
                                if (elementos2[0] == "-type->"):
                                    comandoOpen.type(elementos2[1])
                                elif(elementos2[0] == "-ip->"):
                                    comandoOpen.Ip(elementos2[1])
                                elif(elementos2[0] == "-port->"):
                                    comandoOpen.Port(elementos2[1])
                                else:
                                    comandoOpen.Name(elementos2[1])
                            #! Dependiento del configure
                            if (comandoOpen.tipo == "bucket")&(comandoOpen.ip==comandoOpen.port): #Open bucket  propio
                                comandoOpen.openBucket()
                            #else:
                            #    comandoBackup.backupBuckettoBucket()
                      