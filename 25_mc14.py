# Polimorfismo: Crea una clase base Animal con un método hacerSonido 
# y una clase derivada Perro que sobrescriba este método.
class Animal:
    def hacerSonido(self):
        print("Hacer sonido")

class Gato(Animal):
    def hacerSonido(self):
        print("Miau")

animal = Animal()
perro = Gato()

animal.hacerSonido()
perro.hacerSonido()