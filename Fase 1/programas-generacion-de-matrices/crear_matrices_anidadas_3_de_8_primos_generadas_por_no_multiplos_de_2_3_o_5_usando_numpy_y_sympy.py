# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:24:33 2022

@author: equipo
"""
"""
Este programa genera matrices anidadas de 3x3 cuyo central no es múltiplo de 
2,3 o 5 y el resto de elementos son primos.
"""

import numpy as np
from sympy.ntheory import isprime
import time

start = time.time()

centrales = []

nin = 0
nfin = 1000

f = open("matrices_centrales_primos_y_no_primos_de_"+str(nin)+"_a_"+str(nfin)+".txt", "a")


for i in range(nin,nfin):
    if i%2 != 0 and i%5 != 0 and i%3 != 0:
        centrales.append(i)
        
d = 6

#una_matriz_por_central = []
#centrales_no_generadores = []

counter = 0        
for c in centrales:
    counter += 1    
    if counter%10== 0:
        print(str(counter) + "/" + str(len(centrales)))
    
    #Vemos que numeros (diferencia multiplo de 6 y primos) pueden aparecer en la matriz
    multmax = int(c/d)
    multiplicador = np.arange(1,multmax+1)
    mul6 = c - multiplicador*d
    
    pares = []
    for i in mul6:
        if isprime(i) and isprime(2*c-i):
            pares.append(i)
            pares.append(2*c-i)
    
    #print(pares)
    #Construimos las matrices posibles y guardamoslas que tengan el par más lejano y el más cercano al centro (o el seguno más cercano o lejano en su defecto)
    
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
                    if (x13 in pares) and (x21 in pares) and len(set(matriz)) == 9:# and nnp == 1:   
                        #una_matriz_por_central.append(matriz)
                        matriz_encontrada = 1
                        for i in range(8):
                            f.write(str(matriz[i]) + " ")
                        f.write(str(matriz[8]) + "\n")
                        break
                    
            if matriz_encontrada == 1:
                break
            
    #if matriz_encontrada == 0:
        #centrales_no_generadores.append(c)
        
    if (counter%10==0 and counter>0):
        f.close()
        f = open("matrices_centrales_primos_y_no_primos_de_"+str(nin)+"_a_"+str(nfin)+".txt", "a")
        #np.savetxt("matrices_centrales_primos_y_no_primos_de_"+str(counter)+"_a_"+str(counter-50000)+".txt",una_matriz_por_central[counter-50000:counter,:],fmt="%i")
        
#np.savetxt("matrices_centrales_primos_y_no_primos.txt",una_matriz_por_central,fmt="%i")
#np.savetxt("centrales_no_generadores.txt",centrales_no_generadores,fmt="%i")

f.close()
end = time.time()  
print(end-start)

