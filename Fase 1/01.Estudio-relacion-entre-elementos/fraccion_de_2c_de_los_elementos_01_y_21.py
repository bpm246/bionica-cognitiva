# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:46:57 2021

@author: equipo
"""
"""
Este programa calcula la fraccion de 2c que representan los elementos en las
posiciones (0,1) y (2,1) de cada matriz anidada y representa un histograma
de frecuencias de dichosvalores
"""

import numpy as np
import matplotlib.pyplot as plt

d = 2
e = 31


"""
a       b       x02
x10     c       x12
x20     x21     x22
"""

div01 = []
div21 = []

mat = np.zeros((3,3),int)
for n in range(250,1500):
    a = n - 6*d
    b = n + (6*e + 3*(6*d))
    c = n
    
    mat[0][0] = a
    mat[0][1] = b
    mat[0][2] = -a-b+3*c
    mat[1][0] = -2*a-b+4*c
    mat[1][1] = c
    mat[1][2] = 2*a+b-2*c
    mat[2][0] = a + b -c
    mat[2][1] = -b + 2*c
    mat[2][2] = -a + 2*c
    
    
    div01.append(mat[0][1]/(2*mat[2][2]))
    div21.append(mat[2][1]/(2*mat[2][2]))
    
    
div01 = np.array(div01)
div21 = np.array(div21)

plt.figure()
plt.hist(div01,bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("elemento (0,1) dividido entre 2c")
plt.show()

plt.figure()
plt.hist(div21,bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("elemento (2,1) dividido entre 2c")
plt.show()

plt.figure()
plt.plot(range(250,1500), div01)
plt.plot(range(250,1500), div21)

plt.figure()
plt.plot((div01-div21), range(250,1500))

