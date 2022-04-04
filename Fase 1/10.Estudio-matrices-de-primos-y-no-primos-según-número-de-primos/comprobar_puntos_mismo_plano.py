# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:03:03 2021

@author: equipo
"""
"""
Este programa calcula si todos los puntos de la matriz 'mat' expresada en 
términos de x,y,a pertenecen a un mismo plano.
"""

import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt

#Check if every point is in the same plane
mat = np.array([[10,-5,-1],[8,-7,2],[12,-3,-1],
                [12,-3,0],[10,-5,0],[8,-7,0],
                [8,-7,1],[12,-3,-2],[10,-5,1]])

u = mat[1]-mat[0]
v = mat[2]-mat[0]

i = 2
while np.sum(np.abs(np.cross(u,v))) == 0 and i < len(mat):
    i+=1
    v = mat[i]-mat[0]
    
if np.sum(np.abs(np.cross(u,v))) == 0:
    print("Los puntos estan alineados")
    
n = np.cross(u,v)

samepl = 1

for i in range(1,len(mat)):
    vec = mat[i]-mat[0]
    dp = vec.dot(n)
    
    if dp != 0:
        samepl = 0
        print("Este punto no pertenece al plano")
        print(mat[i])
        
if(samepl == 1):
    print("Todos los puntos están en el mismo plano")
    

fig = plt.figure()
 
 # Convertir 2D a 3D
axes3d = Axes3D(fig)
 
# axes3d.scatter3D(x,y,z)
 # Mismo efecto
axes3d.scatter(mat[:,0],mat[:,1],mat[:,2])

plt.xlabel('X',size = 30)
plt.ylabel('Y',size = 30)
axes3d.set_zlabel('Z',size=30)


print("Comprobamos si los valores de x, y, a son los mismos")
A = np.array([mat[4][0:2], mat[5][0:2]])
B = np.array([257, 443])
X = np.linalg.inv(A).dot(B)

print(X)

dif = int(np.round(10*X[0]-5*X[1] - 233))

print(dif)