# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:23:21 2021

@author: equipo
"""
"""
Este programa descompone 2*c y 3*c entodas las sumas posibles de 2 y 3 números
primos respectivamente.
"""

import sympy
import numpy as np

c = 859

primes = list(sympy.primerange(0,c))

primosa = []

sumas2 = np.zeros((1,2),int)

#Obtenemos todas las posibles descomposiciones de 2c en dos números primos
for i in range(len(primes)):
    primo1 = primes[i]
    primo2 = 2*c-primo1
    if (sympy.ntheory.isprime(primo2)):
        print(str(primo1) + " + " + str(primo2))
        primosa.append(primo1)
        primosa.append(primo2)
        
        
print("")
primosa = sorted(primosa)
primosa = np.array(primosa)

sumas3 = np.zeros((1,3),int)

#Obtenemos todas las posibles descomposiciones de 3c en tres números primos de la lista anterior
for i in range(len(primosa)):
    primo1 = primosa[i]
    
    for j in range(i+1,len(primosa)):
        primo2 = primosa[j]
            
        primo3 = 3*c-(primo2+primo1)
        
        if (sum(primosa == primo3) > 0 and primo3 > primo2 and primo3 > primo1):
            print(str(primo1) + " + " + str(primo2) + " + " + str(primo3))
            
            sumas3 = np.append(sumas3, [[primo1, primo2, primo3]], 0)
            
            
sumas3 = np.delete(sumas3, 0, axis=0)