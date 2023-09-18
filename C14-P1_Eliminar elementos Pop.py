# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:08:01 2023

@author: PC
"""

#Elimina de la siguiente lista los elementos 'azul' y 'blanco' utilizando el método pop(). 
#Además, tendrás que guardar esos dos colores en una nueva lista.

Colors = ['Red','Blue','Green','Yellow','Brown','Purple','Black','Pink','White','Orange']
#declaramos lista

ColorB = Colors.pop(1) #eliminamos de la lista el color azul y lo guardamos en una variable
ColorW = Colors.pop(-2) #eliminamos de la lista el color blanco y lo guardamos en una variable

print(Colors)#imprimimos para comprobar las eliminaciones

Colors_Value = [ColorB, ColorW] #creamos la nueva lista con estos dos valores

print('El color eliminado y guardado es:', Colors_Value)#imprimimos para comprobar las eliminaciones