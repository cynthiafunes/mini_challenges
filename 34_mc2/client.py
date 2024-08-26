import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 55556))

mensaje = input("Escribe tu mensaje: ")

cliente.send(mensaje.encode('utf-8'))
cliente.close()
