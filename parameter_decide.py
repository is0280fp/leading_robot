# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:21:13 2017

@author: yume
"""

import numpy as np


def Kp_goal_decide(Kp_goal):
    Kp_goal += 0.01
    return Kp_goal

def Ki_goal_decide(Ki_goal):
    Ki_goal += 0.01
    return Ki_goal

def Kp_follower_decide(Kp_follower):
   Kp_follower += 0.01
   return Kp_follower


if __name__ == '__main__':
    i = 0
    Kp_goal = 0.01
    Ki_goal = 0.01
    Kp_follower = 0.01

    for i in np.arange(0.01, 1, 0.01):
        Kp_goal = Kp_goal_decide(Kp_goal)
        Ki_goal = Ki_goal_decide(Ki_goal)
        Kp_follower = Kp_follower_decide(Kp_follower)
        print("Kp_goal", Kp_goal)
        print("Ki_goal", Ki_goal)
        print("Kp_follower", Kp_follower)
