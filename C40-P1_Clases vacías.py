
class Usuario:
	def __init__(self, nombre, apodos):
		self.nombre = nombre
		self.apodos = apodos
	

	def imprime_datos(self):
		print("el nombre del usuario es: " + self.nombre, self.apodos)

usuario2 = Usuario("Jona", 21)

print(usuario2.nombre, usuario2.apodos)

del usuario2
#print(usuario2.nombre, usuario2.apodos)

