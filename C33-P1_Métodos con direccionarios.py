# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:44:15 2023

@author: PC
"""

#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. 
#Muestra la última clave ('Modelo') que queda en la consola.

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1 #eliminamos todo el diccionario 1
del teclado2['Categoría'] #eliminamos con metodo 'del'
del teclado2['Precio'] #eliminamos con metodo 'del'
print(teclado2['Modelo'])