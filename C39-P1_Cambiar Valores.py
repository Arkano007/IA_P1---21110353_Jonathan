class Usuario:
	def __init__(self, nombre, apodos):
		self.nombre = nombre
		self.apodos = apodos
	

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApodos:', self.apodos)

usuario001 = Usuario('JhonyL', 'Cash')

usuario002 = Usuario('Alex', 'Marin')

usuario002.nombre = 'Kerberos'

usuario002.imprime_datos()