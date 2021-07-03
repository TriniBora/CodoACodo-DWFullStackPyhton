import os

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

    def depositar(self):
        entrada = input("Ingrese la cantidad de dinero que va a depositar: ")
        try:
            cantidad = float(entrada)
            self._cantidad = self._cantidad + cantidad
            print(f'Ha depositado ${cantidad}')
        except ValueError:
            print("La entrada es incorrecta: sólo se aceptan valores numéricos.")
            self.depositar()

    def extraer(self):
        entrada = input("Ingrese la cantidad de dinero que desea extraer: ")
        try:
            cantidad = float(entrada)
            if cantidad <= self.cantidad:
                self._cantidad = self._cantidad - cantidad
                print(f'Ha extraido ${cantidad}')
            else:
                print (f'No dispone de saldo suficiente para realizar la operación')
        except ValueError:
            print("La entrada es incorrecta: sólo se aceptan valores numéricos.")
            self.extraer()

    def mostrar_total(self):
        print(f'Su saldo actual es: ${self._cantidad}')

    def menuCliente(self):
        '''
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")'''

        entrada = input("Ingrese una opción: \n1: Depositar dinero \n2: Extraer dinero \n3: Consultar saldo \n4: Salir ")

        try:
            opcionNro = int(entrada)

            if(opcionNro == 1):
                self.depositar()
            elif(opcionNro == 2):
                self.extraer()
            elif(opcionNro == 3):
                self.mostrar_total()
            elif(opcionNro == 4):
                exit()
            else:
                print("Debe ingresar un número entero entre 1 y 4")
        except ValueError:
            print("Debe ingresar un número entero.")

        print()
        self.menuCliente()

#MAIN
cliente1=Cliente("Juan Gomez", 32677)
cliente2=Cliente("Ana Díaz", 23789)
cliente3=Cliente("Martina Oro", 109000)
print(cliente2)
cliente2.menuCliente()
