
class CuentaBancaria:
    balance= 0
    tasa_int = 0.01

    def __init__(self, tasa_int, balance): 
        self.tasa_int = tasa_int
        self.balance = balance

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if CuentaBancaria.puede_retirar(self.balance,amount):
            self.balance -= amount - 5
        else:
            print("Fondos insuficientes")
            return self

    def mostrar_info_cuenta(self):
        print("Balance: " + self.balance)
        return self

    def generar_interes(self):
        self.balance = CuentaBancaria.calcularInteres(self.balance)
        return self

    @staticmethod
    def puede_retirar(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    @staticmethod
    def calcularInteres(balance):
        if balance > 0:
            balance += balance*0.01


cuenta1 = CuentaBancaria(0.01,300)
cuenta2 = CuentaBancaria(0.01,500)

cuenta1.deposito(50).deposito(40).deposito(30).retiro(100).generar_interes(0.01).mostrar_info_cuenta()
cuenta2.deposito(100).deposito(30).retiro(100).retiro(20).retiro(20).retiro(20).generar_interes(0.01).mostrar_info_cuenta()