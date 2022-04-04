# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:28:56 2022

@author: equipo
"""
"""
Este programa crea matrices de diferencias fijas y cuenta cuántos múltiplos
de cada primo hay en ellas
"""

from os.path import isfile
from sys import exit

diferencia_pequenna = 210
primos_hasta = 20

nombre_archivo = "xproporcion_multiplos_hasta_" +str(primos_hasta) + "_matrices_diferencia_pequenna_" + str(diferencia_pequenna) + ".txt"
nombre_archivo_numero_matrices = "xprop_matrices_sin_multiplos_de_primos_hasta_" +str(primos_hasta) + "para_matrices_diferencia_pequenna_" + str(diferencia_pequenna) + ".txt"
#nombre_archivo_matrices = "matrices_diferencia_pequenna_" + str(diferencia_pequenna) + ".txt"

if isfile(nombre_archivo):
    print("El archivo '" + nombre_archivo + "' ya existe")
    exit()
    
if isfile(nombre_archivo_numero_matrices):
    print("El archivo '" + nombre_archivo_numero_matrices + "' ya existe")
    exit()
"""
if isfile(nombre_archivo_matrices):
    print("El archivo '" + nombre_archivo_matrices + "' ya existe")
    exit()
"""

#El programa buscara matrices para todos los primos comprendidos entre nin y nfin
nin = diferencia_pequenna+1
nfin = 300

ncentrales = 0


numerodiferencias = 0
diferencias_grandes_posibles = [0 for i in range((2*nfin-2*diferencia_pequenna)//6)]



e1,e2,e3,e4,e5,e6,e7,e8,e9 = 0,0,0,0,0,0,0,0,0
matriz = [0 for i in range(9)]
matriz_ordenada = [0 for i in range(9)]
#matrices_encontradas = [[0 for i in range(9)] for j in range((nfin-nin)+1)] #En esta lista se van a almacenar todas las matrices que se encuentren


#Antes de empezar a buscar matrices, creamos una lista que almacene si un número es primo o no 
#Si el elemento esprimo[i] es igual 1 entonces el número i será primo, pero si es 0, no.

nprimos = 0

esprimo = [1 for x in range(primos_hasta)]
esprimo[0] = 0
esprimo[1] = 0

i = 2
# Utilizamos la Criba de Erastótenes (https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes)
# para buscar todos los primos hasta el doble del máximo central posible

while i*i <= (primos_hasta):
    # Si ya hemos eliminado este número continuamos
    if esprimo[i] == 0:
        i += 1
        continue

    j = 2*i
    while j < (primos_hasta):
        # Eliminamos este número, ya que es compuesto
        esprimo[j] = 0
        # Incrementamos j en i unidades porque queremos tachar todos los múltiplos
        j += i

    i += 1

nprimos = sum(esprimo)

primos = [0 for i in range(nprimos)]
indice = 0
for i in range(primos_hasta):
    if esprimo[i]:
        primos[indice] = i
        indice += 1

cantidad_elementos_multiplos_de = [0 for i in range(primos_hasta)]
prop_elementos_multiplos_de = [0 for i in range(primos_hasta)]

matrices_sin_elementos_multiplos_de = [0 for i in range(primos_hasta)]
prop_matrices_sin_elementos_multiplos_de = [0 for i in range(primos_hasta)]

tiene_multiplo_de = [ 0 for i in range(primos_hasta)]

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
for c in centrales[:ncentrales]:
    
    #Cada mil primos buscados mostramos en pantalla el estado de la busqueda
    counter += 1    
    if counter%200== 0:
        print(str(counter) + "/" + str(ncentrales))
    
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
                
                tiene_multiplo_de[:] = [ 0 for i in range(primos_hasta)]
                for m in matriz:
                    for primo in primos:
                        if m%primo == 0:
                            cantidad_elementos_multiplos_de[primo] += 1
                            tiene_multiplo_de[primo] = 1
                
                for i in range(primos_hasta):
                    if i in primos and not tiene_multiplo_de[i]:
                        matrices_sin_elementos_multiplos_de[i] += 1
                
                contmatrices += 1
                
                """
                for m in matriz[0:8]:
                    f.write(str(m) + " ")
                    
                f.write(str(matriz[8]) + "\n")
                """
                #break
                            
#f.close()
print(str(ncentrales) + "/" + str(ncentrales))
nmatrices = contmatrices   #Numero total de matrices que se han encontrado (solo se busca una matriz como máximo por cada elemento central)     

for i in range(primos_hasta):
    prop_elementos_multiplos_de[i] = cantidad_elementos_multiplos_de[i]/nmatrices
    
for i in range(primos_hasta):
    prop_matrices_sin_elementos_multiplos_de[i] = matrices_sin_elementos_multiplos_de[i]/float(nmatrices)


import matplotlib.pyplot as plt

plt.figure()
plt.plot(prop_elementos_multiplos_de,'g')
plt.title(diferencia_pequenna)

plt.figure()
plt.plot(prop_matrices_sin_elementos_multiplos_de,'g')
plt.title(diferencia_pequenna)



print("Entre " + str(nin) + " y " + str(nfin) + " se han encontrado " + str(nmatrices) + " matrices con diferencia pequeña " + str(diferencia_pequenna))   

f = open(nombre_archivo,"a")

for i in range(primos_hasta):
    f.write(str(i) + "\t" + str(prop_elementos_multiplos_de[i]) + "\n")
    
f.close()


f = open(nombre_archivo_numero_matrices,"a")

for i in range(primos_hasta):
    f.write(str(i) + "\t" + str(prop_matrices_sin_elementos_multiplos_de[i]) + "\n")
    
f.close()


#Dejamos comentado el siguiente comando porque para intervalos muy grandes la lista de matrices puede ser inmanejable. Descomentar para ver las matrices encontradas.
#print(matrices_encontradas)