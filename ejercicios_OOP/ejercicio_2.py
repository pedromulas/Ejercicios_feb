#EJERCICIO 2
class contador():
    def __init__(self, inicio = 1):
        self.inicio = inicio
    def modificador(self, modificador):
        self.inicio += modificador
        return self.inicio
    def get_contador(self):
        return self.inicio
