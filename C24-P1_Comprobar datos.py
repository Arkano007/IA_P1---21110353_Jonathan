# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:22:12 2023

@author: PC
"""

Colors = ('Red','Blue','Green','Yellow') #declaramos lista #creamos tupla

Color = input("Selecciona un color. ") #pedimos el color al usuario

if Color in Colors: #verificamos si el color está en la tupla
    print("El color " + Color + " fue encontrado") #si está, imprimimos con el color introducido por el usuario
else:
    print("Color no fue encontrado") #sino está, imprimimos sin el color introducido