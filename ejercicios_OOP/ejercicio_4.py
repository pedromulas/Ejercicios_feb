#EJERCICIO 4
import math
class fraccion():
    def __init__(self, num1, den1, num2, den2):
        self.num1 = num1
        self.den1 = den1
        self.num2 = num2
        self.den2 = den2
    def get_valores(self):
        frac1 = self.num1/self.den1
        frac2 = self.num2/self.den2
        msg = 'Valor fraccion 1 = {frac1} \nValor fraccion 2 = {frac2}'.format(frac1 = frac1, frac2 = frac2)
        return msg
    def suma(self):
        gcd = math.gcd(self.den1, self.den2)
        lcm = (self.den1 * self.den2) // gcd
        num1 = self.num1 * (lcm // self.den1)
        num2 = self.num2 * (lcm// self.den2)
        suma = num1 + num2
        valor = suma / lcm
        suma, gcd = str(suma), str(lcm)
        msg = 'Suma = {frac} = {valor}'.format(frac = suma+'/'+gcd, valor = valor)
        return msg
    def resta(self):
        gcd = math.gcd(self.den1, self.den2)
        lcm = (self.den1 * self.den2) // gcd
        num1 = self.num1 * (lcm // self.den1)
        num2 = self.num2 * (lcm // self.den2)
        resta = num1 - num2
        valor = resta/ lcm
        resta, gcd = str(resta), str(lcm)
        msg = 'Resta = {frac} = {valor}'.format(frac = resta+'/'+gcd, valor = valor)
        return msg
    def multiplicacion(self):
        num = self.num1 * self.num2
        den = self.den1 * self.den2
        valor = num/den
        num, den = str(num), str(den)
        msg = 'Multiplicacion = {frac} = {valor}'.format(frac = num+'/'+den, valor = valor)
        return msg
    def division(self):
        num = self.num1 * self.den2
        den = self.den1 * self.num2
        valor = num/den
        num, den = str(num), str(den)
        msg = 'Division = {frac} = {valor}'.format(frac = num+'/'+den, valor = valor)
        return msg
