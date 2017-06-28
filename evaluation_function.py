# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:37:53 2017

@author: yume
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def evaluation_function(leader_x, follower_x):
    residual = (leader_x - follower_x) ** 2
    residual = math.sqrt(residual)
    return residual

if __name__ == '__main__':
    leader_x = -6
    follower_x = 1

    print(evaluation_function(leader_x, follower_x))
