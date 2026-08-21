class Coche():
	# Atributos de la clase Coche
	_largoChasis: int = 0
	_anchoChasis: int = 0
	_ruedas: int = 0
	_arrancar: bool = False

	# Constructor con parametros
	def __init__(self, largoChasis, anchoChasis, ruedas):
		self._largoChasis  = largoChasis
		self._anchoChasis = anchoChasis
		self._ruedas = ruedas

	def Coche(self):
		pass

	@property
	def largoChasis(self) -> int:
		return self._largoChasis

	@property
	def anchoChasis(self) -> int:
		return self._anchoChasis

	@property
	def ruedas(self) -> int:
		return self._ruedas

	@property
	def enmarcha(self) -> bool:
		return self._arrancar

	# Para crear el setter debo crear antes el getter, ya que el setter es un metodo que permite modificar el valor de un atributo privado, en este caso el atributo privado es _enmarcha
	@enmarcha.setter
	def enmarcha(self, valor: bool):
		self._arrancar = valor

	# Metodo para mostrar la informacion del coche
	def mostrarInfo(self) -> str:
		return (f"Informacion Del Vehiculo: \n"
		        f" Largo Chasis: {self._largoChasis} \n"
		        f"Ancho Chasis: {self._anchoChasis} \n"
		        f"Ruedas: {self._ruedas}")
