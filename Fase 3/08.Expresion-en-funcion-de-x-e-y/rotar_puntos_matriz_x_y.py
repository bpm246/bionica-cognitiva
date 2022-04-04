# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:49:21 2021

@author: equipo
"""
"""
Este programa rota los puntos de la matriz expresados en función de x,y,a
"""

import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt

#Matriz de coeficientes
mat = np.array([[[10,-5,-1],[8,-7,2],[12,-3,-1]],
                [[12,-3,0],[10,-5,0],[8,-7,0]],
                [[8,-7,1],[12,-3,-2],[10,-5,1]]]) 


#Matriz de primos
matprim = np.array([[233, 491, 47],
                    [71, 257, 443],
                    [467, 23, 281]])

#Resolvemos el sistema para calcular los valores de x, y, a para este elemento central
A = np.array([mat[1,1], mat[1,2], mat[0,0]])
B = np.array([matprim[1,1], matprim[1,2], matprim[0,0]])
n = np.linalg.inv(A).dot(B)

x= n[0]
y= n[1]
a= n[2]

n = n/np.linalg.norm(n) #Vector unitario perpendicular al plano

matrot = np.zeros((np.shape(mat)[0],np.shape(mat)[1],3))

fig = plt.figure()
ax = Axes3D(fig)

for theta in np.array([0]):#np.arange(0,2*np.pi,np.pi/20):
    #Matriz de rotación entorno al vector n
    #theta = np.pi/2
    costh = np.cos(theta)
    sinth = np.sin(theta)
    
    Rn = np.array([[costh+n[0]*n[0]*(1-costh), n[0]*n[1]*(1-costh)-n[2]*sinth, n[0]*n[2]*(1-costh)+n[1]*sinth],
                   [n[1]*n[0]*(1-costh)+n[2]*sinth, costh+n[1]*n[1]*(1-costh), n[1]*n[2]*(1-costh)-n[0]*sinth],
                   [n[2]*n[0]*(1-costh)-n[1]*sinth, n[2]*n[1]*(1-costh)+n[0]*sinth, costh + n[2]*n[2]*(1-costh)]])
    
    #Vector de traslación (para centrar la matriz en el origen de coordenadas al hacer la rotación)
    vt = -mat[int(np.shape(mat)[0]/2),int(np.shape(mat)[0]/2)]
    
    
    for i in range(np.shape(mat)[0]):
        for j in range(np.shape(mat)[0]):
            matrot[i,j] = np.matmul(Rn,mat[i,j]+vt)-vt
            
    
    ax.scatter(matrot[:,:,0].reshape(np.size(matrot[:,:,0])),matrot[:,:,1].reshape(np.size(matrot[:,:,1])),matrot[:,:,2].reshape(np.size(matrot[:,:,2])),color='green')

           
    if (np.round(np.matmul(matrot,np.array([x,y,a])))!= matprim).any():
        print("theta = " + str(theta) + "no genera la matriz")
        print(np.matmul(matrot,np.array([x,y,a])))
        

ax.scatter(mat[:,:,0].reshape(np.size(mat[:,:,0])),mat[:,:,1].reshape(np.size(mat[:,:,1])),mat[:,:,2].reshape(np.size(mat[:,:,2])),color='blue')
          
plt.xlabel('X',size = 30)
plt.ylabel('Y',size = 30)
ax.set_zlabel('Z',size=30)
"""
def z(i,j):
    return (233-x*i-y*j)/a

def z1(i,j):
    return (281-x*i-y*j)/a

I = np.linspace(7,13,50)

J = np.linspace(-8,-2,50)

I,J = np.meshgrid(I,J)
surf = ax.plot_surface(I,J,z(I,J))
surf1 = ax.plot_surface(I,J,z1(I,J))
"""

plt.show()