# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:50:45 2022

@author: equipo
"""

"""
Este programa toma matrices anidadas de 3x3 y cuenta cuantas son de primos,
cuales mixtas y cuales de compuestos. En el último caso, cuenta cuántas son
simplificables (divisibles por un mismo número)
"""

from sympy import sieve, isprime
import numpy as np

def factorizar(a):
    
    factores = []
    n = a    
    if a>1:
        while not isprime(n):
            for primo in sieve.primerange(int(n**0.5)+1):
                if n%primo == 0:
                    factores.append(primo)
                    n = n//primo
                    break
    
    factores.append(n)
    return factores



matrices = np.loadtxt("matrices_3_no_multiplos_2_o_3.txt",int)
nmatricessimp = 0

compuestas_no_simplificables = 0

nmmixtas = np.zeros(9,int)
nmprimos = 0

nm_simplificable_a_compuestas = 0
nm_simplificable_a_primos = 0
nm_simplificable_a_mixtas = np.zeros(9,int)


multiplos2o3 = 0
counter = 0
lenmatrices = str(len(matrices))

prop08_primos = []
prop08_compuestas = []

for matriz in matrices:
    counter += 1
    if counter%10000 == 0:
        print(str(counter) + "/" + lenmatrices)
    
    factoresrepetidos = factorizar(matriz[0])
    simplificable = 1
    
    for m in matriz[1:]:
        factores = factorizar(m)
        
        fraux = factoresrepetidos.copy()
        factaux = factores.copy()
        for factorrepetido in fraux:
            if not factorrepetido in factaux:
                factoresrepetidos.remove(factorrepetido)
            else:
                factaux.remove(factorrepetido)
                
        if len(factoresrepetidos) == 0:
            simplificable = 0
            break
        
    if simplificable == 1:
        matrizsimplificada = matriz.copy()
        nmatricessimp += 1
        for fr in factoresrepetidos:
            matrizsimplificada = matrizsimplificada//fr
        if 2 in factoresrepetidos or 3 in factoresrepetidos:
            multiplos2o3 += 1
        #else:
            #print(matriz)
            #print(factoresrepetidos)
            #print(matrizsimplificada)
            
        primos = 0
        
        for m in matrizsimplificada:
            if isprime(m):
                primos += 1
        
        if primos == 0:
            nm_simplificable_a_compuestas += 1
            prop08_compuestas.append(matriz[8]/matriz[0])
            if abs(matriz[8]/matriz[0] - 3.4) < 0.001:
                print(matriz)
                print(factoresrepetidos)
        elif primos == 9:
            nm_simplificable_a_primos += 1
            prop08_primos.append(matriz[8]/matriz[0])
        else:
            nm_simplificable_a_mixtas[primos] += 1
        
    
            
    else:
        primos = 0
        
        for m in matriz:
            if isprime(m):
                primos += 1
                
        if primos == 0:
            compuestas_no_simplificables += 1
            prop08_compuestas.append(matriz[8]/matriz[0])
            if abs(matriz[8]/matriz[0] - 3.4) < 0.001:
                print(matriz)
                print(factoresrepetidos)
        elif primos == 9:
            nmprimos += 1
            prop08_primos.append(matriz[8]/matriz[0])
        else:
            nmmixtas[primos] += 1
            
            