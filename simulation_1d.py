# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:09:19 2017

@author: yume
"""

import matplotlib.pyplot as plt
import walking_model
import evaluation_function


# Leader
# plotする範囲を指定、plot数も指定
class Leader(object):
    def __init__(self, goal_x, v_max, initial_pos, leading_relative_pos,
                 Kp_goal, Ki_goal, Kp_follower, importance_goal):
        # 目標位置
        self.goal_x = goal_x
        self.leading_relative_pos = leading_relative_pos
        # 自己位置
        self.x = initial_pos  # 現在位置
        # 速度
        self.v_max = v_max
        self.v_x = 0
        self.sum_residual = 0
        self.Kp_goal = Kp_goal
        self.Ki_goal = Ki_goal
        self.Kp_follower = Kp_follower
        self.importance_goal = importance_goal

    def measure(self, target_x, self_x, t):
        self.target_x = target_x
        self.x = self_x
        self.t = t

    def estimate(self):
        pass

    def decide_action(self):
        residual = self.goal_x - self.x  # ゴールとLeader現在位置(目標値からどれだけずれてい)
        self.sum_residual += residual
        v_goal = self.Kp_goal * residual + self.Ki_goal * self.sum_residual

        relative_pos = self.target_x - self.x
        residual = self.leading_relative_pos + relative_pos
        v_follower = self.Kp_follower * residual

        v_x = self.importance_goal * v_goal + \
            (1 - self.importance_goal) * v_follower

        if abs(v_x) > self.v_max:
            if v_x > 0:
                v_x = self.v_max
            else:
                v_x = - self.v_max
        self.v_x = v_x

        print("sum_residual", self.sum_residual)
        print("residual", residual)
        print("relative_pos", relative_pos)

    def move(self):
        self.x = self.x + self.v_x


# Follower
# plotする範囲を指定、plot数も指定
class Follower(object):
    def __init__(self, relative_pos, v_max, initial_pos):
        # LeaderとFollowerの実距離
        self. relative_pos = relative_pos  # LeaderとFollowerの最適距離
        # 自己位置
        self.x = initial_pos  # 現在位置
        # FollowerがLeaderについていく判断
        self.v_x = 0
        self.v_max = v_max

    def measure(self, target_x, self_x, t):
        # LeaderとFollowerの実距離
        self.target_x = target_x
        self.x = self_x
        self.t = t

    def estimate(self):
        pass

    def decide_action(self):
        goal = self.target_x - self.relative_pos
        residual = goal - self.x
        if residual >= 0:
            if residual >= self.v_max:
                self.v_x = walking_model.abusolute_cos(self.t, self.v_max, 1.5)
            else:
                self.v_x = walking_model.abusolute_cos(self.t, residual, 1.5)
        else:
            if residual <= -self.v_max:
                self.v_x = -walking_model.abusolute_cos(
                    self.t, self.v_max, 1.5)
            else:
                self.v_x = -walking_model.abusolute_cos(self.t, residual, 1.5)

    def move(self):
        self.x = self.x + self.v_x


class Logger(object):
    def __init__(self, length_step):
        self.l_x = []  # 現在位置を格納するリスト
        self.f_x = []  # 現在位置を格納するリスト
        self.length_step = length_step

    def log_leader(self, x):
        self.l_x.append(x)

    def log_follower(self, x):
        self.f_x.append(x)

    def display(self):
        plt.plot(self.l_x, "-*")
        plt.plot(self.f_x, "o")
        plt.xlim(0, self.length_step)  # 表の軸を0~20に固定
        plt.grid()
        plt.gcf()
        plt.show()
        print("leader.x", self.l_x[-1])
        print("follower.x", self.f_x[-1])

    def savefig(self, filename):
        plt.savefig(filename)
        self.display()
        plt.draw()

if __name__ == '__main__':
    # 表描画
    goal_x = 11
    relative_pos = 2
    l_v_max = 3
    f_v_max = 2
    l_initial_pos = 0
    f_initial_pos = 0
    length_step = 30
    Kp_goal = 1
    Ki_goal = 0.01
    Kp_follower = 0.7
    importance_goal = 0.4
    n = 0
    sum_residual = []
    reaching_distance = []

    leader = Leader(goal_x, l_v_max, l_initial_pos, relative_pos,
                    Kp_goal, Ki_goal, Kp_follower, importance_goal)
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
        logger.display()

        n += 1  # インクリメント

#    logger.display()
    sum_residual.append(leader.sum_residual)
    reaching_distance.append(evaluation_function.reaching_evaluation_function(
            goal_x, leader.x))

    print(" ")
    print("Kp_goal", Kp_goal)
    print("sum_residual", sum_residual)
    print("Kp_follower", Kp_follower)
    print("reaching_distance", min(reaching_distance))
