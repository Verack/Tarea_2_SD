import pika, os, logging,threading,uuid
from datetime import datetime
logging.basicConfig()

def process_function(msg):
    print("Recibido el mensaje: " + msg+" ")
    return;


def callback(ch, method, properties, body):
    process_function(body)

def enviar(idr):
    url = os.environ['AMQP_URL']
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue='e') # Declare a queue
    while (True):
        print("Escriba la id del destinatario: ")
        id=raw_input("")
        print("Escriba su mensaje: ")
        msg=raw_input("")
        now=str(datetime.now())
        msgf=idr+";"+id+";"+msg+";"+now
        channel = connection.channel() # start a channel
        channel.queue_declare(queue='e') # Declare a queue
        channel.basic_publish(exchange='', routing_key='e', body="")
        channel.basic_publish(exchange='', routing_key='e', body=msgf)
        print ("El mensaje "+msg+" ha sido enviado a "+id+" en "+now)



def recibir(id):

    url = os.environ['AMQP_URL']
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue=id) # Declare a queue
    channel.basic_consume(id,
      callback,
      auto_ack=True)
    channel.start_consuming()


corr_id = str(uuid.uuid4())
print ("ID del usuario: "+corr_id)


t1 = threading.Thread(target=enviar, args=(corr_id,))
t2 = threading.Thread(target=recibir, args=(corr_id,))
t1.start()
t2.start()
