import pika, os, time,threading,uuid


def callback(ch, method, props, body):
    if(body ==""):
        return
    print(" Recibido paquete: " + str(body))
    msg_id = str(uuid.uuid4())
    print (msg_id)
    f= open("log.txt","a")
    g= open("usuarios.txt","r")
    lis=body.split(";")
    flag=False
    for line in g:
      if line.strip() == lis[0]:
          print line.strip()
          flag=True
          break
    g.close()
    if (flag==False):
        g= open("usuarios.txt","a")
        g.write(lis[0]+"\n")
        g.close()
    f.write(body+";"+msg_id+"\n")
    f.close()


    channel.queue_declare(queue=lis[1])
    ch.basic_publish(exchange='', routing_key=lis[1], body=lis[2])
    print("Mensaje enviado");
    return;


def consola():
    while(True):
        print("Elija una opcion:")
        print("1) Ver mensajes de usuario: ")
        print("2) Ver usuarios")
        opc=raw_input("")
        if opc =="1":
            print("Escriba la id del usuario: ")
            idu=raw_input("")
            f= open("log.txt","r")
            for i in f:
                if i.split(";")[0] == idu:
                    print("Mensaje: "+i.split(";")[2]+" al destinatario: "+i.split(";")[1])
            f.close()
        if opc =="2":
            f= open("usuarios.txt","r")
            for i in f:
                print(i)
            f.close()

t1 = threading.Thread(target=consola, args=())
t1.start()

f= open("log.txt","w")
f.write("ID_Remitente;ID_Destinatario;Mensaje;TimeStamp;ID_Mensaje"+"\n")
g= open("usuarios.txt","w")
f.close()
g.close()



url = os.environ['AMQP_URL']
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='e') # Declare a queue
print(" conectado")


# set up subscription on the queue
channel.basic_consume('e',
  callback,
  auto_ack=True)

# start consuming (blocks)
channel.start_consuming()
