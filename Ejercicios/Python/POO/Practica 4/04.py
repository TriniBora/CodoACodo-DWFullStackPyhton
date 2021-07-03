def dividir(num1, num2):
    try:
        cociente = num1 / num2
        print(f'El cociente de dividir {num1} por {num2} es {cociente}')
    except ZeroDivisionError:
        print(f'La división por cero no existe, debe ingresar otro valor.')


#MAIN
num1=10
num2=0
dividir(num1,num2)