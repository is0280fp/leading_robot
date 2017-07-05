# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:09:19 2017

@author: yume
"""

import evaluation_function
import itertools
from simulation_1d import Leader, Follower, Logger

if __name__ == '__main__':
    # 表描画
    goal_x = 12
    relative_pos = 2
    l_v_max = 3
    f_v_max = 2
    l_initial_pos = 0
    f_initial_pos = 0
    length_step = 27
    Kp_goal = 0
    Ki_goal = 0
    Kp_follower = 0
    n = 0
    sum_residual = []
    reaching_distance = []

    Kp_goals = np.linspace(0.01, 1, 10)
    Ki_goals = np.linspace(0.01, 1, 10)
    Kp_followers = np.linspace(0.01, 1, 10)
    params = itertools.product(Kp_goals, Ki_goals, Kp_followers)

    for Kp_goal, Ki_goal, Kp_follower in params:
        n = 0
        print("Kp_goal", Kp_goal)
        print("Ki_goal", Ki_goal)
        print("Kp_follower", Kp_follower)

        leader = Leader(goal_x, l_v_max, l_initial_pos, Kp_goal, Ki_goal,
                        Kp_follower)
        follower = Follower(relative_pos, f_v_max, f_initial_pos)
        logger = Logger(length_step)

        logger.log_leader(leader.x)
        logger.log_follower(follower.x)

#        print("length_step", length_step)
#        print("n", n)
        while n < length_step:

            leader.measure(follower.x, leader.x, n)
            follower.measure(leader.x, follower.x, n)

            leader.decide_action()
            follower.decide_action()

            leader.move()
            follower.move()

            logger.log_leader(leader.x)
            logger.log_follower(follower.x)

            print("leader.v_x", leader.v_x)
            # logger.display()

            n += 1  # インクリメント
        logger.display()
        sum_residual.append(leader.sum_residual)
        reaching_distance.append(
                evaluation_function.reaching_evaluation_function(
                        goal_x, leader.x))

    print(" ")
    print("Least_sum_residual", min(map(abs, sum_residual)))
    # print(reaching_distance.index(min(reaching_distance)))
    # Kp_f = reaching_distance.index(min(reaching_distance)) * 0.01 + 0.01
    # print("Kp_follower", Kp_f)
    print("Least_reaching_distance", min(reaching_distance))
    print(" ")
    print("sum_residual", sum_residual)
