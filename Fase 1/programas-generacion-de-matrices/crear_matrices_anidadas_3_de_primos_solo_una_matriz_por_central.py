# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:24:33 2022

@author: equipo
"""

"""
El siguiente programa construye matrices anidadas de números primos o "matrices mágicas de números
primos" de 3x3. Es decir, matrices de 3x3 en las que cada fila, columna y diagonal principal suman 
lo mismo, y que, además, están compuestas exclusivamente por números primos.

Estas matrices tienen las siguientes características:
    1. La suma de las diagonales filas y columnas suman siempre el triple del elemento central (c)
    2. La diferencia entre dos elementos cualesquiera de la matriz es siempre un múltiplo de 6
    3. Están determinadas unívocamente por tres números a, b y c de la siguiente forma:
        
            a       b    -a-b+3c
        -2a-b+4c    c    2a+b-2c
          a+b-c    2c-b    2c-a  
          
    Aunque que a, b y c sean primos no implica que el resto de elementos lo sean. Es decir, es 
    condición necesaria pero no suficiente.
          
Además, el programa descarta todas aquellas matrices que tengan números negativos o repetidos.   
"""

#El programa buscara matrices para todos los primos comprendidos entre nin y nfin
nin = 0
nfin = 1000

ncentrales = 0
centrales = [0 for i in range((nfin-nin)//2+1)]  #En esta lista se van a almacenar todos los primos que existan entre nin y nfin


primo_posible = 0
numeroprimos = 0
primos_posibles = [0 for i in range(((nfin-1)//6-((nfin-1)//6)//5)*2)]


a,b,c,x13,x21,x23,x31,x32,x33 = 0,0,0,0,0,0,0,0,0
matriz = [0 for i in range(9)]
matriz_ordenada = [0 for i in range(9)]
matrices_encontradas = [[0 for i in range(9)] for j in range((nfin-nin)//2+1)] #En esta lista se van a almacenar todas las matrices que se encuentren
matriz_encontrada = 0

counter = 0   
contmatrices = 0
contprimos = 0

#Antes de empezar a buscar matrices, creamos una lista que almacene si un número es primo o no 
#Si el elemento esprimo[i] es igual 1 entonces el número i será primo, pero si es 0, no.

esprimo = [1 for x in range(nfin*2)]
esprimo[0] = 0
esprimo[1] = 0

i = 2
# Utilizamos la Criba de Erastótenes (https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes)
# para buscar todos los primos hasta el doble del máximo central posible

while i*i <= (nfin*2):
    # Si ya hemos eliminado este número continuamos
    if esprimo[i] == 0:
        i += 1
        continue

    j = 2*i
    while j < (nfin*2):
        # Eliminamos este número, ya que es compuesto
        esprimo[j] = 0
        # Incrementamos j en i unidades porque queremos tachar todos los múltiplos
        j += i

    i += 1


#Almacenamos en una lista todos los primos entre nin y nfin
counter = 0
for i in range(nin,nfin):
    if esprimo[i]:
        centrales[counter] = i
        counter += 1
      
        
ncentrales = counter #Número total de primos a estudiar
        
#Para cada primo buscamos si se puede construir una matriz anidada de primos siendo dicho primo el elemento central (c)
counter = 0
for c in centrales[:ncentrales]:
    
    #Cada mil primos buscados mostramos en pantalla el estado de la busqueda
    counter += 1    
    if counter%1000== 0:
        print(str(counter) + "/" + str(ncentrales))
    
    
    #Lista en la que vamos a almacenar todos los primos que pueden formar la matriz de acuerdo con las reglas
    primos_posibles[:] = [0 for i in range(((nfin-1)//6-((nfin-1)//6)//5)*2)]
    
    contprimos = 0
    primo_posible = c
    
    #Elegimos, de entre los números que tienen una diferencia con el central igual a un múltiplo de 6, los que son primos
    for i in range(c//6):
        primo_posible -= 6
        if esprimo[primo_posible] and esprimo[2*c-primo_posible]:
            primos_posibles[contprimos] = primo_posible
            primos_posibles[contprimos+1] = 2*c-primo_posible
            contprimos += 2
        
            
    numeroprimos = contprimos       
    
    #Construimos las matrices posibles y guardamos las que tengan el par más lejano y el más cercano al centro (o el seguno más cercano o lejano en su defecto)
    matriz_encontrada = 0
    if numeroprimos>= 8:        
        #Buscamos, de entre la lista de primos, todas las combinaciones posibles para a y b
        for a in primos_posibles[:numeroprimos]:
            for b in primos_posibles[:numeroprimos]:
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
                            #Comprobamos que todos los elementos sean primos
                            if esprimo[x13] and esprimo[x21] and esprimo[x23] and esprimo[x31] and esprimo[x32] and esprimo[x33]:
                                
                                #Si cumple todas las condiciones, entonces almacenamos la matriz y pasamos al siguiente elemento primo central
                                matriz_encontrada = 1
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
                                break
                        
            
            #Una vez hemos encontrado una matriz concluimos la búsqueda y pasamos al siguiente primo central
            if matriz_encontrada == 1:
                break
            
nmatrices = contmatrices   #Numero total de matrices que se han encontrado (solo se busca una matriz como máximo por cada elemento central)     

print("Entre " + str(nin) + " y " + str(nfin) + " se han encontrado " + str(nmatrices) + " matrices anidadas de primos")   

#Dejamos comentado el siguiente comando porque para intervalos muy grandes la lista de matrices puede ser inmanejable. Descomentar para ver las matrices encontradas.
#print(matrices_encontradas)

