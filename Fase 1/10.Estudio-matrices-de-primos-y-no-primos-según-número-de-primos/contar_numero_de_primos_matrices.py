"""
De entre las matrices anidadas de primos y no primos almacenadas en filename,
este programa calcula y representa cuántas de ellas tienen 1,2,3,4,5,6,7,8 ó 9
primos. Además, en el caso de las matrices de 2 primos, calcula en que
posición aparecen en cada matriz
"""

import numpy as np
from sympy.ntheory import isprime
import matplotlib.pyplot as plt
from matplotlib import cm

filename = "matrices_primos_y_no_primos_hasta_1000000.txt"
mat = np.loadtxt(filename,int)
pos2primos = np.zeros((9,9),int)
pp1 = -1
pp2 = -1

posicionesprimos = np.zeros((9,9),int)

numprim = np.zeros(len(mat),int)
for i in range(len(mat)):
	m = mat[-i]
	for j in m[0:4]:
		if isprime(j):
			numprim[i] += 1
	for j in m[5:]:
		if isprime(j):
			numprim[i] += 1
			
	if numprim[i] == 8:
		print(isprime(m[4]))
		print(m)
	
	elif numprim[i] == 2:
		pp1 = -1
		pp2 = -1
		for k in range(9):
			if isprime(m[k]) and pp1 <0:
				pp1 = k
			elif isprime(m[k]):
				pp2 = k
		pos2primos[pp1,pp2] += 1
    
	for j in range(9):
		if isprime(m[j]):
			posicionesprimos[numprim[i],j] += 1
			
unique, counts = np.unique(numprim,return_counts = True)
print(unique)
print(counts/len(mat)*100)		

print(pos2primos)

plt.figure()
plt.plot(unique, counts/len(mat)*100)


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X = np.arange(0,9)
Y = np.arange(0,9)
X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y, pos2primos, cmap=cm.coolwarm, linewidth=0, antialiased=False)

for i in range(9):
    plt.figure()
    plt.plot(posicionesprimos[i])
    plt.title(i)

plt.show()
