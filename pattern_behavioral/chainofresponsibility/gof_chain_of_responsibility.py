#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_chain_of_responsibility.py
"""

class Chain(object):
    """职责链父类"""
    def __init__(self, level):
        """
        初始化方法
        :param level: 能够处理的级别
        """
        self.level = level
        self.next = None  # 下一个处理对象，类型还是职责链父类

    def handle(self, number):
        """
        处理方法
        :param number:  # 被处理的数字
        :return: # None
        """
        if self.level >= number:
            print(f'{self} handle {number}')  # 如果权限满足，直接处理
        elif self.next:  # 如果下一个处理对象不为空
            self.next.handle(number)  # 调用下一个处理对象处理数字
        else:
            pass

class ChainA(Chain):
    """职责链子类对象A"""
    pass

class ChainB(Chain):
    """职责链子类对象B"""
    pass

if __name__ == '__main__':
    ca, cb = ChainA(10), ChainB(100)  # 创建职责链对象
    ca.next = cb  # 配置传递关系
    ca.handle(10)  # 请求都通过职责链子类对象A处理
    ca.handle(100)  # 请求都通过职责链子类对象A处理，A如果没有权限处理，会提交给下一个处理对象B
