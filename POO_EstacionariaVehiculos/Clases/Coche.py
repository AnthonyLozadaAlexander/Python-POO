class Coche():
	# Atributos de la clase Coche
	_largo_chasis: int
	_ancho_chasis: int
	_ruedas: int
	_arrancar: bool
	_placa: str
	_marca : str
	_hora_entrada: str

	# Constructor con parametros
	# self. es el equivalente a this.
	def __init__(self, placa: str, marca : str, largo_chasis : int, ancho_chasis : int, ruedas: int) -> None:
		self._largo_chasis : int  = largo_chasis
		self._ancho_chasis : int = ancho_chasis
		self._ruedas: int = ruedas
		self._placa : str = placa
		self._marca : str = marca
		self._arrancar : bool = False

	@property
	def marca(self) -> str:
		return self._marca

	@property
	def placa(self) -> str:
		return self._placa

	@property
	def largo_chasis(self) -> int:
		return self._largo_chasis

	@property
	def ancho_chasis(self) -> int:
		return self._ancho_chasis

	@property
	def ruedas(self) -> int:
		return self._ruedas

	@property
	def enmarcha(self) -> bool:
		return self._arrancar

	@property
	def hora_entrada(self) -> str:
		return self._hora_entrada

	@hora_entrada.setter
	def hora_entrada(self, hora: str) -> None:
		self._hora_entrada = hora


	# Para crear el setter debo crear antes el getter, ya que el setter es un metodo que permite modificar el valor de un atributo privado, en este caso el atributo privado es _enmarcha
	@enmarcha.setter
	def enmarcha(self, valor: bool) -> None:
		self._arrancar = valor

	# Metodo de informacion para el usuario
	def __str__(self) -> str:
		return self.mostrarInfo()

	# Metodo para mostrar la informacion del coche
	def mostrarInfo(self) -> str:
		return (f"Informacion Del Vehiculo: \n"
		        f"Placa: {self._placa}\n"
		        f"Marca: {self._marca}\n"
		        f"Hora Entrada: {self._hora_entrada}\n"
		        f" Largo Chasis: {self._largo_chasis} \n"
		        f"Ancho Chasis: {self._ancho_chasis} \n"
		        f"Ruedas: {self._ruedas}")

	# Metodo para mostrar para el desarrollador
	def __repr__(self) -> None:
		print(f"Coche({self._placa}, {self._marca}, {self._largo_chasis}, {self._ancho_chasis}, {self._ruedas})")