# Inversión de una Cadena: Escribe un programa que invierta una cadena de caracteres dada por el usuario.

def invertir_caracteres(cadena_de_caracteres):
    if len(cadena_de_caracteres) == 0:
        return ""
    else:
        return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1])

cadena_ingresada = input("Ingresa una cadena de caracteres: ")
resultado = invertir_caracteres(cadena_ingresada)
print("Cadena invertida:", resultado)