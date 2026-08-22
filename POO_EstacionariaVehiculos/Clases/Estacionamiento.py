from POO_EstacionariaVehiculos.Clases.Coche import Coche  # importando la clase Coche

class Estacionamiento:
    _nombre: str
    _capacidad_Max: int
    _tarifaFija: float
    _coches_Dentro: list[Coche]
    _total: float
    _hora_entrada: int

    def __init__(self, nombre: str, capacidad_Max: int, tarifaFija: int) -> None:
        self._nombre: str = nombre
        self._capacidad_Max: int = capacidad_Max
        self._tarifaFija: float = tarifaFija
        self._coches_Dentro: list[Coche] = (
            []
        )  # se inicializa la lista de coches como vacia
        self._total: float = 0.0

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def capacidad_Max(self) -> int:
        return self._capacidad_Max

    @property
    def tarifaFija(self) -> float:
        return self._tarifaFija

    @property
    def totalRecaudado(self) -> float:
        return self._total

    def esta_lleno(self) -> bool:
        if len(self._coches_Dentro) == self._capacidad_Max:
            return True
        else:
            return False

    def buscar_coche(self, placa: str) -> Coche | None:
        # Bucle foreach que recorre la lista de coches dentro del estacionamiento y busca el coche
        for coche in self._coches_Dentro:
            if coche.placa == placa:
                return coche

        return None

    @property
    def hora_entrada(self) -> int:
        return self._hora_entrada

    @hora_entrada.setter
    def hora_entrada(self, hora: int) -> None:
        self._hora_entrada = hora

    def registrar_entrada(self, coche: Coche, hora_entrada: int) -> bool:

        if self.esta_lleno():
            return False

        if self.buscar_coche(coche.placa):
            return False

        self._coches_Dentro.append(coche)
        self.hora_entrada = hora_entrada

        return True

    def registrar_salida(self, placa: str, hora_salida: int) -> float:
        monto : float
        for coche in self._coches_Dentro:
            if (not (coche.placa == placa)):
                return 0.0
            else:
                monto = (hora_salida - coche.hora_entrada) * self.tarifaFija
                self._coches_dentro.remove(coche)
                _total = _total + monto
