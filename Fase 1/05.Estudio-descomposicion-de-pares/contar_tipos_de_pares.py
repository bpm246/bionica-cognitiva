# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 13:50:04 2022

@author: equipo
"""
"""
Este programa coge una lista de matrices anidadas con diferencias
múltiplos de 6 y estudia qué porcentaje hay de cada tipo de par de primos
(primo-primo, compuesto-compuesto, primo-compuesto)
"""

import numpy as np
from sympy.ntheory import isprime
import time
import matplotlib.pyplot as plt

matrices3 = np.loadtxt("10000_matrices.txt",int)


pares = []
for c in range(31,181):
    for p in range(c-6, 0, -6):
        if not [p,2*c-p] in pares and p%2 != 0 and p%3 != 0:
            pares.append([p,2*c-p])

Npares = np.zeros(len(pares),int)

paresprimos = 0
parescompuestos = 0
paresprimocompuesto = 0

for matriz in matrices3:
    if matriz[0]%2 != 0 and matriz[0]%3 != 0:
        for i in range(4):
            if [min(matriz[i],matriz[8-i]),max(matriz[i],matriz[8-i])] in pares:
                np.where(np.array(pares) == [min(matriz[i],matriz[8-i]),max(matriz[i],matriz[8-i])])[0][0]
                pmin = min(matriz[i],matriz[8-i])
                pmax = max(matriz[i],matriz[8-i])
                wheremin = np.where(np.array(pares)[:,0] == pmin)[0]
                           
                ipar = wheremin[np.where(np.array(pares)[wheremin,1] == pmax)[0][0]]
                
                Npares[ipar] += 1
            else:
                print("Falta un par")
                
            if isprime(matriz[i]) and isprime(matriz[8-i]):
                paresprimos += 1
            elif isprime(matriz[i]) or isprime(matriz[8-i]):
                paresprimocompuesto += 1
            else:
                parescompuestos += 1
            
parestotales = paresprimos + parescompuestos + paresprimocompuesto
            
print("Pares primos: " + str(paresprimos/parestotales*100) + "%")
print("Pares compuestos: " + str(parescompuestos/parestotales*100) + "%")
print("Pares primo-compuesto: " + str(paresprimocompuesto/parestotales*100) + "%")

plt.figure()
plt.plot(Npares)
for i in range(len(Npares)):
    if isprime(pares[i][0]) and isprime(pares[i][1]):
        plt.plot(i,Npares[i],'b.')
    elif isprime(pares[i][0]) or isprime(pares[i][1]):
        plt.plot(i,Npares[i],'r.')
    else:
        plt.plot(i,Npares[i],'g.')
