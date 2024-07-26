#Formas geométricas: Define una clase base FormaGeometrica con métodos calcular_area y calcular_perimetro. 
#  clases derivadas Rectangulo y Circulo que sobrescriban estos métodos.

class FormaGeometrica:
    def calcular_area(self):
        pass #para crear metodos vacios

    def calcular_perimetro(self):
        pass

class Rectangulo(FormaGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio * self.radio

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

rectangulo = Rectangulo(5, 3)
circulo = Circulo(4)

print("Area del rectangulo:", rectangulo.calcular_area())
print("Perimetro del rectangulo:", rectangulo.calcular_perimetro())
print("Area del circulo:", circulo.calcular_area())
print("Perimetro del circulo:", circulo.calcular_perimetro())