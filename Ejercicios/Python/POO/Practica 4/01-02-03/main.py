from vehiculo import Vehiculo
from coche import Coche
from camioneta import Camioneta
from bicicleta import Bicicleta
from motocicleta import Motocicleta


def catalogar(lista_vehiculos, *ruedas):
        for vehiculo in lista_vehiculos:
            print(f'{type(vehiculo).__name__}: ')#muestra el nombre de la clase del objeto al que es esta haciendo referencia
            print(vehiculo)


def main():
    coche = Coche('Gris',4,250,2.0)
    camioneta = Camioneta('Blanco',2,200,3.0,2000)
    bicicleta=Bicicleta('Azul',2,'Urbana')
    motocicleta = Motocicleta('Negro',2,'Deportiva',300,200)

    vehiculos=[]
    vehiculos.append(coche)
    vehiculos.append(camioneta)
    vehiculos.append(bicicleta)
    vehiculos.append(motocicleta)


if __name__ == "__main__":
    main()