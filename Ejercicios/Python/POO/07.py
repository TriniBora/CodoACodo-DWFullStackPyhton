'''7) Desarrollar un programa que cargue los datos de un triángulo. Implementar una
clase con los métodos para inicializar los atributos, imprimir el valor del lado
con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o
escaleno).'''


class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def __str__(self):
        return f'Los lados del triángulo miden {self.lado1}, {self.lado2} y {self.lado3} unidades, respectivamente.'

    def validar_triangulo(self):
        '''Este método valida si se cumple la desigualdad triangular, si no se
        lo hace, entonces los valores ingresados para los lados no forman un triángulo.
        Retorna True si se puede construir un triángulo con esos lados y False en caso contrario.'''
        if float(self.lado1) < float(self.lado2)+float(self.lado3) and float(self.lado2) < float(self.lado1)+float(self.lado3) and float(self.lado3) < float(self.lado2)+float(self.lado1):
            return True
        else:
            return False

    def mostrar_lado_mayor_y_tipo_triangulo(self):
        if float(self.lado1) < float(self.lado2)+float(self.lado3) and float(self.lado2) < float(self.lado1)+float(self.lado3) and float(self.lado3) < float(self.lado2)+float(self.lado1):
            if self.lado1 > self.lado2:
                if self.lado1 > self.lado3:
                    return f"El primer lado es mayor y su valor es {self.lado1}. El triángulo es escaleno."
                elif self.lado1 < self.lado3:
                    return f"El tercer lado es mayor y su valor es {self.lado3}. El triángulo es escaleno."
                else:
                    return f"El primer lado y el tercer lado son mayores y su valor es {self.lado1}. El triángulo es isósceles."
            else:
                if self.lado1 < self.lado2:
                    if self.lado2 > self.lado3:
                        return f"El segundo lado es mayor y su valor es {self.lado2}. El triángulo es escaleno."
                    elif self.lado2 < self.lado3:
                        return f"El tercer lado es mayor y su valor es {self.lado3}. El triángulo es escaleno."
                    else:
                        return f"El segundo lado y el tercer lado son mayores y su valor es {self.lado2}. El triángulo es isósceles."
                else:
                    if self.lado1 > self.lado3:
                        return f"El primer lado y el segundo lado son mayores y su valor es {self.lado1}. El triángulo es isósceles."
                    elif self.lado1 < self.lado3:
                        return f"El tercer lado es mayor y su valor es {self.lado3}. El triángulo es isósceles."
                    else:
                        return f"Los tres lados son iguales y su valor es {self.lado1}. El triángulo es equilátero."
        else:
            return f"Los lados ingresados no permiten construir un triángulo."



tri1 = Triangulo(5, 3, 5)
print(tri1)
#print(tri1.validar_triangulo())
print(tri1.mostrar_lado_mayor_y_tipo_triangulo())

tri2 = Triangulo(1.5, 8, 6.5)
print(tri2)
#print(tri2.validar_triangulo())
print(tri2.mostrar_lado_mayor_y_tipo_triangulo())

tri3 = Triangulo(4, 8, 6.5)
print(tri3)
#print(tri3.validar_triangulo())
print(tri3.mostrar_lado_mayor_y_tipo_triangulo())

tri4 = Triangulo(4.3, 4.3, 4.3)
print(tri4)
#print(tri4.validar_triangulo())
print(tri4.mostrar_lado_mayor_y_tipo_triangulo())
