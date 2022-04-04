# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 13:50:53 2021

@author: equipo
"""
"""
Este programa calcula y representa los autovalores y autovectores de todas
las matrices con elemento central n y diferencia mayor 6*M

"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

n = 1000
m = 10


eM = np.arange(6,100,6)
autovalores = np.empty((3,len(eM)),complex)
autovectores1 = np.empty((len(eM),3),complex)
autovectores2 = np.empty((len(eM),3),complex)
autovectores3 = np.empty((len(eM),3),complex)

for i in range(len(eM)):
    
    M = eM[i]
    
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
    
    autovectores1[i] = featurevector[0]
    autovectores2[i] = featurevector[1]
    autovectores3[i] = featurevector[2]  
    
    
fi = np.array(len(eM), float)


"""
plt.figure()
plt.title("Primer autovalor frente a diferencia mayor")
plt.plot(eM,autovalores[0,:].real,'.')

plt.figure()
plt.title("Parte real segundo autovalor frente a diferencia mayor")
plt.plot(eM,autovalores[1,:].real,'.')
"""

fi = autovalores[1,:].imag
#plt.figure()
plt.title("Parte imaginaria segundo autovalor frente a diferencia mayor \n para un elemento central de 1000")
plt.plot(eM,fi,'.', label = str(6*m))


"""
plt.figure()
plt.title("Parte real tercer autovalor frente a diferencia mayor")
plt.plot(eM,autovalores[2,:].real,'.')

fi = autovalores[2,:].imag
plt.figure()
plt.title("Parte imaginaria tercer autovalor frente a diferencia mayor")
plt.plot(eM,fi,'.')
"""
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