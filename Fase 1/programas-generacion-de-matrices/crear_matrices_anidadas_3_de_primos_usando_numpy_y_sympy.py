# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:24:33 2022

@author: equipo
"""

"""
El siguiente programa construye matrices anidadas de "matrices mágicas" de 3x3. Es decir, matrices de 3x3 en las que cada fila, columna y diagonal principal suman 
lo mismo.

Estas matrices, además, tienen las siguientes características:
    1. La suma de las diagonales filas y columnas suman siempre el triple del elemento central (c)
    2. Imponemo suqe la diferencia entre dos elementos cualesquiera de la matriz es siempre un múltiplo de 6
    3. Están determinadas unívocamente por tres números a, b y c de la siguiente forma:
        
            a       b    -a-b+3c
        -2a-b+4c    c    2a+b-2c
          a+b-c    2c-b    2c-a  
          
    Aunque que a, b y c sean primos no implica que el resto de elementos lo sean. Es decir, es 
    condición necesaria pero no suficiente.
          
Además, el programa descarta todas aquellas matrices que tengan números negativos o repetidos.   
"""

from sympy.ntheory import isprime
import numpy as np


def crear_matrices_3(c):

    ncentrales = 0
    
    numero_posible = 0
    numeronumpos = 0
    numeros_posibles = [0 for i in range(((c-1)//6)*2)]
    
    
    a,b,x13,x21,x23,x31,x32,x33 = 0,0,0,0,0,0,0,0
    matriz = [0 for i in range(9)]
    matriz_ordenada = [0 for i in range(9)]
    matrices_encontradas = [[0 for i in range(9)] for j in range(c*100)] #En esta lista se van a almacenar todas las matrices que se encuentren
     
    counter = 0   
    contmatrices = 0
    
    
    
    contnumpos = 0
    numero_posible = c
    
    #Elegimos, de entre los números que tienen una diferencia con el central igual a un múltiplo de 6, los que son primos
    for i in range(c//6):
        numero_posible -= 6
        if isprime(numero_posible) and isprime(2*c-numero_posible):
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
                    
                    
                    cont=0
                    
                    #Comprobamos si la matriz es válida
                    matriz_ordenada[:] = sorted(matriz)
                    #Comprobamos que no se repita ningun elemento
                    if matriz_ordenada[0] != matriz_ordenada[1] and matriz_ordenada[1] != matriz_ordenada[2] and matriz_ordenada[2] != matriz_ordenada[3] and matriz_ordenada[3] != matriz_ordenada[4] and matriz_ordenada[4] != matriz_ordenada[5] and matriz_ordenada[5] != matriz_ordenada[6] and matriz_ordenada[6] != matriz_ordenada[7] and matriz_ordenada[7] != matriz_ordenada[8]:
                        #Comprobamos que todos los elementos sean positivos
                        if x13 > 0 and x21 > 0 and x23 > 0 and x31 > 0:
                            if isprime(x13) and isprime(x21) and isprime(x23) and isprime(x31):
                            
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

ntop = 10000
nin = 1000
matrices_encontradas = [[0 for i in range(9)] for j in range((ntop-nin)*100)]

nmatrices = 0
for c in range(nin,ntop):
    if isprime(c):
        matrices = crear_matrices_3(c)
        if len(matrices) > 0:
            for matriz in matrices:
                for i in range(9):
                    matrices_encontradas[nmatrices][i] = matriz[i]
                nmatrices += 1

np.savetxt("matrices_primos_hasta_central_" + str(ntop) + ".txt", np.array(matrices_encontradas[:nmatrices]),fmt="%i")
