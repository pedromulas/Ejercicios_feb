#EJERCICIO 1
class cuenta():
    def __init__(self, ingreso, reintegro, transferencia):
        self.ingreso = ingreso
        self.reintegro = reintegro
        self.transferencia = transferencia
    def get_ingreso(self):
        return self.ingreso
    def get_reintegro(self):
        return self.reintegro
    def get_trasferencia(self):
        return self.transferencia

