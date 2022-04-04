# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:44:55 2021

@author: equipo
"""

import cv2
import numpy as np

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
	       
dim = (256,256)

ma = 0
nummat = 1
for i in range(len(ec)):
    
    imgname = "matriz" + str(ec[i][0]) + "_" + str(ec[i][1]) +"_rand.png"
    
    img = cv2.imread("./test/rand/" + imgname)
    
    #cv2.imshow('sample image',img)
    
    crop_img = img[74:img.shape[0]-69, 103:img.shape[1]-86]
    
    #cv2.imshow('crop_image', crop_img)
    
    resized = cv2.resize(crop_img, dim, interpolation = cv2.INTER_AREA)
    
    #cv2.imshow('resized', resized)
    
    cv2.imwrite("./test/rand/" + imgname, resized)
