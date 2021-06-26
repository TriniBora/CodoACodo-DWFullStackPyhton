'''1) Crear la clase Persona con los métodos “set_nombre”, “set_edad”,
“get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo
Persona e imprimirlos por consola.
2) Agregarle a la clase anterior un constructor que reciba nombre y edad.
3) Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva
True o False.
4) Agregarle un método “es_mayor_que” el cual recibe un objeto persona y
compara su edad con la del objeto actual.
5) Agregarle un método estático “get_mayor” que reciba dos objetos Persona y
devuelva el de edad mayor.'''

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Se crean los métodos set y get solo porque los pide el ejercicio
    #No hacen falta, ya que los atributos no son privados

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def print_persona(self):
        return f'Nombre: {self.nombre} - Edad: {self.edad}'

    def es_mayor_de_edad(self):
        if int(self.edad) >= 18:
            return True
        else:
            return False

    def get_mayor(self, persona2):
        if int(self.edad) > persona2.edad:
            print(f'{self.nombre} es mayor que {persona2.nombre}')
        elif int(self.edad) < persona2.edad:
            print(f'{self.nombre} es menor que {persona2.nombre}')
        else:
            print(f'{self.nombre} y {persona2.nombre} tienen la misma edad')


persona1=Persona("Miriam", 54)
print(f'Nombre: {persona1.get_nombre()} Edad: {persona1.get_edad()}')
print(f'¿{persona1.get_nombre()} es mayor de edad? {persona1.es_mayor_de_edad()}')
print()
persona1.set_nombre("Antonella")
persona1.set_edad(12)
print(persona1.print_persona())
print(f'¿{persona1.get_nombre()} es mayor de edad? {persona1.es_mayor_de_edad()}')
print()
persona2=Persona("Ignacio", 8)
persona1.get_mayor(persona2)
persona3=Persona("Pía", 12)
persona1.get_mayor(persona3)
persona4=Persona("Carlos", 32)
persona1.get_mayor(persona4)