# Polimorfismo: Crea una clase base Animal con un método hacerSonido 
# y una clase derivada Perro que sobrescriba este método.
class Animal:
    def hacerSonido(self):
        print("Hacer sonido")

class Perro(Animal):
    def hacerSonido(self):
        print("Guau")

animal = Animal()
perro = Perro()

animal.hacerSonido()
perro.hacerSonido()