#Crear un Diccionario: Escribe un programa que cree un diccionario a partir de dos listas dadas: una de claves y otra de valores

claves = ['nombre', 'apellido', 'correo']  
valores = ["Maria", "Lopez", "marialopez@gmail.com"]       

diccionario = {}

for indice in range(len(claves)):
    diccionario[claves[indice]] = valores[indice]
print(diccionario)