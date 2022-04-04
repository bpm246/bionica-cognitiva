# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 13:08:51 2021

@author: equipo
"""
"""
Este programa escribe una matriz anidada para un elemento central n, una
diferencia menor 6m y una diferencia mayor 6M
"""

n = 273
m = 2
M = 31
    
c = n
b = n + (6*M + 3*(6*m))
a = n - 6*m


e11 = a
e12 = b
e13 = -a-b+3*c
e21 = -2*a-b+4*c
e22 = c
e23 = 2*a+b-2*c
e31 = a+b-c
e32 = -b+2*c
e33 = -a+2*c

print(str(e11) + "\t" + str(e12) + "\t" + str(e13))
print(str(e21) + "\t" + str(e22) + "\t" + str(e23))
print(str(e31) + "\t" + str(e32) + "\t" + str(e33))
