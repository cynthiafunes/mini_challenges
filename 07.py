# Juego de Piedra, Papel o tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora

import random

def jugar_piedra_papel_tijera():
    opciones = ['piedra', 'papel', 'tijera']
    computadora = random.choice(opciones)
    usuario = input("piedra, papel o tijera: ").lower()
    
    if usuario not in opciones:
        print("Opcion no valida")
        return
    
    print(f"Turno de la computadora: {computadora}")
    
    if usuario == computadora:
        print("Empate")
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        print("Ganaste")
    else:
        print("Perdiste")

jugar_piedra_papel_tijera()
