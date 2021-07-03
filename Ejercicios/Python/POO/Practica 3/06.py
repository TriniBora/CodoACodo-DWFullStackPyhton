'''6) Realizar un programa que conste de una clase llamada Alumno que tenga
como atributos el nombre y la nota del alumno. Definir los métodos para
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la
nota y si ha aprobado o no.'''

class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f'Nombre del alumno: {self.nombre} - Nota del alumno: {self.nota}'

    def aprobado(self):
        if int(self.nota) >= 7:
            print(f'La nota es {self.nota}, {self.nombre} ha aprobado.')
        else:
            print(f'La nota es {self.nota}, {self.nombre} ha desaprobado.')

alu1=Alumno("Juan Martinez", 6)
print(alu1)
alu1.aprobado()
alu2=Alumno("Melina Gonzalez", 10)
alu2.aprobado()
alu1.nota=7
alu1.aprobado()
