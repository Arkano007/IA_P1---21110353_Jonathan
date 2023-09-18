# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:01:05 2023

@author: PC
"""

string_1 = "Hi" #declaramos string 1 y 2
string_2 = 'Kick'
string_3 = string_1 + string_2 #concatenamos los dos strings con el operando '+' almacenando en una tercer variable
print(string_3)

string_1 = string_1 + string_2 #concatenamos los strings reciclando una variable
print(string_1)

print("Hi" + string_2 + " :)") #concatenamos strings con otra variable dentro de un print