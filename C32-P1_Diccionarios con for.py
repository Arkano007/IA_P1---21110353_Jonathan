# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:35:08 2023

@author: PC
"""

#Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:
#Categoría = Teclados.
#Modelo = HyperX Alloy FPS Pro.
#Precio = 89,99.

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

for x, y in teclado1.items():#La funcion 'items()' obtiene los elementos del diccionario y ademas sus atributos
	print(x, ": ", y , ".") #mostramos en consola añadiendo presentacion con los puntos y espacios
