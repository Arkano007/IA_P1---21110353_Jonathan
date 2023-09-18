# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:21:11 2023

@author: PC
"""
#De la lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'.
#Debes utilizar al menos una vez las posiciones negativas para eliminar un color. 
#Después, imprime la lista para ver los colores que se han eliminado.

Colors = ['Red','Blue','Green','Yellow','Brown','Purple','Black','Pink','White','Orange']
#declaramos lista

del Colors[1] #eliminamos el color azul
del Colors[3] #eliminamos el marron
del Colors[4] #eliminamos negro
del Colors[-3] #eliminamos rosa

print(Colors)#imprimimos para comprobar las eliminaciones