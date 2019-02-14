#EJERCICIO 15
class cuenta():
    def __init__(self, num, saldo):
        self.num = num
        self.saldo = saldo
    def abonos(self, abono):
        self.saldo += abono
        return self.saldo
    def recibos(self, recibo):
        self.saldo -= recibo
        return self.saldo
    
class persona(cuenta):
    def __init__(self, dni, list_cuentas, saldo = 0):
        self.dni = dni
        self.list_cuentas = list_cuentas
        self.saldo = saldo
        for cuenta in self.list_cuentas:
            self.saldo += cuenta.saldo
    def add_cuenta(self, c1):
        self.list_cuentas.append(cuenta)
        if len(list_cuentas) > 3:
            print('Max numero de cuentas sobrepasado')
            list_cuentas.remove(list_cuentas[-1])
            return list_cuentas
        else:
            print('Cuenta añadida exitosamente')
            return list_cuentas
    def morosidad(self):
        if self.saldo < 0:
            return 'Cuenta en numeros rojos'
        else:
            return 'Cuenta correcta'
            
        
c1 = cuenta(2323, 1000)
c2 = cuenta(5544,7755)
list_cuentas = [c1, c2]
p1 = persona(654, list_cuentas)
p1.add_cuenta(432)
print(p1.saldo, p1.morosidad())

