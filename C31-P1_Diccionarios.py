# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:03:08 2023

@author: PC
"""

#Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con presentación en un print().
# El resultado será esto en la consola: El modelo Corsair K55 RGB cuesta 59,99 $.

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'Tt Sports', #declaracion de teclado 1
	'Precio': '99,50'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',     #declaracion teclado 2
	'Precio': '100'
}

consulta1 = teclado2["Modelo"] #almacenamos la prier consulta
consulta2 = teclado2["Precio"] ##amacenamos la segunda
print("El modelo " + consulta1 + " cuesta " + consulta2 + " $ .") #imprimimos la info