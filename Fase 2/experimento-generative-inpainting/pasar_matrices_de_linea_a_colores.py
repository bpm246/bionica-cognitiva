# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:42:30 2021

@author: equipo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

matrices = np.loadtxt("matrices_test_inv.txt", int)

ec = np.array([[41,2],
	       [73,14],
	       [89,30],
	       [122,56],
	       [127,23],
	       [133,70],
	       [134,93],
	       [135,79],
	       [136,32],
	       [136,74],
	       [144,33],
	       [148,103],
	       [153,52],
	       [155,43],
	       [158,78],
	       [165,95],
	       [167,99],
	       [168,89],
	       [175,95],
	       [180,9]])

nummat = 1
ma = 0
fig, ax = plt.subplots()
for i in range(len(matrices)):
    matriz = matrices[i]
    mathex = []
    for j in range(9):
        ih = hex(matriz[j]*1000)
        ih = ih[2:]
        rgb = "#"
        for k in range(6-len(ih)):
            rgb = rgb + "0"
        rgb = rgb + ih
        mathex.append(rgb)
        
    
    ax.plot(0,0)
    ax.add_patch(Rectangle((0,0),1,1, color = mathex[0]))
    #ax.text(0.4,0.45,matriz[0])
    ax.add_patch(Rectangle((1,0),1,1, color = mathex[1]))
    #ax.text(1.4,0.45,matriz[1])
    ax.add_patch(Rectangle((2,0),1,1, color = mathex[2]))
    #ax.text(2.4,0.45,matriz[2])
    ax.add_patch(Rectangle((0,-1),1,1, color = mathex[3]))
    #ax.text(0.4,-0.55,matriz[3])
    ax.add_patch(Rectangle((1,-1),1,1, color = mathex[4]))
    #ax.text(1.4,-0.55,matriz[4])
    ax.add_patch(Rectangle((2,-1),1,1, color = mathex[5]))
    #ax.text(2.4,-0.55,matriz[5])
    ax.add_patch(Rectangle((0,-2),1,1, color = mathex[6]))
    #ax.text(0.4,-1.55,matriz[6])
    ax.add_patch(Rectangle((1,-2),1,1, color = mathex[7]))
    #ax.text(1.4,-1.55,matriz[7])
    ax.add_patch(Rectangle((2,-2),1,1, color = mathex[8]))
    #ax.text(2.4,-1.55,matriz[8])
    
    ax.axis('off')
    
    if i%100 == 0:
    	print(i)
    
    if ma == matriz[4]:
    	nummat +=1
    else:
    	nummat = 1
    	ma = matriz[4]
    figure_name = "matriz" + str(ec[i][0]) + "_" + str(ec[i][1]) + "_inv"
    	
    plt.savefig("./test/inv/" + figure_name + ".png")
