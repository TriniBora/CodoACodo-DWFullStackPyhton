'''9) Realizar una clase que administre una agenda. Se debe almacenar para cada
contacto el nombre, el teléfono y el email. Además deberá mostrar un menú
con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto,
Editar contacto, Cerrar agenda.'''





def mostrar_opciones():
    print("Selecciona la opción:")
    print("1: Añadir contacto")
    print("2: Listar contactos")
    print("3: Buscar contacto")
    print("4: Editar contacto")
    print("5: Cerrar agenda")


def menu():

    while True:
        mostrar_opciones()
        entrada = input()
        try:
            opcionNro = int(entrada)

            if(opcionNro == 1):
                pass
            elif(opcionNro == 2):
                pass
            elif(opcionNro == 3):
                pass
            elif(opcionNro == 4):
                pass
            elif(opcionNro == 5):
                exit()
            else:
                if opcionNro < 1 or opcionNro > 5:
                    print("La opción ingresada no es válida")

        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero")


#MAIN
menu()