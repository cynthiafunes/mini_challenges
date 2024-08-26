#Configuración Básica de Sockets: Implementa un servidor de sockets básico que escuche en un puerto específico 
#y acepte conexiones de un solo cliente. El servidor debería enviar un mensaje de bienvenida al cliente y luego cerrar la conexión.

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55556))
server.listen(1)
print("El servidor esta escuchando..")

cliente, direccion = server.accept()
print(f"Conectado con {direccion}")

mensaje = "Bienvenido"
cliente.send(mensaje.encode('utf-8'))

cliente.close()
print("Conexion cerrada")
