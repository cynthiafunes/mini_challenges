# Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit

def celsius_fahrenheit():
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = (1.8 * celsius) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")

celsius_fahrenheit()
