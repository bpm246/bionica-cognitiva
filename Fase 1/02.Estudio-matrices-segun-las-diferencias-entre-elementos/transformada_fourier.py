# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:09:26 2022

@author: Pedro
"""
"""
Este programa calcula la transformada de Fourier de los resultados
de las diferencias encontradas en matrices que carecen de ciertos
números
"""
import matplotlib.pyplot as plt
import numpy as np

lim = 20000
dpm = np.loadtxt("diferencias_pequennas_matrices_no_multiplos_de_primos_hasta_11_(hasta_central_5000).txt",int)
t = dpm[10:1000,0]
y = dpm[10:1000,1]
n = len(t)
dt = t[1]-t[0]

plt.figure()
plt.plot(t, y)
#plt.plot(t, y, 'ko')
plt.xlabel('Tiempo (s)')
plt.ylabel('$y(t)$')

from scipy.fftpack import fft, fftfreq
 
Y = fft(y) / n # Normalizada
Y = Y/sum(abs(Y))
frq = fftfreq(n, dt) # Recuperamos las frecuencias

frq2 = np.zeros(len(frq))
frq2[:len(frq)//2] = frq[len(frq)//2:]
frq2[len(frq)//2:] = frq[:len(frq)//2]

Y2 = np.zeros(len(Y), complex)
Y2[:len(Y)//2] = Y[len(Y)//2:]
Y2[len(Y)//2:] = Y[:len(Y)//2]
plt.figure()
plt.plot(frq2, abs(Y2))
plt.xlim([-0.0001,max(frq2)])
plt.xlabel('Frecuencia')
plt.ylabel('|$Y$|')
plt.title("Transformada de Fourier de las diferencias en las matrices no multiplos de primos hasta 11 (hasta central 5000)")

