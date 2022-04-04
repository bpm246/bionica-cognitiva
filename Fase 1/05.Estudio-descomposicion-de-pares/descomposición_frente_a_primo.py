# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:23:21 2021

@author: equipo
"""
"""
Este programa calcula, para cada primo en la lista 'primosmatrices' cuántas
descomposiciones posibles en suma de dos primos hay para el doble de cada
primo, y cuantas descomposiciones en suma de 3 primos hay para el triple
de cada primo
"""

import sympy
import numpy as np
import matplotlib.pyplot as plt

Ntop = 1000

primosmatrices = np.array([ 59,  71,  73,  89, 103, 109, 127, 131, 137, 139, 149, 151, 157,
       167, 173, 179, 191, 193, 211, 227, 239, 241, 251, 257, 263, 269,
       271, 281, 283, 293, 307, 311, 337, 347, 349, 353, 359, 367, 373,
       379, 383, 389, 397, 401, 409, 419, 421, 431, 443, 449, 457, 461,
       463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
       563, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
       643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727,
       733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821,
       823, 827, 829, 839, 853, 857, 863, 877, 881, 883, 887, 907, 911,
       919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])

listaprimos = np.array(list(sympy.primerange(0,Ntop)))
numdesc2 = np.zeros(len(listaprimos))
numdesc3 = np.zeros(len(listaprimos))

plt.figure()

for i in range(len(listaprimos)):

    c = listaprimos[i]

    primes = list(sympy.primerange(0,c))
    
    primosdesc2 = []
    
    sumas2 = np.zeros((1,2),int)
    
    #Obtenemos todas las posibles descomposiciones de 2c en dos números primos
    for j in range(len(primes)):
        primo1 = primes[j]
        primo2 = 2*c-primo1
        if (sympy.ntheory.isprime(primo2)):
            numdesc2[i] = numdesc2[i] + 1
            primosdesc2.append(primo1)
            primosdesc2.append(primo2)
        
        
    primosdesc2 = sorted(primosdesc2)
    primosdesc2 = np.array(primosdesc2)
    
    
    if len(np.where(primosmatrices == c)[0]) > 0:
        plt.plot(np.ones(len(primosdesc2))*c, primosdesc2, 'b')
    
    plt.plot(np.ones(len(primosdesc2))*c, primosdesc2, 'b.')
    plt.plot(c,c,'r.')
    
    #Obtenemos todas las posibles descomposiciones de 3c en tres números primos de la lista anterior
    for j in range(len(primosdesc2)):
        primo1 = primosdesc2[j]
        
        for k in range(j+1,len(primosdesc2)):
            primo2 = primosdesc2[k]
                
            primo3 = 3*c-(primo2+primo1)
            
            if (sum(primosdesc2 == primo3) > 0 and primo3 > primo2 and primo3 > primo1):
                numdesc3[i] = numdesc3[i] + 1
                
                
                
    
        
plt.figure()
plt.plot(listaprimos,numdesc2)
plt.xlabel("Numero primo")
plt.ylabel("Numero de descomposiciones posibles")

plt.plot(listaprimos,numdesc2, 'b.')

for i in range(len(primosmatrices)):
    plt.plot(primosmatrices[i], numdesc2[np.where(listaprimos==primosmatrices[i])],'r.')
    

plt.figure()
plt.plot(listaprimos,numdesc3)
plt.xlabel("Numero primo")
plt.ylabel("Numero de descomposiciones posibles en sumas de 3")

plt.plot(listaprimos,numdesc3, 'b.')
for i in range(len(primosmatrices)):
    plt.plot(primosmatrices[i], numdesc3[np.where(listaprimos==primosmatrices[i])],'r.')




