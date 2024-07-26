#Clase de Punto 2D: Crea una clase Punto2D con atributos x & y, y un método para imprimir sus coordenadas.

class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas: ({self.x}, {self.y})")

punto = Punto2D(9, 12)
punto.imprimir()