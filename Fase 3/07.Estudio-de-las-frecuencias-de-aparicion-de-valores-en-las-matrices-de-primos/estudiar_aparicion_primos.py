# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 10:36:38 2021

@author: equipo
"""
"""
Este programa genera matrices anidadas de primos para centrales entre 0 y
Ntop y después cuenta qué primos aparecen y con qué frecuencia


Matriz

a       b      x13
x21     c      x23
x31     x32    x33

"""

import sympy
import numpy as np
import matplotlib.pyplot as plt

Ntop = 100
primosparacentral = np.array(list(sympy.primerange(0,Ntop)))
#primosparacentral = np.array([167])
matricesdeprimos = 0

cont = 0

primosaparecidos = np.zeros(0)

for c in primosparacentral:
    
    primes = list(sympy.primerange(0,c))
    
    primosa = []
    
    primosmatrices = np.zeros((1,9))
    
    #Obtenemos todas las posibles descomposiciones de 2c en dos números primos
    for i in range(len(primes)):
        primo1 = primes[i]
        primo2 = 2*c-primo1
        if (sympy.ntheory.isprime(primo2)):
            #print(str(primo1) + " + " + str(primo2))
            primosa.append(primo1)
            primosa.append(primo2)
            
    primosa = sorted(primosa)
    #print("Posibles valores de a:")
    #print(primosa)
    #print("\n")
    
    solucion = 0
    #Calculamos los valores de b para todos los posibles valores de a
    for j in range(len(primosa)):
        
        a = primosa[j]
        
        #Imponemos que todos los elementos de la matriz sean positivos
        primosb = []
        for i in range(len(primosa)):
            b = primosa[i]
            mayor = (-b+4*c)/2
            menor = (2*c-b)/2
            if(mayor > a and menor < a and b !=a and b+a != 2*c):
                primosb.append(b)
                
        #print(primosb)
                
        #print("\n")
        n = 4*c-2*a
        #print("4c - 2a = " + str(n))
        #print("b + j")
        
        #Imponemos que el valor x21 sea primo
        primosbx21 = []
        
        for i in range(len(primosb)):
            primo1 = primosb[i]
            primo2 = n-primo1
            if (sympy.ntheory.isprime(primo2) == True and primo1 != primo2 and primo1 != a and (2*c-primo2) != a):
                #print(str(primo1) + " + " + str(primo2))
                primosbx21.append(primo1)
                
        #print(primosbx21)
                
        
        #print("\n")
        n = a - c
        #print("a - c = " + str(n))
        #print("- b + k")
        
        #Imponemos que el valor x31 sea primo
        primosbx31 = []
        
        for i in range(len(primosbx21)):
            primo1 = primosbx21[i]
            primo2 = n+primo1
            if (sympy.ntheory.isprime(primo2)):
                #print("-" + str(primo1) + " + " + str(primo2))
                primosbx31.append(primo1)
                
        #print(primosbx31)
        #print("\n")
        n = 3*c - a
        #print("3c - a = " + str(n))
        #print("b + l")
        
        #Imponemos que el valor x13 sea primo
        primosbx13 = []
        
        for i in range(len(primosbx31)):
            primo1 = primosbx31[i]
            primo2 = n-primo1
            if (sympy.ntheory.isprime(primo2)):
                #print(str(primo1) + " + " + str(primo2))
                primosbx13.append(primo1)
                
        #print(primosbdel)
        #print("\n")
        n = 2*a - 2*c
        #print("2a - 2c = " + str(n))
        #print("- b + q")
        
        #Imponemos que el valor x23 sea primo
        primosbx23 = []
        
        for i in range(len(primosbx13)):
            primo1 = primosbx13[i]
            primo2 = n+primo1
            if (sympy.ntheory.isprime(primo2)):
                #print("-" + str(primo1) + " + " + str(primo2))
                primosbx23.append(primo1)
                
        #print(primosbx23)
        #print("\n")
        
        solucionb = []   
        
        #Imponemos que no se repita ningún número de la matriz
        for i in range(len(primosbx23)):
            b = primosbx23[i]
            x13 = -a-b+3*c
            x21 = -2*a-b+4*c
            x23 = 2*a+b-2*c
            x31 = a+b-c
            x32 =-b+2*c
            x33 = -a+2*c
            
            if(a != x13 and a != x21 and a != x23 and a != x31 and a != x32 and a != x33 and b != x13 and b != x21 and b != x23 and b != x31 and b != x32 and b != x33 and c != x13 and c != x21 and c != x23 and c != x31 and c != x32 and c != x33):
                solucionb.append(b)
                
                matriz = np.array([[a,b,x13,x21,c,x23,x31,x32,x33]])                
                primosmatrices = np.append(primosmatrices,matriz,0)
          
    
    if (len(primosmatrices) > 1):
        solucion = 1            
        
        primosmatrices = np.delete(primosmatrices, 0, axis=0)        
        primosmatrices.sort()
        if (primosmatrices[0]*np.shape(primosmatrices)[0] != np.sum(primosmatrices,0)).any():
            #print(str(c) + " varias pos")
            unique = np.unique(primosmatrices)
            primosaparecidos = np.append(primosaparecidos, unique)
        else:
            #print(str(c) + " solo una pos")
            primosaparecidos = np.append(primosaparecidos, primosmatrices[0])
    
    cont += 1
    
unique,counts = np.unique(primosaparecidos, return_counts=True)
plt.figure()
plt.plot(unique, counts)
plt.xlabel("Número primo")
plt.ylabel("Número de veces que aparece")


plt.figure()
plt.hist(primosaparecidos, bins=10)
plt.xlabel("Número primo")
plt.ylabel("Número de veces que aparece")


primoshasta10000 = np.array(list(sympy.primerange(0,10000)))

for i in primoshasta10000:
    if len(np.where(primosaparecidos==i)[0]) == 0:
        print(str(i))