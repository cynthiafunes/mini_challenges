#Configuración Básica de Sockets: Implementa un servidor de sockets básico que escuche en un puerto específico 
#y acepte conexiones de un solo cliente. El servidor debería enviar un mensaje de bienvenida al cliente y luego cerrar la conexión.

import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 55556))

mensaje = cliente.recv(1024).decode('utf-8')
print(mensaje)

cliente.close()
