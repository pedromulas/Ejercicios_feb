class producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def get_nombre(self):
        return self.nombre
    def info_producto(self):
        info = """Nombre producto: {nombre}
Precio: {precio}
""".format(nombre = self.nombre, precio = self.precio)
        return info
    
class medicamento(producto):
    def __init__(self, nombre, precio, compuesto, porcentaje):
        super().__init__(nombre, precio)
        self.compuesto = compuesto
        self.porcentaje = porcentaje
    def info_adicional_med(self):
        info = """Nombre compuesto: {comp}
Porcentaje: {porc}
""".format(comp = self.compuesto, porc = self.porcentaje)
        return info

class laboratorio():
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
    def info_lab(self):
        info = """{nombre}
Prductos disponibles: {prod}
""".format(nombre = self.nombre, prod = self.productos)
        return info 
    
    
p1 = producto('chupete', 5)
p2 = producto('vendas', 0.10)
p3 = medicamento('ibuprofeno', 12, 'aas', 24)
p4 = medicamento('betadine',12, 'yodo', 14)
productos = [p1,p2,p3,p4]
lab = laboratorio('Bayer', productos)
print(p2.info_producto())
print(p3.info_producto(), p3.info_adicional_med())
print(lab.info_lab())

