#Cliente Simple de Chat: Desarrolla un cliente que se conecte a un servidor de sockets y permita al usuario
#enviar un mensaje simple a través de la terminal. Una vez enviado, el cliente debería cerrar la conexión.

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55556))
server.listen(1)
print("El servidor esta escuchando..")

cliente, direccion = server.accept()
print(f"Conectado con {direccion}")

mensaje_recibido = cliente.recv(1024).decode('utf-8')
print(f"Mensaje del cliente: {mensaje_recibido}")

cliente.close()
print("Conexion cerrada")