import math
class figura():
    def __init__(self):
        pass
    def area(self):
        return None
    def perimetro(self):
        return None

class circulo(figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        area = self.radio**2 * math.pi
        return area
    def perimetro(self):
        perimetro = 2*math.pi * self.radio
        return perimetro

class rectangulo(figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        area = self.base * self.altura
        return area
    def perimetro(self):
        perimetro = 2*self.base + 2*self.altura
        return perimetro

class triangulo_rect(figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        area = (self.base * self.altura)/2
        return area
    def perimetro(self):
        lado = (self.base**2 + self.altura**2)**(1/2)
        perimetro = self.base + self.altura + lado
        return perimetro


c = circulo(4)
print(c.area(), c.perimetro())
