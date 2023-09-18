# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:45:32 2023

@author: PC
"""

#Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.

x = 0

while x <= 15:
	print(x)
	x += 5

#Esta vez, hay que invertir el operador y utilizar el decremento para llegar a -100

x = 0

while x >= -100:
	print(x)
	x -= 20
    
#Solo hay que ir decrementando y en el print concatenar una frase al valor de x.

x = 10

while x >= 0:
	print('El valor de x es: ', x)
	x -= 1