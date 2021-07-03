Actividad Práctica - Python Unidad 4
1)
Crea la clase Vehiculo, extiende la clase y realiza la siguiente implementación:

Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
Nota: Puedes utilizar el atributo especial de clase name para recuperar el nombre de la
clase de un objeto: type(objeto).__name__
2) Continua con el ejercicio anterior y realiza una función llamada catalogar() que
reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus
atributos.
3) Continua con el ejercicio anterior y modifica la función catalogar() para que reciba
un argumento optativo ruedas, haciendo que muestre únicamente los que su número
de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje
“Se han encontrado {} vehículos con {} ruedas:” únicamente si se envía el
argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar
que el programa se bloquee y además explica en un mensaje al usuario la causa y/o
solución: resultado = 10/0
5) Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un
elemento. La función debe añadir el elemento al final de la lista con la condición de no
repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe
invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su
lugar: Error: Imposible añadir elementos duplicados => [elemento].