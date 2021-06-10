'''Escribe un programa que pida 3 números y escriba en la pantalla el mayor de
los tres.'''

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))


if num1 > num2:
    if num1 > num3:
        print(f"El primer número es mayor y su valor es {num1}")
    elif num1 < num3:
        print(f"El tercer número es mayor y su valor es {num3}")
    else:
        print(f"El primer número y el tercer número son mayores y su valor es {num1}")
else:
    if num1 < num2:
        if num2 > num3:
            print(f"El segundo número es mayor y su valor es {num2}")
        elif num2 < num3:
            print(f"El tercer número es mayor y su valor es {num3}")
        else:
            print(f"El segundo número y el tercer número son mayores y su valor es {num2}")
    else:
        if num1 > num3:
            print(f"El primer número y el segundo número son mayores y su valor es {num1}")
        elif num1 < num3:
            print(f"El tercer número es mayor y su valor es {num3}")
        else:
            print(f"Los tres números son iguales y su valor es {num1}")
