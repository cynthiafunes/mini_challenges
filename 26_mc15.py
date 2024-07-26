# Auto y Motor: Implementa una clase Auto que contenga una instancia de una clase Motor 
# con un método para describir el motor.
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def describir(self):
        print(f"Motor: {self.tipo}")

class Auto:
    def __init__(self, motor):
        self.motor = motor

    def describir_motor(self):
        self.motor.describir()

motor = Motor("De combustion interna")
auto = Auto(motor)
auto.describir_motor()