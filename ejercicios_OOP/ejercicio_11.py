#EJERCICIO 11
class alumno():
    def __init__(self, matricula, nombre, nota1, nota2, nota3, nota_media = None):
        self.matricula = matricula
        self.nombre = nombre 
        self.nota1 = nota1
        self.nota2 = nota2 
        self.nota3 = nota3
        self.nota_media = (nota1 + nota2 + nota3)/3
    def get_nota_media(self):
        return nota_media
    def datos_alumno(self):
        msg = """Matricula nº: {matricula}
Nombre: {nombre}
Nota media: {nota}
        """.format(matricula = self.matricula, nombre = self.nombre, nota = self.nota_media)
        return msg
    def aprobado(self):
        if self.nota_media >= 4.8:
            return 'APROBADO'
        else:
            return 'SUSPENSO'

p1 = alumno(520, 'Jesus', 4.8,4.8,4.8)
print(p1.datos_alumno(),p1.aprobado())
