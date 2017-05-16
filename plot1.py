# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:25:48 2017

@author: yume
"""
import time
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 10)

 #自己位置
x = []
y = []
pos_x = 0
pos_y = 0

 #目標位置
G_x = 10
G_y = 0

 #速度
V_x = 1
V_y = 0

n = 0
while n < G_x and G_y == 0:
    x.append(pos_x)
    y.append(pos_y)
    pos_x = pos_x + V_x
    plt.plot(x,y,"-o")
    plt.xlim(0,20)
    plt.show()
    n += 1 #インクリメント
    time.sleep(1)

