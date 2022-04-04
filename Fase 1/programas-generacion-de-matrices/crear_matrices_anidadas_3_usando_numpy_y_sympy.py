# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:24:33 2022

@author: equipo
"""
"""
Este programa genera matrices de primos y no primos no múltiplos de 2 ni de 5
"""

import numpy as np
import time
from sympy.ntheory import isprime

start = time.time()
centrales = []

f = open("matrices_primos_y_no_primos.txt", "a")


for i in range(59,1000):
    if i%2 != 0 and i%5 != 0:
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
    
    numeropares = c//6-(c//6)//5 #Tomamos todos los pares que disten un multiplo de seis pero excluimos los múltiplos de 5 (que son uno de cada cinco)
    pares = np.zeros(numeropares*2, int)
    
    cont = 0
    for i in mul6:
        if i%2 !=0 and i%5 != 0:
            pares[2*cont] = i
            pares[2*cont+1] = 2*c-i
            
        cont += 1
    
    #print(pares)
    #Construimos las matrices posibles y guardamos las que tengan el par más lejano y el más cercano al centro (o el seguno más cercano o lejano en su defecto)
    
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
                        
                        nump = 0
                        for i in matriz:
                            if isprime(i):
                                nump += 1
                                
                        if nump == 9:
                            print(matriz)
                        break
                    
            if matriz_encontrada == 1:
                break
            
    #if matriz_encontrada == 0:
        #centrales_no_generadores.append(c)
        
    if (counter%10==0 and counter>0):
        f.close()
        f = open("matrices_primos_y_no_primos.txt", "a")
        #np.savetxt("matrices_centrales_primos_y_no_primos_de_"+str(counter)+"_a_"+str(counter-50000)+".txt",una_matriz_por_central[counter-50000:counter,:],fmt="%i")
        
#np.savetxt("matrices_centrales_primos_y_no_primos.txt",una_matriz_por_central,fmt="%i")
#np.savetxt("centrales_no_generadores.txt",centrales_no_generadores,fmt="%i")

f.close()
end = time.time()  
print(end-start)

