# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:35:12 2021

@author: equipo
"""

"""
Este programa calcula y representa los autovalores de todas las matrices
con diferencia menor 6m y diferencia mayor 6M para elementos centrales entre
0 y 1000
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

m = 2
M = 31


ec = np.arange(0,1000)
autovalores = np.empty((3,len(ec)),complex)

for i in range(len(ec)):
    
    n = ec[i]
    
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
    

    mat = np.array([[e11, e12, e13],
                  [e21, e22, e23],
                  [e31, e32, e33]])
    
    eigenvalue, featurevector = np.linalg.eig(mat)
    
    autovalores[0,i] = eigenvalue[0]
    autovalores[1,i] = eigenvalue[1]
    autovalores[2,i] = eigenvalue[2]
    
fi = np.array(len(ec), float)

plt.figure()
plt.title("Primer autovalor frente a ec")
plt.plot(ec,autovalores[0,:].real,'.')

plt.figure()
plt.title("Parte real segundo autovalor frente a ec")
plt.plot(ec,autovalores[1,:].real,'.')

fi = autovalores[1,:].imag
plt.figure()
plt.title("Parte imaginaria segundo autovalor frente a ec")
plt.plot(ec,fi,'.')

plt.figure()
plt.title("Parte real tercer autovalor frente a ec")
plt.plot(ec,autovalores[2,:].real,'.')

fi = autovalores[2,:].imag
plt.figure()
plt.title("Parte imaginaria tercer autovalor frente a ec")
plt.plot(ec,fi,'.')

"""
x = np.array(e22).reshape((-1, 1))
y = autovalores[0,:]

model = LinearRegression()

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
"""