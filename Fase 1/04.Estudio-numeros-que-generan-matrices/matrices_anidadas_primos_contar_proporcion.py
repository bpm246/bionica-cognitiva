# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:27:46 2021

@author: equipo
"""
"""
Este programa genera todas las matrices anidadas de primos 3x3 posibles
y calcula el porcentaje de primos centrales que las generan de entre
todoslos números naturales.
"""
"""
Matriz

a       b      x13
x21     c      x23
x31     x32    x33

"""

import sympy
import numpy as np
import matplotlib.pyplot as plt

Ntop = 1000
primosparacentral = np.array(list(sympy.primerange(0,Ntop)))

matricesdeprimos = 0
mpa = np.zeros(len(primosparacentral),int)

cont = 0

for c in primosparacentral:
    
    primes = list(sympy.primerange(0,c))
    
    primosa = []
    
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
                
        #Escribimos el resultado en pantalla
        if (len(solucionb) > 0):
            solucion = 1
            
    if solucion == 1:
        matricesdeprimos += 1
    
    mpa[cont] = matricesdeprimos
    cont += 1
    

mpaa = np.ones(primosparacentral[0])*0
for i in range(len(primosparacentral)-1):
    unir = np.ones(primosparacentral[i+1]-primosparacentral[i])*mpa[i]
    mpaa = np.append(mpaa,unir)
    

unir = np.ones(Ntop - primosparacentral[len(primosparacentral)-1])*mpa[len(mpa)-1]    
mpaa = np.append(mpaa,unir)

mpaporc = mpaa/np.arange(1,len(mpaa)+1)*100

plt.figure()
plt.plot(mpaporc)

plt.title("Porcentaje de elementos centrales que generan matrices de primos\nfrente a la cantidad total de elementos posibles")
plt.xlabel("Numero central máximo")
plt.ylabel("Porcentaje de elementos centrales\nque generan matrices de primos")


plt.figure()
plt.plot(np.arange(1,Ntop+1)*3, mpaporc)

plt.title("Porcentaje de sumatorios que generan matrices de primos\nfrente a la cantidad total de elementos posibles")
plt.xlabel("Sumatorio máximo")
plt.ylabel("Porcentaje de elementos centrales\nque generan matrices de primos")

plt.figure()
plt.plot(mpaa)


#Proporcion de primos

mpapp = mpa/np.arange(1,len(mpa)+1)*100

plt.figure()
plt.plot(mpapp)

#Primos sobre la recta

primsobrect = np.zeros(Ntop,int)

contprimos = 1
for i in range(3,Ntop):
    if sympy.isprime(i) == False:
        primsobrect[i] = 0
    elif mpa[contprimos]>mpa[contprimos-1]:
        primsobrect[i] = 1
        contprimos += 1
    else: 
        primsobrect[i] = 0
        contprimos += 1
        
plt.figure()
plt.plot(np.arange(1,len(primsobrect)+1), primsobrect)

rectadeprimos = np.zeros(Ntop)
for i in range(Ntop):
    if sympy.isprime(i) == True:
        rectadeprimos[i] = 1
        
        
plt.figure()
plt.plot(np.arange(1,len(rectadeprimos)+1), rectadeprimos)
plt.plot(np.arange(1,len(primsobrect)+1), primsobrect)