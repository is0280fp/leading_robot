# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:09:19 2017

@author: yume
"""

import matplotlib.pyplot as plt


# Leader
# plotする範囲を指定、plot数も指定
class Leader(object):
    def __init__(self, goal_x):
        # 目標位置
        self.G_x = goal_x
        # 自己位置
        self.x = 0  # 現在位置
        # 速度
        self.V_x = 1

    def measure(self):
        pass

    def decide_action(self):
        pass

    def move(self):
        self.x = self.x + self.V_x


# Follower
# plotする範囲を指定、plot数も指定
class Follower(object):
    def __init__(self, opt_dis):
        # LeaderとFollowerの実距離
        self.opt_dis = opt_dis  # LeaderとFollowerの最適距離
        # 自己位置
        self.x = 0  # 現在位置
        # FollowerがLeaderについていく判断
        self.dis = 0
        self.dx = 0

    def measure(self, target_x, self_x):
        # LeaderとFollowerの実距離
        self.target_x = target_x
        self.x = self_x

    def decide_action(self):
        self.dis = self.target_x - self.x
        self.dx = self.dis - self.opt_dis

    def move(self):
        self.x = self.x + self.dx


class Logger(object):
    def __init__(self):
        self.l_x = []  # 現在位置を格納するリスト
        self.f_x = []  # 現在位置を格納するリスト

    def log_leader(self, x):
        self.l_x.append(x)
        print(self.l_x)

    def log_follower(self, x):
        self.f_x.append(x)
        print(self.f_x)

    def display(self):
        plt.plot(self.l_x, "-*")
        plt.plot(self.f_x, "o")
        plt.xlim(0, 30)  # 表の軸を0~20に固定
        plt.show()


if __name__ == '__main__':
    # 表描画
    leader = Leader(10)
    follower = Follower(2)
    logger = Logger()

    n = 0
    while n < 20:

        logger.log_leader(leader.x)

        logger.log_follower(follower.x)

        leader.measure()

        leader.decide_action()

        leader.move()

        follower.measure(leader.x, follower.x)

        follower.decide_action()

        follower.move()

        logger.display()

        n += 1  # インクリメント
