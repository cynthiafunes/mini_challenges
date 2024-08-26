import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 55556))

mensaje = cliente.recv(1024).decode('utf-8')
print(mensaje)

cliente.close()
