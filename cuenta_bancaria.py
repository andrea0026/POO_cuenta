
class CuentaBancaria:
    balance= 0
    tasa_int = 0.01

    def __init__(self, tasa_int, balance): 
        self.tasa_int = 0.5
        self.balance = balance

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if CuentaBancaria.puede_retirar(self.balance,amount):
            self.balance -= amount + 5
        else:
            print("Fondos insuficientes")
        return self

    def mostrar_info_cuenta(self):
        print("Balance:", self.balance)
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance*self.tasa_int
        return self

    @staticmethod
    def puede_retirar(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

cuenta1 = CuentaBancaria(1.003,300)
cuenta2 = CuentaBancaria(1.003,500)

cuenta1.deposito(50).deposito(40).deposito(30).retiro(100).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(100).deposito(30).retiro(100).retiro(20).retiro(10).retiro(15).generar_interes().mostrar_info_cuenta()