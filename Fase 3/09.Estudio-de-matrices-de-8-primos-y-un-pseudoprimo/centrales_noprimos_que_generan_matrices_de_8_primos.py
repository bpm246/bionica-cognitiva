# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:24:33 2022

@author: equipo
"""
"""
Este programa calcula el porcentaje de números no primos entre 0 y 10000 que
generan matrices anidadas de 3x3 en las que los 8 números restantes sí
son primos
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy.ntheory import isprime
import itertools
import time


#Vemos qué no primos generan matrices de 8 primos como centrales
noprimos = []

for i in range(0,10000):
    if not isprime(i):
        noprimos.append(i)

d = 6

noprimos_centrales = []

counter = 0        
for c in noprimos:
    counter += 1    
    if counter%500 == 0:
        print(str(counter) + "/" + str(len(noprimos)))
    
    #Vemos que numeros (diferencia multiplo de 6 y primos) pueden aparecer en la matriz
    multmax = int(c/d)
    multiplicador = np.arange(1,multmax+1)
    mul6 = c - multiplicador*d
    
    pares = []
    for i in mul6:
        if isprime(i) and isprime(2*c-i):
            pares.append(i)
            pares.append(2*c-i)
    
    
    #Construimos las matrices posibles y guardamoslas que tengan el par más lejano y el más cercano al centro (o el seguno más cercano o lejano en su defecto)
    matrices_validas =[]
    
    matriz_encontrada = 0
    if len(pares)>= 8:        
        for a in pares:
            for b in pares:
                if a != b:
                    x13 = -a-b+3*c
                    x21 = -2*a-b+4*c
                    x23 = 2*a+b-2*c
                    x31 = a+b-c
                    x32 =-b+2*c
                    x33 = -a+2*c
                    
                    
                    matriz = [a,b,x13,x21,c,x23,x31,x32,x33]
                    cont=0
                    
                    #Comprobamos que todos los elementos pertenezcan a la lista de posibles pares y que no se repitan elementos
                    if (x13 in pares) and (x21 in pares) and len(set(matriz)) == 9:                    
                        noprimos_centrales.append(c)
                        matriz_encontrada = 1
                        break
                    
            if matriz_encontrada == 1:
                break
            
print(len(noprimos_centrales)/len(noprimos)*100, end = "%\n")