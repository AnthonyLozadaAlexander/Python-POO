from POO_EstacionariaVehiculos.Clases.Coche import Coche # importando la clase Coche

class Estacionamiento():
	_nombre : str
	_capacidad_Max : str
	_tarifaFija : float
	_coches_Dentro : list[Coche]
	_total : float

	def __init__(self, nombre : str, capacidad_Max : int, tarifaFija : int) -> None:
		self._nombre : str = nombre
		self._capacidad_Max : int = capacidad_Max
		self._tarifaFija : float = tarifaFija
		self._coches_Dentro : list[Coche] = [] # se inicializa la lista de coches como vacia
		self._total : float = 0.0

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
		if(len(self._coches_Dentro) == self._capacidad_Max):
			return True
		else:
			return False