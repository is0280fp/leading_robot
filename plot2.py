# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:09:19 2017

@author: yume
"""

import matplotlib.pyplot as plt


# Leader
# plotする範囲を指定、plot数も指定
class Leader(object):
    def __init__(self, goal_x, v_max):
        # 目標位置
        self.goal_x = goal_x
        # 自己位置
        self.x = 0  # 現在位置
        # 速度
        self.v_max = v_max
        self.v_x = 0

    def measure(self):
        pass

    def estimate(self):
        pass

    def decide_action(self):
        residual = self.goal_x - self.x  # ゴールとLeader現在位置(目標値からどれだけずれてい)
        if residual >= 0 and residual >= self.v_max:
            self.v_x = self.v_max
        elif residual < 0 and residual <= -self.v_max:
            self.v_x = -self.v_max
        else:
            self.v_x = residual

    def move(self):
        self.x = self.x + self.v_x


# Follower
# plotする範囲を指定、plot数も指定
class Follower(object):
    def __init__(self, relative_pos):
        # LeaderとFollowerの実距離
        self. relative_pos = relative_pos  # LeaderとFollowerの最適距離
        # 自己位置
        self.x = 0  # 現在位置
        # FollowerがLeaderについていく判断
        self.v_x = 0

    def measure(self, target_x, self_x):
        # LeaderとFollowerの実距離
        self.target_x = target_x
        self.x = self_x

    def estimate(self):
        pass

    def decide_action(self):
        residual = self.target_x - self.x
        self.v_x = residual - self.relative_pos

    def move(self):
        self.x = self.x + self.v_x


class Logger(object):
    def __init__(self):
        self.l_x = []  # 現在位置を格納するリスト
        self.f_x = []  # 現在位置を格納するリスト

    def log_leader(self, x):
        self.l_x.append(x)
        #print(self.l_x)

    def log_follower(self, x):
        self.f_x.append(x)
        #print(self.f_x)

    def display(self):
        plt.plot(self.l_x, "-*")
        plt.plot(self.f_x, "o")
        plt.xlim(0, 30)  # 表の軸を0~20に固定
        plt.grid()
        plt.show()


if __name__ == '__main__':
    # 表描画
    goal_x = -11
    relative_pos = -2
    v_max = 5
    leader = Leader(goal_x, v_max)
    follower = Follower(relative_pos)
    logger = Logger()

    n = 0
    logger.log_leader(leader.x)
    logger.log_follower(follower.x)

    while n < 20:

        leader.measure()
        follower.measure(leader.x, follower.x)

        leader.decide_action()
        follower.decide_action()

        leader.move()
        follower.move()

        logger.log_leader(leader.x)
        logger.log_follower(follower.x)

        logger.display()

        n += 1  # インクリメント
