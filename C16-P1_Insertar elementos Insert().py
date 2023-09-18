# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:26:40 2023

@author: PC
"""

#31- Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert().
# Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición.
# Deberás hacer esto utilizando posiciones de lista negativa

Colors = ['Red','Blue','Green','Yellow','Brown','Purple','Black','Pink','White','Orange']
#declaramos lista

Colors.insert(-4, 'Magenta') #añadimos el color con el parametro de la posicion
Colors.insert(-1, 'Turquoise') #añadimos usando numeros negativos

print(Colors) #mostramos con los elementos agregados