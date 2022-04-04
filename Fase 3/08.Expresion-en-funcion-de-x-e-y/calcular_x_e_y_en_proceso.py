# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 13:51:00 2021

@author: equipo
"""
"""
Este programa obtiene los valores de x y de y para todas las matrices almacenadas
en el archivo de excel 'file'
"""

import numpy as np
import pandas as pd

file = 'th5-2000.xlsx'
df = pd.read_excel(file, sheet_name = 'Hoja77', skiprows=5)
print(df.head())


ec = df.iloc[:,5]
edc = df.iloc[:,8]
eai = df.iloc[:,1]

A = np.array([[10, -5], [8, -7]])

X = np.zeros([len(ec),2])
dif = np.zeros(len(ec),int)

for i in range(len(ec)):
    B = np.array([ec[i], edc[i]])
    X[i,:] = np.linalg.inv(A).dot(B)
    dif[i] = int(np.round(10*X[i,0]-5*X[i,1] - eai[i]))

print(X)
print(dif)