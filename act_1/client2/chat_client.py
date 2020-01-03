import threading

import grpc

import sys
sys.path.append('../')

import chat_pb2 as chat
import chat_pb2_grpc as rpc

address = 'server'
port = 11912

class Client:

    def __init__(self):
        # Se genera un gRPC channel + stub
        channel = grpc.insecure_channel(address + ':' + str(port))
        self.conn = rpc.ChatServerStub(channel)

        response = self.conn.EnviarNotaInicial(chat.NotaInicial(nombre = 'AAAAAAAA'))

        self.flag = True
        self.ID = response.ID

        print(response.mensaje)
        print("\n")


        threading.Thread(target=self.__listen_for_messages, daemon=True).start()

        while self.flag:
            print("Ingrese comando...")
            comando = input("[1] Enviar mensajes\n[2] Ver lista de mensajes enviados\n")
            if (comando == "1"):
                self.console_mens()
            elif (comando == "2"):
                self.lista_mensaje()
            else:
                print("Funcion Invalida, Intente de nuevo")


    def console_mens(self):
        mens = input("Escriba su mensaje \n")
        recep = input("Esbriba el ID del receptor del mensaje \n")
        self.enviar_mensaje(texto = str(mens), receptor = int(recep))


    def __listen_for_messages(self):

        for note in self.conn.ChatStream(chat.Vacio()):  
            if (note.ID == self.ID):
                print("[{}] {} Te envio el siguiente mensaje: \n {} \n".format(str(note.timestamp), note.emisor_ID ,note.mensaje))  # debugging statement
            

    def enviar_mensaje(self, texto, receptor):

        if texto is not '':
            n = chat.Nota()
            n.ID = receptor
            n.mensaje = texto
            n.emisor_ID = self.ID
            self.conn.EnviarNota(n)  
        else:
            print("No se puede enviar un texto Vacio\n")


    def lista_mensaje(self):
        print("TIMESTAMP \t\t MESSAGE_ID \t\t RECEPTOR_ID \t\t MESSAGE\n")

        m = chat.Nota(emisor_ID = self.ID)

        for note in self.conn.EnviarListaMensajes(m).lista:
            print("{} \t\t {} \t\t {} \t\t {}\n".format(note.timestamp, note.log_ID, note.ID, note.mensaje))


if __name__ == '__main__':

    c = Client()  
