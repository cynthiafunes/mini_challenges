# Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable (entre 8 y 16 caracteres)
# que incluya letras mayúsculas, minúsculas, números y símbolos

import random
import string

def generar_contraseña(longitud):
    if longitud < 8 or longitud > 16:
        print("La longitud debe estar entre 8 y 16 caracteres")
        return None                                      
    caracteres = string.ascii_letters + string.digits + string.punctuation      #string.ascii_letters: Incluye todas las letras mayúsculas (A-Z) y minúsculas (a-z).                                                                                                                                                        
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))    #string.digits: Incluye todos los dígitos (0-9).
    return contraseña                                                           #string.punctuation: Incluye todos los caracteres de puntuación y símbolos disponibles

def main():
    try:
        longitud = int(input("Introduce la longitud de la contraseña (entre 8 y 16 caracteres): "))
        contraseña = generar_contraseña(longitud)
        if contraseña:
            print(f"Contraseña: {contraseña}")
    except ValueError:
        print("Error: La longitud debe ser un numero entero")

main()

