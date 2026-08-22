import datetime as dt
from POO_EstacionariaVehiculos.Clases.Coche import Coche


def main():
    _fecha = dt.datetime.now()
    _hora: int = _fecha.hour

    miCoche = Coche("ABC123", "Toyota", 400, 200, 4)
    print(miCoche)

    miCoche.__repr__()


if __name__ == "__main__":
    main()
