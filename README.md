# Tarea 2 SD

##  Integrantes:
-	Leonardo Astudillo - Rol: 201573598-0
-	Claudio Valenzuela - Rol: 201573530-1

#### Consideraciones:

General:
  - Cada actividad esta separada por las carpetas act_1 y act_2
  - Dentro de esa carpetas se encuentra el archivo docker-compose.yml
  - En cada carpeta se tiene que ejecutar el comando "> docker-compose build" y "> docker-compose up"
  - Una vez que se haya ejecutado el comando "docker-compose up", para interactuar con el chat, se debe primero, utilizar el comando "> sudo docker ps -a"
  - Luego de hacer esto, para tomar control de un cliente en el terminal (que no sea el mismo que cuando se ejecuto "docker-compose up"), se debe poner el comando "sudo docker attach [ID container]"

Actividad 1:

  - Los dos archivos (log.txt y user.txt) se generan en la misma ruta donde se ubica el docker-compose
  
Actividad 2:
  
  - Los publisher corresponden a los clientes, mientras que el consumer cumple el rol de servidor
  - Se recomienda ejecutar primero el servidor de rabbitmq para evitar errores de conexion esto utilizando el comando "docker-compose up -d rabbitmq"
  - Al inicio de la ejecucion de los clientes aparecera su id correspondiente, para enviar un mensaje primero se debe colocar la id del remitente y luego el mensaje a enviar.
  - En el servidor se podra seleccionar la opcion de ver los mensajes de un cliente, luego de seleccionarla se debera ingresar la id del cliente correspondiente para ver sus mensajes
  - Para que un servidor sepa la existencia de un cliente, este debe haber mandado primero un mensaje. Esto es importante de considerar en la opcion de ver los clientes conectados al servidor.
  
