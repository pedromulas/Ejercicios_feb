#EJERCICIO 3
class libro():
    def __init__(self, prestamo, devolucion):
        self.prestamo= prestamo
        self.devolucion = devolucion
    def dame_info(self):
        info = 'El prestamo del libro es {prestamo} \n La devolucion es {devolucion}'.format(prestamo = self.prestamo, devolucion = self.devolucion)
        return info
