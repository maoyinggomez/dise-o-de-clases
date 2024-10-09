#Laboratorio 
#Mao Ying Gomez Uribe
#Acitvidad 2 Estado interno de una clase


class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de ${cantidad} realizado. Saldo actual: ${self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
        else:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado. Saldo actual: ${self.saldo}")

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.titular}: ${self.saldo}")

cuenta = CuentaBancaria("Mao", 50500)
cuenta.mostrar_saldo()

cuenta.depositar(20000)
cuenta.retirar(10000)
cuenta.retirar(70000)  

cuenta.mostrar_saldo()
