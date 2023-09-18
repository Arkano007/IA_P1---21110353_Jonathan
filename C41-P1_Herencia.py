

class Usuario:
	def __init__(self, nombre, apodos):
		self.nombre = nombre
		self.apodos = apodos
	

	def muestra_datos(self):
		print("el nombre del usuario es: " + self.nombre, "y Carolina", self.apodos)

usuario1 = Usuario("Jhony", "Kerberos")

usuario1.muestra_datos()

class Usuario_Premium(Usuario):
 pass
usuario2 = Usuario("Jona", "Kerpanq")

usuario2.muestra_datos()
	

