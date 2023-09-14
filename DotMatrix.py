# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 18:30:14 2023

@author: admin
"""
import matplotlib
import matplotlib.pyplot as plt

data = [
        [0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0],
        [0,1,0,0,0,1,0],
        [0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0],
        [0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0]]

plt.imshow(data, cmap= 'gray')
plt.show()