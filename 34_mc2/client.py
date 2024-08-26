##Cliente Simple de Chat: Desarrolla un cliente que se conecte a un servidor de sockets y permita al usuario
#enviar un mensaje simple a través de la terminal. Una vez enviado, el cliente debería cerrar la conexión.

import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 55556))

mensaje = input("Escribe tu mensaje: ")

cliente.send(mensaje.encode('utf-8'))
cliente.close()
