'''8) Realizar un programa en el cual se declaren dos valores enteros por teclado
utilizando el método __init__. Calcular después la suma, resta, multiplicación y
división. Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.'''


class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f'Los valores ingresados son {self.num1} y {self.num2}'

    def suma(self):
        return f'La suma entre {self.num1} y {self.num2} es {self.num1 + self.num2}'

    def resta(self):
        return f'La resta entre {self.num1} y {self.num2} es {self.num1 - self.num2}'

    def multiplicacion(self):
        return f'El producto entre {self.num1} y {self.num2} es {self.num1 * self.num2}'

    def division(self):
        try:
            return f'El cociente entre {self.num1} y {self.num2} es {(self.num1 / self.num2):.2f}'
        except ZeroDivisionError:
            return f'La división por cero no es una operación válida.'

#MAIN
while True:
    valor1 = input("Ingrese el primer número: ")
    valor2 = input("Ingrese el segundo número: ")
    try:
        num1 = int(valor1)
        num2 = int(valor2)
        calcu=Calculadora(num1,num2)

        break
    except ValueError:
        print("La entrada es incorrecta: escribe un numero entero")

print(calcu)
print(calcu.suma())
print(calcu.resta())
print(calcu.multiplicacion())
print(calcu.division())