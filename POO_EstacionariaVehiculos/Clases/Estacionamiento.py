from POO_EstacionariaVehiculos.Clases import Coche

class Estacionamiento():
	_nombre : str
	_capacidad_Max : str
	_tarifaFija : int
	_coches_Dentro : list
	_total : int

	def __init__(self, nombre : str, capacidad_Max : int, tarifaFija : int) -> None:
		self._nombre : str = nombre
		self._capacidad_Max : int = capacidad_Max
		self._tarifaFija : int = tarifaFija
		self._coches_Dentro : list = []
		self._total : int = 0