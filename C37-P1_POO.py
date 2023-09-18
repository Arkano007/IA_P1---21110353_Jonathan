class naves():
    peso = 2500
    largo = 50
    ancho = 20
    color1 = "azul"
    color2 = "negro"
    motores = 4
    activada = False
    compuerta_principal = False
    sistema_defensa = True
    autodestruccion = False

    def encender(self):
        self.activada = True

