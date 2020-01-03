import pika, os, logging,threading,uuid
from datetime import datetime
logging.basicConfig()

def pdf_process_function(msg):
  print("processing")
  print(" [x] Received " + str(msg))
  print(" processing finished");
  return;


def callback(ch, method, properties, body):
  pdf_process_function(body)

def enviar(idr):
    url = os.environ['AMQP_URL']
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue='e') # Declare a queue
    while (True):
        id=input("Escriba la id: ")
        msg=input("Escriba su mensaje: ")
        now=str(datetime.now())
        msg=idr+";"+id+";"+msg+";"+now
        channel = connection.channel() # start a channel
        channel.queue_declare(queue='e') # Declare a queue
        channel.basic_publish(exchange='', routing_key='e', body="")
        channel.basic_publish(exchange='', routing_key='e', body=msg)
        print ("[x] "+msg+" enviado")



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
print (corr_id)


t1 = threading.Thread(target=enviar, args=(corr_id,))
t2 = threading.Thread(target=recibir, args=(corr_id,))
t1.start()
t2.start()
