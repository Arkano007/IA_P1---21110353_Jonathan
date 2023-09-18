# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:35:43 2023

@author: PC
"""

import re

texto = "Trina triste traga trigo, trigo traga triste Trina."
busqueda = re.findall("t", texto)
print(busqueda)

import re

texto = "Trina triste traga trigo, trigo traga triste Trina."
busqueda = re.findall("ta", texto)
print(busqueda)