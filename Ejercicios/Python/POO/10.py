'''10) En un banco tienen clientes que pueden hacer depósitos y extracciones de
dinero. El banco requiere también al final del día calcular la cantidad de dinero
que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase
banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos
__init__, depositar, extraer, mostrar_total. La clase banco tendrá como
atributos 3 objetos de la clase cliente y los métodos __init__, operar y
deposito_total.'''


class Cliente:

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self._cantidad = cantidad

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self,cantidad):
        self._cantidad = cantidad

    def __str__(self):
        return f'Nombre del cliente: {self.nombre} - Cantidad: {self._cantidad}'

    def depositar(self, cantidad):
        self._cantidad = self._cantidad + cantidad
        print(f'{self.nombre} ha depositado ${cantidad}')

    def extraer(self, cantidad):
        if cantidad <= self.cantidad:
            self._cantidad = self._cantidad - cantidad
            print(f'{self.nombre} Ha extraido ${cantidad}')
        else:
            print (f'No dispone de saldo suficiente para realizar la operación')

    def mostrar_total(self):
        print(f'Su saldo actual es: ${self._cantidad}')

class Banco:

    def __init__(self, cliente1, cliente2, cliente3):
        self.cliente1 = cliente1
        self.cliente2 = cliente2
        self.cliente3 = cliente3

    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(300)
        self.cliente3.depositar(43)
        self.cliente1.extraer(400)

    def deposito_total(self):
        print (f'El total depositado en el día fue de: ${self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad}')


    def menu(self):

        entrada = input("Ingrese una opción: \n1: Operar \n2: Total depositado en el día \n3: Salir ")
        try:
            opcionNro = int(entrada)
            if(opcionNro == 1):
                banco.operar()
            elif(opcionNro == 2):
                banco.deposito_total()
            elif(opcionNro == 3):
                exit()
            else:
                print("Debe ingresar un número entero entre 1 y 3")
        except ValueError:
            print("Debe ingresar un número entero.")
            self.menu()

        print()
        self.menu()

#MAIN
cliente1=Cliente("Juan Gomez", 0)
cliente2=Cliente("Ana Díaz", 0)
cliente3=Cliente("Martina Oro", 0)
banco = Banco(cliente1, cliente2, cliente3)
banco.menu()
