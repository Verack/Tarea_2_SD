from concurrent import futures

import grpc
import time

from datetime import datetime

import chat_pb2 as chat
import chat_pb2_grpc as rpc

import threading

class PeerSet(object):
    def __init__(self):
        self._peers_lock = threading.RLock()
        self._peers = {}

    def connect(self, peer):
        print("Peer {} connecting".format(peer))
        with self._peers_lock:
            if peer not in self._peers:
                self._peers[peer] = 1
            else:
                self._peers[peer] += 1

    def disconnect(self, peer):
        print("Peer {} disconnecting".format(peer))
        with self._peers_lock:
            if peer not in self._peers:
                raise RuntimeError("Tried to disconnect peer '{}' but it was never connected.".format(peer))
            self._peers[peer] -= 1
            if self._peers[peer] == 0:
                del self._peers[peer]

    def peers(self):
        with self._peers_lock:
            return self._peers.keys()


class ChatServer(rpc.ChatServerServicer):

    def __init__(self):

        self.chats = []
        self._peer_set = PeerSet()
        self.log = open("log.txt","w")
        self.log.write("TIMESTAMP \t\t MESSAGE_ID \t\t EMISOR_ID \t\t RECEPTOR_ID \t\t MESSAGE\n")
        self.user = open("user.txt","w")
        self.user.write("IP_USER \t\t ID_USER\n")

    def _record_peer(self, context):
        def _unregister_peer():
            self._peer_set.disconnect(context.peer())
        context.add_callback(_unregister_peer)
        self._peer_set.connect(context.peer())

    def ChatStream(self, request_iterator, context):

        lastindex = 0
        # For every client a infinite loop starts (in gRPC's own managed thread)
        while True:
            # Check if there are any new messages
            while len(self.chats) > lastindex:
                n = self.chats[lastindex]
                lastindex += 1
                yield n

    def EnviarNota(self, request: chat.Nota, context):

        now = datetime.now()

        registro = request
        registro.timestamp = str(now)
        registro.log_ID = len(self.chats)

        print("timestamp {} \t\t messaje_ID {} \t\t emisor_ID {} \t\t user_ID: {} \t\t mensaje: {}\n".format(registro.timestamp, registro.log_ID ,registro.emisor_ID, registro.ID, registro.mensaje))
        self.log.write("{} \t\t {} \t\t {} \t\t {} \t\t {}".format(registro.timestamp, registro.log_ID ,registro.emisor_ID, registro.ID, registro.mensaje))

        self.log.flush()

        self.chats.append(registro)

        return chat.Vacio()  

    def EnviarNotaInicial(self, request: chat.NotaInicial, context):

        self._record_peer(context)
        print("Se esta registrando el cliente {}".format(context.peer()))
        self.user.write(str(context.peer())+"\t\t"+str(context.peer().split(':')[4])+"\n")

        self.user.flush()

        return chat.Nota(mensaje='Hola '+str(context.peer())+', tu ID sera: '+str(context.peer().split(':')[4]), ID = int(context.peer().split(':')[4]))  


    def EnviarListaMensajes(self, request: chat.Nota, context):

        respuesta = chat.ListaNota()

        for men in self.chats:
            if (men.emisor_ID == request.emisor_ID):
                respuesta.lista.append(men)

        return respuesta


if __name__ == '__main__':
    port = 11912  
   
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  
    rpc.add_ChatServerServicer_to_server(ChatServer(), server)  

    print('Starting server. Listening...')
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    print("Listening on port {}..".format(port))
    try:
        while True:
            time.sleep(10000)
    except KeyboardInterrupt:
        server.stop(0)