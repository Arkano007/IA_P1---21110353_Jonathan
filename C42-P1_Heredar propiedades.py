# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:30:59 2023

@author: PC
"""

class Usuarios:
	def _init_(self, nombre, apellidos): 
		self.nombre = nombre
		self.apellidos = apellidos
	  

	def imprime_datos(self):
		print("El nombre de usuario es: ", self.nombre, "su apellido es", self.apellidos)

usuario1 = Usuarios("isaac", 21)
usuario1.imprime_datos()

# Esta es la subclase
class UsuariosPremium(Usuarios):
	def _init_(self, nombre, apellidos, facebok):
	    Usuarios._init_ (self,nombre, apellidos, facebok)
		
def imprime_datos(self):
    print("el nombre de usuario es: " , self.nombre, "y tiene", self.apellidos, "tambien tiene facebok", self.facebok)
usuario2 = UsuariosPremium("isaac", "franco", "isaaccrack12")
usuario2.imprime_datos()