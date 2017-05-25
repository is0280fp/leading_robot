# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:09:19 2017

@author: yume
"""
import time
import numpy as np
import matplotlib.pyplot as plt

#Leader
 #plotする範囲を指定、plot数も指定
l_x = np.linspace(0, 20, 10)
 #自己位置
l_x = [] #現在位置を格納するリスト
l_y = []
pos_l_x = 0 #現在位置
pos_l_y = 0
 #目標位置
G_l_x = 10
G_l_y = 0
 #速度
V_l_x = 1
V_l_y = 0

 #Follower
 #plotする範囲を指定、plot数も指定
f_x = np.linspace(0, 20, 10)
 #自己位置
f_x = [] #現在位置を格納するリスト
f_y = []
pos_f_x = 0 #現在位置
pos_f_y = 0
# #目標位置
#G_f_x = 10
#G_f_y = 0
# #速度
#V_f_x = 1
#V_f_y = 0

 #FollowerがLeaderについていく判断
#dis = pos_l_x - pos_f_x #LeaderとFollowerの実距離
opt_dis = 2 #LeaderとFollowerの最適距離

 #表描画
n = 0
while n < G_l_x and G_l_y == 0:
    l_x.append(pos_l_x)
    l_y.append(pos_l_y)
    f_x.append(pos_f_x)
    f_y.append(pos_f_y)
    dis = pos_l_x - pos_f_x #LeaderとFollowerの実距離
    if dis > opt_dis:
        pos_f_x = pos_f_x + (dis - opt_dis)
        f_x.append(pos_f_x)
        f_y.append(pos_f_y)
    pos_l_x = pos_l_x + V_l_x
    plt.plot(l_x,l_y,"-*")
    plt.plot(f_x,f_y,"o")
    plt.xlim(0,30) #表の軸を0~20に固定
    plt.show()
    n += 1 #インクリメント
    time.sleep(1)

