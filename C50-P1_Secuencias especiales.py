

import re
texto = "¿tienes unos calcetines par o impar?"
buscar = re.findall("par|impar", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")
	#