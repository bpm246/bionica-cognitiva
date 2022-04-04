# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:01:03 2021

@author: equipo
"""
"""
Este programa crea matrices anidadas de primos de 5x5 sin utilizar numpy
"""

#Construirmatrices de 5x5

import itertools
import time

start = time.time()

"""
Funcion que crea las matrices de 3
"""

def crear_matrices_3(c, esprimo):

    
    numero_posible = 0
    numeronumpos = 0
    numeros_posibles = [0 for i in range(((c-1)//6)*2)]
    
    
    a,b,x13,x21,x23,x31,x32,x33 = 0,0,0,0,0,0,0,0
    matriz = [0 for i in range(9)]
    matriz_ordenada = [0 for i in range(9)]
    matrices_encontradas = [[0 for i in range(9)] for j in range(c*100)] #En esta lista se van a almacenar todas las matrices que se encuentren
     
    contmatrices = 0
    
    
    
    contnumpos = 0
    numero_posible = c
    
    #Elegimos, de entre los números que tienen una diferencia con el central igual a un múltiplo de 6, los que son primos
    for i in range(c//6):
        numero_posible -= 6
        if esprimo[numero_posible] and esprimo[2*c-numero_posible]:
            numeros_posibles[contnumpos] = numero_posible
            numeros_posibles[contnumpos+1] = 2*c-numero_posible
            contnumpos += 2
        
            
    numeronumpos = contnumpos       
    
    matriz_repetida = 0
    if numeronumpos>= 8:        
        #Buscamos, de entre la lista de primos, todas las combinaciones posibles para a y b
        for a in numeros_posibles[:numeronumpos]:
            for b in numeros_posibles[:numeronumpos]:
                if a != b:
                    x13 = -a-b+3*c
                    x21 = -2*a-b+4*c
                    x23 = 2*a+b-2*c
                    x31 = a+b-c
                    x32 =-b+2*c
                    x33 = -a+2*c
                    
                    
                    matriz[0] = a
                    matriz[1] = b
                    matriz[2] = x13
                    matriz[3] = x21
                    matriz[4] = c
                    matriz[5] = x23
                    matriz[6] = x31
                    matriz[7] = x32
                    matriz[8] = x33
                    
                    
                    
                    #Comprobamos si la matriz es válida
                    matriz_ordenada[:] = sorted(matriz)
                    #Comprobamos que no se repita ningun elemento
                    if matriz_ordenada[0] != matriz_ordenada[1] and matriz_ordenada[1] != matriz_ordenada[2] and matriz_ordenada[2] != matriz_ordenada[3] and matriz_ordenada[3] != matriz_ordenada[4] and matriz_ordenada[4] != matriz_ordenada[5] and matriz_ordenada[5] != matriz_ordenada[6] and matriz_ordenada[6] != matriz_ordenada[7] and matriz_ordenada[7] != matriz_ordenada[8]:
                        #Comprobamos que todos los elementos sean positivos
                        if x13 > 0 and x21 > 0 and x23 > 0 and x31 > 0:
                            if esprimo[x13] and esprimo[x21] and esprimo[x23] and esprimo[x31]:
                            
                                matriz_repetida = 0
                                for matriz_encontrada in matrices_encontradas[:contmatrices]:
                                    if sorted(matriz) == sorted(matriz_encontrada):
                                        matriz_repetida = 1
                                        break
                                #Si cumple todas las condiciones, entonces almacenamos la matriz
                                
                                if matriz_repetida == 0:
                                    matrices_encontradas[contmatrices][0] = matriz[0]
                                    matrices_encontradas[contmatrices][1] = matriz[1]
                                    matrices_encontradas[contmatrices][2] = matriz[2]
                                    matrices_encontradas[contmatrices][3] = matriz[3]
                                    matrices_encontradas[contmatrices][4] = matriz[4]
                                    matrices_encontradas[contmatrices][5] = matriz[5]
                                    matrices_encontradas[contmatrices][6] = matriz[6]
                                    matrices_encontradas[contmatrices][7] = matriz[7]
                                    matrices_encontradas[contmatrices][8] = matriz[8]
                                    
                                    contmatrices += 1
                    
                        
                
                
    nmatrices = contmatrices   #Numero total de matrices que se han encontrado 
    return matrices_encontradas[:nmatrices]


"""
Programa principal
"""

cmin = 475
cmax = 500
counter = 0

matricesde3 = [[0 for i in range(9)] for j in range(10000)]
nmatrices3 = 0

paresde3 = [[0,0],[0,0],[0,0],[0,0]]


elemento1 = 0
elemento2 = 0
par = [0,0]


nmaxpares = (cmax)//6

pares = [[0,0] for i in range(nmaxpares)]

nmaxcombpos = ((nmaxpares))*(nmaxpares-1)*(nmaxpares-2)*(nmaxpares-3)*(nmaxpares-4)//120
combpos = [[0,0,0,0,0] for i in range(nmaxcombpos)]

matrizvalida = 0

Nmatrices = 100000

parparamatriz = tuple(([0 for i in range(5)],[0 for i in range(5)]))
aux = [0 for i in range(10)]

posacambiar1 = 0
posacambiar2 = 0

eesq1 = 0
eesq2 = 0
eesq3 = 0

mat1D = [0 for i in range(25)]

ya = 0

countermatrices = 0
subcountermatrices = 0

#Antes de empezar a buscar matrices, creamos una lista que almacene si un número es primo o no 
#Si el elemento esprimo[i] es igual 1 entonces el número i será primo, pero si es 0, no.

esprimo = [1 for x in range(cmax*2)]
esprimo[0] = 0
esprimo[1] = 0

i = 2
# Utilizamos la Criba de Erastótenes (https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes)
# para buscar todos los primos hasta el doble del máximo central posible

while i*i <= (cmax*2):
    # Si ya hemos eliminado este número continuamos
    if esprimo[i] == 0:
        i += 1
        continue

    j = 2*i
    while j < (cmax*2):
        # Eliminamos este número, ya que es compuesto
        esprimo[j] = 0
        # Incrementamos j en i unidades porque queremos tachar todos los múltiplos
        j += i

    i += 1
    
primos = []

for i in range(cmin,cmax+1):
    if esprimo[i]:
        primos.append(i)
        
        
matrices_encontradas = []

f = open("matrices_5_primos.txt", "a")

for c in primos:
    
    matrices_encontradas = []
    #Construimos la matriz de 3x3
    
    counter = 0
    for matriz3 in crear_matrices_3(c, esprimo):
        matricesde3[counter][:] = matriz3[:]
        counter += 1
        
    nmatrices3 = counter
    
    matrizvalida = 0
    
    #Ahora construimos el anillo de 5x5 para cada una de las posibilidades de 3x3
        
    for h in range(0,nmatrices3):
        print("Matriz de 3: " + str(h))
        mat3 = matricesde3[h]
        
        pares = [[0,0] for i in range(c//6*2)]
        
        counter= 0
        #Obtenemos todas las posibles descomposiciones de 2c en dos números primos
        
       
        paresde3 = [[min(mat3[0],mat3[8]),max(mat3[0],mat3[8])],
                    [min(mat3[1],mat3[7]),max(mat3[1],mat3[7])],
                    [min(mat3[2],mat3[6]),max(mat3[2],mat3[6])],
                    [min(mat3[3],mat3[5]),max(mat3[3],mat3[5])]] #Pares que ya existen en la matriz de 3 y que no podemos utilizar
                    
                    
        for i in range(c-6,0,-6):
            elemento1 = i
            elemento2 = 2*c-elemento1
            
            par = [elemento1,elemento2]
            if esprimo[elemento1] and esprimo[elemento2]:
                if par != paresde3[0] and par != paresde3[1] and par != paresde3[2] and par != paresde3[3]:
                    pares[counter] = [elemento1,elemento2]
                    counter +=1
        
        npares = counter
        
        
        
        #https://es.wikipedia.org/wiki/Combinatoria#Combinatoria_sin_repetici%C3%B3n
        
        
        counter = 0
        #Elegimos solo las combinaciones que sumen 5c
        for combinacion in itertools.combinations(pares[:npares], 5): #Todos los posibles grupos de cinco pares
            for elementodelparelegido in itertools.product([0,1], repeat=5): #Todas las posibles maneras de sumar eligiendo solo un elemento de cada par
                suma = combinacion[0][elementodelparelegido[0]]+combinacion[1][elementodelparelegido[1]]+combinacion[2][elementodelparelegido[2]]+combinacion[3][elementodelparelegido[3]]+combinacion[4][elementodelparelegido[4]]
                if suma == 5*c:
                    combpos[counter][:] = [combinacion[0][elementodelparelegido[0]],combinacion[1][elementodelparelegido[1]],combinacion[2][elementodelparelegido[2]],combinacion[3][elementodelparelegido[3]],combinacion[4][elementodelparelegido[4]]]
                    counter += 1
        
        ncombpos = counter
        
        
        counter = 0
        subcountermatrices = 0
        
        for parparamatriz in itertools.combinations(combpos[:ncombpos], 2):
            #Elegimos los pares de grupos que compartan un solo elemento (el de la esquina)
            if 10 == len(set([parparamatriz[0][0], parparamatriz[0][1], parparamatriz[0][2], parparamatriz[0][3], parparamatriz[0][4], parparamatriz[1][0], parparamatriz[1][1], parparamatriz[1][2], parparamatriz[1][3], parparamatriz[1][4]]))+1:
                #Buscamos los pares de grupos entre los cuales exista un solo par (cada elemento del par en un grupo distinto)
                                
                for i in range(5):
                    aux[i] = parparamatriz[0][i]
                
                for i in range(5):
                    aux[i+5] = 2*c-parparamatriz[1][i]
                
                if 10 == len(set(aux))+1:
                    #Construimoslasmatrices
                    eesq1 =  list(set(parparamatriz[0]).intersection(parparamatriz[1]))[0]
                    
                    eesq2 = list(set(parparamatriz[0]).intersection([2*c-parparamatriz[1][x] for x in range(5)]))[0]
                    
                    eesq3 = 2*c - eesq2
                    
                    posacambiar1 = parparamatriz[0].index(eesq1)
                    posacambiar2 = parparamatriz[1].index(eesq1)
                    parparamatriz[0][0],parparamatriz[0][posacambiar1] = parparamatriz[0][posacambiar1], parparamatriz[0][0]
                    parparamatriz[1][0],parparamatriz[1][posacambiar2] = parparamatriz[1][posacambiar2], parparamatriz[1][0]
                    
                    posacambiar1 = parparamatriz[0].index(eesq2)
                    posacambiar2 = parparamatriz[1].index(eesq3)
                    parparamatriz[0][4],parparamatriz[0][posacambiar1] = parparamatriz[0][posacambiar1], parparamatriz[0][4]
                    parparamatriz[1][4],parparamatriz[1][posacambiar2] = parparamatriz[1][posacambiar2], parparamatriz[1][4]
                    
                    
                    mat1D = [parparamatriz[0][0], parparamatriz[0][1], parparamatriz[0][2], parparamatriz[0][3], parparamatriz[0][4],
                    parparamatriz[1][1], mat3[0], mat3[1], mat3[2], 2*c-parparamatriz[1][1],
                    parparamatriz[1][2], mat3[3], mat3[4], mat3[5], 2*c-parparamatriz[1][2],
                    parparamatriz[1][3], mat3[6], mat3[7], mat3[8], 2*c-parparamatriz[1][3],
                    parparamatriz[1][4], 2*c - parparamatriz[0][1], 2*c - parparamatriz[0][2], 2*c - parparamatriz[0][3], 2*c - parparamatriz[0][0]]
                    
                    matrizvalida = 1
                    
                    for matriz_encontrada in matrices_encontradas:
                        if sorted(matriz_encontrada) == sorted(mat1D):
                            matrizvalida = 0
                            break
                    
                    
                    
                    if matrizvalida == 1:
                        countermatrices += 1
                        
                        matrices_encontradas.append(mat1D)
                        
                        #Guardamos la matriz que hemos encontrado
                        for m in mat1D:
                            f.write(str(m) + " ")
                            
                        f.write("\n")
                    
                        if countermatrices%1 == 0:
                            print(countermatrices)
                            f.close()
                            f = open("matrices_5_primos.txt", "a")
                            
                            
                        if countermatrices>=Nmatrices:                    
                            ya = 1
                            break
                        
                if ya == 1:
                    break
                
            if ya == 1:
                break
            
            
        if ya == 1:
            break
    
            
f.close()

end = time.time()


print("El programa ha tardado: " + str(end-start) + "s")


        
    
