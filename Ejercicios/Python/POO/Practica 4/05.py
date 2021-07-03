def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError(f'Error: Imposible añadir elementos duplicados => {el}. ')
        else:
            elementos.append(el)
            print(f'{el} se agregó a la lista')
            print(elementos)
    except ValueError:
        print(f'Error: Imposible añadir elementos duplicados => {el} (desde el except)')


#MAIN
elementos = [1, 5, -2]
agregar_una_vez(elementos,5)