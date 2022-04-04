# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:28:56 2022

@author: equipo
"""
"""
Este crea matrices anidadas de primos con un rango de diferencias pequeñas y
cuenta la proporcion de ellas que son de primos
"""

from os.path import isfile
from sys import exit

primos_hasta = 20
matrices_por_c = 5000

dif_in = 6
dif_fin = 6*7*5*11
ndif = (dif_fin-dif_in)//6+1
diferencias = [i for i in range(dif_in,dif_fin,6)] 

nombre_archivo_proporciones_matrices = "prop_matrices_primos_para_matrices_diferencias_entre_" + str(dif_in) + "_y_" + str(dif_fin) + ".txt"
#nombre_archivo_matrices = "matrices_diferencia_pequenna_" + str(diferencia_pequenna) + ".txt"

    
if isfile(nombre_archivo_proporciones_matrices):
    print("El archivo '" + nombre_archivo_proporciones_matrices + "' ya existe")
    exit()
    
    
"""
if isfile(nombre_archivo_matrices):
    print("El archivo '" + nombre_archivo_matrices + "' ya existe")
    exit()
"""

nin = 0
nfin = 0

e1,e2,e3,e4,e5,e6,e7,e8,e9 = 0,0,0,0,0,0,0,0,0
matriz = [0 for i in range(9)]
matriz_ordenada = [0 for i in range(9)]
#matrices_encontradas = [[0 for i in range(9)] for j in range((nfin-nin)+1)] #En esta lista se van a almacenar todas las matrices que se encuentren

#Antes de empezar a buscar matrices, creamos una lista que almacene si un número es primo o no 
#Si el elemento esprimo[i] es igual 1 entonces el número i será primo, pero si es 0, no.

nprimos = 0

esprimo = [1 for x in range((dif_fin+1001)*2)]
esprimo[0] = 0
esprimo[1] = 0

i = 2
# Utilizamos la Criba de Erastótenes (https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes)
# para buscar todos los primos hasta el doble del máximo central posible

while i*i <= ((dif_fin+1001)*2):
    # Si ya hemos eliminado este número continuamos
    if esprimo[i] == 0:
        i += 1
        continue

    j = 2*i
    while j < ((dif_fin+1001)*2):
        # Eliminamos este número, ya que es compuesto
        esprimo[j] = 0
        # Incrementamos j en i unidades porque queremos tachar todos los múltiplos
        j += i

    i += 1

nprimos = sum(esprimo)

primos = [0 for i in range(primos_hasta)]
indice = 0
for i in range(primos_hasta):
    if esprimo[i]:
        primos[indice] = i
        indice += 1
        
        
prop_matrices_primos = [0 for i in range(ndif)]
esmatrizprimos = 1

counterdiferencias = -1
for diferencia_pequenna in diferencias:
    
    counterdiferencias += 1
    if counterdiferencias%1== 0:
        print(str(counterdiferencias) + "/" + str(ndif))
        
    #El programa buscara matrices para todos los primos comprendidos entre nin y nfin
    nin = diferencia_pequenna+1
    nfin = nin + 10000
    
    ncentrales = 0
    
    numerodiferencias = 0
    diferencias_grandes_posibles = [0 for i in range((2*nfin-2*diferencia_pequenna)//6)]
    
    matriz_encontrada = 0
    
    counter = 0   
    contmatrices = 0
    contdiferencias = 0
    
    esmultiplo = 0
    
    #Almacenamos en una lista todos los numeros entre nin y nfin
    centrales = [i for i in range(nin,nfin)]   
    ncentrales = nfin-nin
    
            
    #Para cada central buscamos todas las matrices con la diferencia "pequeña" fija que se pueda construir
    #f = open(nombre_archivo_matrices,"a")
    
    counter = 0
    #Cogemos solo las primeras 1500 matrices
    while contmatrices < matrices_por_c and counter < ncentrales:
        
        c = centrales[counter]
        
        #Cada mil primos buscados mostramos en pantalla el estado de la busqueda
        counter += 1    
        
        #Lista en la que vamos a almacenar todos los primos que pueden formar la matriz de acuerdo con las reglas
        diferencias_grandes_posibles[:numerodiferencias] = [0 for i in range(numerodiferencias)]
        
        numerodiferencias = 2*(c-diferencia_pequenna)//6
        diferencias_grandes_posibles[:numerodiferencias] = [i for i in range(-c-diferencia_pequenna + (c+diferencia_pequenna)%6, c-3*diferencia_pequenna, 6)]
         
        
            
                
        
        #Construimos las matrices posibles 
        for diferencia_grande in diferencias_grandes_posibles:
            
            e1 = c - 3*diferencia_pequenna - diferencia_grande
            e2 = c - 2*diferencia_pequenna - diferencia_grande
            e3 = c - diferencia_pequenna - diferencia_grande
            e4 = c - diferencia_pequenna
            e5 = c
            e6 = c + diferencia_pequenna
            e7 = c + diferencia_pequenna + diferencia_grande
            e8 = c + 2*diferencia_pequenna + diferencia_grande
            e9 = c + 3*diferencia_pequenna + diferencia_grande
                        
                        
            matriz[0] = e8
            matriz[1] = e1
            matriz[2] = e6
            matriz[3] = e3
            matriz[4] = e5
            matriz[5] = e7
            matriz[6] = e4
            matriz[7] = e9
            matriz[8] = e2
            
                        
            cont=0
            
            #Comprobamos si la matriz es válida
            matriz_ordenada[:] = sorted(matriz)
            #Comprobamos que no se repita ningun elemento
            if matriz_ordenada[0] != matriz_ordenada[1] and matriz_ordenada[1] != matriz_ordenada[2] and matriz_ordenada[2] != matriz_ordenada[3] and matriz_ordenada[3] != matriz_ordenada[4] and matriz_ordenada[4] != matriz_ordenada[5] and matriz_ordenada[5] != matriz_ordenada[6] and matriz_ordenada[6] != matriz_ordenada[7] and matriz_ordenada[7] != matriz_ordenada[8]:
                if not matriz_ordenada[0] <= 0:
                    
                    esmatrizprimos = 1
                    for m in matriz:
                        if not esprimo[m]:
                            esmatrizprimos = 0
                            break
                    
                    if esmatrizprimos:
                        prop_matrices_primos[counterdiferencias] += 1/float(matrices_por_c)
                        
                    contmatrices += 1
                    
                    """
                    for m in matriz[0:8]:
                        f.write(str(m) + " ")
                        
                    f.write(str(matriz[8]) + "\n")
                    """
                    #break
                            
#f.close()
print(str(ndif) + "/" + str(ndif))

"""
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.plot(diferencias,np.array(prop_matrices_sin_elementos_multiplos_de)[:,5])
plt.plot(diferencias,np.array(prop_matrices_sin_elementos_multiplos_de)[:,7])
plt.plot(diferencias,np.array(prop_matrices_sin_elementos_multiplos_de)[:,11])

plt.xlabel("Diferencia pequeña")
plt.ylabel("Matrices que nocontinen múltiplos")
plt.legend([5,7,11])
"""


f = open(nombre_archivo_proporciones_matrices,"a")

for i in range(ndif):
    f.write(str(diferencias[i]) + " " + str(prop_matrices_primos[i]) + "\n")

f.close()




