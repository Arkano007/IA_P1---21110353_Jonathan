# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:53:24 2023

@author: PC
"""

#Completa el siguiente fragmento de código:
#def colores(*args):

#colores()

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores("Morado","Violeta") #añadimos los parametros faltantes de la funcion

#################################################################################################
#Crea una función que realice la suma de cinco números utilizando solo *args. 
#Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

def suma(*args): #definimos la funcion con args para no especificar cantidad exacta de parametros
	total = 0 #creamos variable que almacene el total de la suma (igualada a cero para que comience ahi la suma)
	for x in args: #ciclo que se repetira tantas veces como parametros tengamos
		total = total + x #suma el parametro con lo anterior ya acumulado
	print("La suma de los numeros es: ",total) #sale del for e imprime la suma

suma(1,2,3,4,5) #mandamos llamar a funcion y le mandamos los parametros