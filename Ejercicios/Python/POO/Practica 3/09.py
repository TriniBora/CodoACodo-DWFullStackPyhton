'''9) Realizar una clase que administre una agenda. Se debe almacenar para cada
contacto el nombre, el teléfono y el email. Además deberá mostrar un menú
con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto,
Editar contacto, Cerrar agenda.'''

import os, re

class Contacto:

    def __init__(self, apellido, nombre, telefono, email):
        self.apellido = apellido
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f'Apellido: {self.apellido}\nNombre: {self.nombre}\nTelefono: {self.telefono}\nEmail: {self.email}'


class Agenda:

    def __init__(self):
        self.contactos=[]

    def __str__(self):
        for contacto in self.contactos:
            print(contacto)

    def agregarContacto(self):
        '''Este método pide al usuario que ingrese nombre, telefono y mail del contacto que desea agregar, verificando que los datos ingresados sean válidos. Si los datos son válidos, se crea un objeto del tipo Contacto y se lo agrega a la Agenda.'''
        apellido = input("Ingrese el apellido: ").title()

        nombre = input("Ingrese el nombre: ").title()

        entradaTel = input("Ingrese el número de teléfono:")

        if re.search('^[0-9]{10}$',entradaTel):#si hay conincidencia entre la entrada y la expresión regular, la entrada es válida
            telefono = int(entradaTel)
        else:
            print("Debe ingresar diez caracteres numéricos.")
            self.agregarContacto()

        entradaEmail = input("Ingrese la dirección de email:")
        if re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',entradaEmail):#si hay conincidencia entre la entrada y la expresión regular, la entrada es válida
            email = entradaEmail
        else:
            print("Debe ingresar una dirección de email válida.")
            self.agregarContacto()

        contacto = Contacto(apellido, nombre, telefono, email)
        #print(contacto.__str__())

        self.contactos.append(contacto)

    def listaContactos(self):
        '''Este método verifica si hay contactos guardados en la agenda. Si hay, la recorre y los muestra por pantalla. Si no hay contactos muestra un mensaje.'''

        if len(self.contactos) >0:
            for contacto in self.contactos:
                print('Contacto:')
                print(contacto.__str__())
                print()
        else:
            print("No hay contactos guardados en la agenda.")


    def buscarContacto(self):

        if len(self.contactos) >0:
            apellido =input('Ingrese el apellido del contacto que desea buscar en la agenda: ').title()

            nombre =input('Ingrese el nombre del contacto que desea buscar en la agenda: ').title()

            for contacto in self.contactos:
                if contacto.apellido == apellido and contacto.nombre == nombre:
                    print('Contacto:')
                    print(contacto.__str__())
                    print()
                else:
                    print(f'{apellido}, {nombre} no está almacenado en la agenda.')
        else:
            print("No hay contactos guardados en la agenda.")



    def editarContacto(self):

        telValido = False
        emailValido = False

        if len(self.contactos) >0:
            apellido =input('Ingrese el apellido del contacto que desea editar: ').title()

            nombre =input('Ingrese el nombre del contacto que desea editar: ').title()

            for contacto in self.contactos:
                if contacto.apellido == apellido and contacto.nombre == nombre:
                    while telValido == False:
                        telefono = input("Ingrese el número de teléfono:")
                        if re.search('^[0-9]{10}$',telefono):#si hay conincidencia entre la entrada y la expresión regular, la entrada es válida
                            contacto.telefono = int(telefono)
                            telValido = True
                        else:
                            print("Debe ingresar diez caracteres numéricos.")

                    while emailValido == False:
                        email = input("Ingrese la dirección de email:")
                        if re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',email):#si hay conincidencia entre la entrada y la expresión regular, la entrada es válida
                            contacto.email = email
                            emailValido = True
                        else:
                            print("Debe ingresar una dirección de email válida.")

                    print('Contacto modificado:')
                    print(contacto.__str__())
                    print()

        else:
            print("No hay contactos guardados en la agenda.")


    def menu(self):
        #limpiar la pantalla
        '''
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")'''

        entrada = input("Ingrese una opción: \n1: Agregar contacto \n2: Lista de contactos \n3: Buscar contacto \n4: Editar contacto \n5: Cerrar agenda ")

        try:
            opcionNro = int(entrada)

            if(opcionNro == 1):
                self.agregarContacto()
            elif(opcionNro == 2):
                self.listaContactos()
            elif(opcionNro == 3):
               self.buscarContacto()
            elif(opcionNro == 4):
                self.editarContacto()
            elif(opcionNro == 5):
                exit()
            else:
                print("Debe ingresar un número entero entre 1 y 5")
        except ValueError:
            print("Debe ingresar un número entero.")

        print()
        self.menu()

#MAIN
agenda=Agenda()
agenda.menu()
