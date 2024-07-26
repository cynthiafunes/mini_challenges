#Cuenta bancaria: Implementa una clase CuentaBancaria con métodos para depositar y consultar el saldo.

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

cuenta = CuentaBancaria()
cuenta.depositar(250000)
cuenta.consultar_saldo()
cuenta.depositar(250000)
cuenta.consultar_saldo()