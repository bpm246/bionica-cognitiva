# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:24:33 2022

@author: equipo
"""

"""
El siguiente programa construye matrices anidadas de números primos o "matrices mágicas de números
primos" de 3x3 y de entre ellas selecciona aquellas que son matrices de "superprimos".

Además, cuenta si son del tipo 6n+1 o 6n-1
"""

#El programa buscara matrices para todos los primos comprendidos entre nin y nfin
nin = 2000000
nfin = 3000000

ncentrales6nmas1 = 0
ncentrales6nmenos1 = 0
centrales6nmas1 = [0 for i in range((nfin-nin)//10+1)]  #En esta lista se van a almacenar todos los primos que existan entre nin y nfin
centrales6nmenos1 = [0 for i in range((nfin-nin)//10+1)]  #En esta lista se van a almacenar todos los primos que existan entre nin y nfin


primo_posible = 0
primo_complementario = 0
numeroprimos = 0
primos_posibles = [0 for i in range(((nfin-1)//6-((nfin-1)//6)//5)*2)]


a,b,c,x13,x21,x23,x31,x32,x33 = 0,0,0,0,0,0,0,0,0
matriz = [0 for i in range(9)]
matriz_ordenada = [0 for i in range(9)]
#matrices_encontradas = [[0 for i in range(9)] for j in range((nfin-nin)//100+1)] #En esta lista se van a almacenar todas las matrices que se encuentren

#matrices_superprimos6nmas1 = [[0 for i in range(9)] for j in range((nfin-nin)//100+1)] #En esta lista se van a almacenar todas las matrices de "superprimos" que se encuentren
#matrices_superprimos6nmenos1 = [[0 for i in range(9)] for j in range((nfin-nin)//100+1)] #En esta lista se van a almacenar todas las matrices de "superprimos" que se encuentren
superprimos = 0

counter=0
counter6nmas1 = 0 
counter6nmenos1 = 0   
contmatrices = 0
contprimos = 0
contsuperprimos6nmas1 = 0
contsuperprimos6nmenos1 = 0

nmatrices = 0
nsuperprimos6nmas1 = 0
nsuperprimos6nmenos1 = 0
nsuperprimos = 0

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
counter6nmas1 = 0
counter6nmenos1 = 0
for i in range(nin,nfin):
    if esprimo[i] and (i-1)%6 == 0 and esprimo[(i-1)//6]:
        centrales6nmas1[counter6nmas1] = i
        counter6nmas1 += 1
        
    if esprimo[i] and (i+1)%6 == 0 and esprimo[(i+1)//6]:
        centrales6nmenos1[counter6nmenos1] = i
        counter6nmenos1 += 1
      
        
ncentrales6nmas1 = counter6nmas1 #Número total de primos 6n+1 a estudiar
ncentrales6nmenos1 = counter6nmenos1 #Número total de primos 6n-1 a estudiar
        
#Para cada primo buscamos si se puede construir una matriz anidada de primos siendo dicho primo el elemento central (c)
#Primero buscamos en los primos 6nmas1
print("\n\nBuscamos primos 6n+1")
counter6nmas1 = 0
for c in centrales6nmas1[:ncentrales6nmas1]:
    
    #Cada mil primos buscados mostramos en pantalla el estado de la busqueda
    counter += 1    
    if counter%100== 0:
        print(str(counter) + "/" + str(ncentrales6nmas1))
    
    
    #Lista en la que vamos a almacenar todos los primos que pueden formar la matriz de acuerdo con las reglas
    primos_posibles[:] = [0 for i in range(((nfin-1)//6-((nfin-1)//6)//5)*2)]
    
    contprimos = 0
    primo_posible = c
    
    #Elegimos, de entre los números que tienen una diferencia con el central igual a un múltiplo de 6, los que son primos
    for i in range(c//6):
        primo_posible -= 6
        primo_complementario = 2*c-primo_posible
        if esprimo[primo_posible] and (primo_posible-1)%6 == 0 and esprimo[(primo_posible-1)//6]:
            if esprimo[primo_complementario] and (primo_complementario-1)%6 == 0 and esprimo[(primo_complementario-1)//6]:
                primos_posibles[contprimos] = primo_posible
                primos_posibles[contprimos+1] = primo_complementario
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
                                contmatrices += 1
                                superprimos = 0
                                for i in matriz:
                                    if (i+1)%6 == 0 and esprimo[(i+1)//6]:
                                        superprimos += 1
                                    elif (i-1)%6 == 0 and esprimo[(i-1)//6]:
                                        superprimos += 1
                                
                                if superprimos == 9:
                                    #print(matriz)
                                    """
                                    matrices_superprimos6nmas1[contsuperprimos6nmas1][0] = matriz[0]
                                    matrices_superprimos6nmas1[contsuperprimos6nmas1][1] = matriz[1]
                                    matrices_superprimos6nmas1[contsuperprimos6nmas1][2] = matriz[2]
                                    matrices_superprimos6nmas1[contsuperprimos6nmas1][3] = matriz[3]
                                    matrices_superprimos6nmas1[contsuperprimos6nmas1][4] = matriz[4]
                                    matrices_superprimos6nmas1[contsuperprimos6nmas1][5] = matriz[5]
                                    matrices_superprimos6nmas1[contsuperprimos6nmas1][6] = matriz[6]
                                    matrices_superprimos6nmas1[contsuperprimos6nmas1][7] = matriz[7]
                                    matrices_superprimos6nmas1[contsuperprimos6nmas1][8] = matriz[8]
                                    """
                                    contsuperprimos6nmas1 += 1
                                    
                                    
#Después buscamos en los primos 6nmenos1
print("\n\nBuscamos primos 6n-1")
counter6nmenos1 = 0
counter = 0
for c in centrales6nmenos1[:ncentrales6nmenos1]:
    
    #Cada mil primos buscados mostramos en pantalla el estado de la busqueda
    counter += 1    
    if counter%100== 0:
        print(str(counter) + "/" + str(ncentrales6nmenos1))
    
    
    #Lista en la que vamos a almacenar todos los primos que pueden formar la matriz de acuerdo con las reglas
    primos_posibles[:] = [0 for i in range(((nfin-1)//6-((nfin-1)//6)//5)*2)]
    
    contprimos = 0
    primo_posible = c
    
    #Elegimos, de entre los números que tienen una diferencia con el central igual a un múltiplo de 6, los que son primos
    for i in range(c//6):
        primo_posible -= 6
        primo_complementario = 2*c-primo_posible
        if esprimo[primo_posible] and (primo_posible+1)%6 == 0 and esprimo[(primo_posible+1)//6]:
            if esprimo[primo_complementario] and (primo_complementario+1)%6 == 0 and esprimo[(primo_complementario+1)//6]:
                primos_posibles[contprimos] = primo_posible
                primos_posibles[contprimos+1] = primo_complementario
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
                                contmatrices += 1
                                superprimos = 0
                                for i in matriz:
                                    if (i+1)%6 == 0 and esprimo[(i+1)//6]:
                                        superprimos += 1
                                    elif (i-1)%6 == 0 and esprimo[(i-1)//6]:
                                        superprimos += 1
                                
                                if superprimos == 9:
                                    #print(matriz)
                                    """
                                    matrices_superprimos6nmenos1[contsuperprimos6nmenos1][0] = matriz[0]
                                    matrices_superprimos6nmenos1[contsuperprimos6nmenos1][1] = matriz[1]
                                    matrices_superprimos6nmenos1[contsuperprimos6nmenos1][2] = matriz[2]
                                    matrices_superprimos6nmenos1[contsuperprimos6nmenos1][3] = matriz[3]
                                    matrices_superprimos6nmenos1[contsuperprimos6nmenos1][4] = matriz[4]
                                    matrices_superprimos6nmenos1[contsuperprimos6nmenos1][5] = matriz[5]
                                    matrices_superprimos6nmenos1[contsuperprimos6nmenos1][6] = matriz[6]
                                    matrices_superprimos6nmenos1[contsuperprimos6nmenos1][7] = matriz[7]
                                    matrices_superprimos6nmenos1[contsuperprimos6nmenos1][8] = matriz[8]
                                    """
                                    contsuperprimos6nmenos1 += 1
                        
            
            
nmatrices = contmatrices   #Numero total de matrices que se han encontrado (solo se busca una matriz como máximo por cada elemento central)     
nsuperprimos6nmas1 = contsuperprimos6nmas1  #Numero total de matrices de "superprimos" que se han encontrado
nsuperprimos6nmenos1 = contsuperprimos6nmenos1  #Numero total de matrices de "superprimos" que se han encontrado
nsuperprimos = nsuperprimos6nmas1+nsuperprimos6nmenos1

print("Entre " + str(nin) + " y " + str(nfin) + " se han encontrado " + str(nmatrices/8) + " matrices anidadas de primos")   
print("Entre " + str(nin) + " y " + str(nfin) + " se han encontrado " + str(nsuperprimos/8) + " matrices anidadas de superprimos: ") 
print(str(nsuperprimos6nmas1/8) + " matrices del tipo (6n+1)")  
print(str(nsuperprimos6nmenos1/8) + " matrices del tipo (6n-1)")  

"""
print("\n6n+1")
print(matrices_superprimos6nmas1[:nsuperprimos6nmas1])
print("\n6n-1")
print(matrices_superprimos6nmenos1[:nsuperprimos6nmenos1])
"""

