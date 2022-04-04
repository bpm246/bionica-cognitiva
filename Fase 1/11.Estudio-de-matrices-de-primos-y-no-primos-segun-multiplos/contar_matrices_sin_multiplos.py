# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:58:16 2022

@author: equipo
"""
"""
Este programa cuenta de entre una lista de matrices con diferencia fija
cuántas no poseen ningún múltiplo de ciertos numeros
"""
import numpy as np
import matplotlib.pyplot as plt

matrices = np.loadtxt("matrices_diferencia_pequenna_.txt",int)

matrices_sin_multiplos = [0 for i in range(20)]

multiplo = 0
for i in range(len(matrices)):
    matriz = matrices[i]
    for primo in [2,3,5,7,11,13,17,19]:
        multiplo = 0
        for elemento in matriz:
            if elemento%primo == 0:
                multiplo =1
                break
                    
        if multiplo == 0:
            matrices_sin_multiplos[primo] += 1
                        
            
plt.plot(matrices_sin_multiplos)