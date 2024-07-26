#Figura y Círculo: Crea una clase base Figura con un método imprimir 
# y una clase derivada Círculo que extienda Figura y sobreescriba el método imprimir.

class Figura:
    def imprimir(self):
        print("Soy una figura")

class Circulo(Figura):
    def imprimir(self):
        print("Soy un circulo")

figura = Figura()
circulo = Circulo()

figura.imprimir()
circulo.imprimir()