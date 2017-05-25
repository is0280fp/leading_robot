# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:25:48 2017

@author: yume
"""
import time
import numpy as np
import matplotlib.pyplot as plt

 #plotする範囲を指定、plot数も指定
x = np.linspace(0, 20, 10)

 #自己位置
x = [] #現在位置を格納するリスト
y = []
pos_x = 0 #現在位置
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
    plt.xlim(0,20) #表の軸を0~20に固定
    plt.show()
    n += 1 #インクリメント
    time.sleep(1)

