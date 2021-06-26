'''Escribe un programa que pida dos números y escriba en la pantalla cual es el
mayor.'''


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

#print(f"El numero {num1} es el mayor") if num1 > num2 else print(f"El numero {num2} es el mayor")

if num1 > num2:
    (f"El numero {num1} es el mayor")
elif num1 == num2:
    ("Los dos números son iguales")
else:
    (f"El numero {num2} es el mayor")