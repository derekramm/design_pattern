#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_chain_of_responsibility.py
职责链：

定义：
为请求创建了一个接收者对象的链，对请求的发送者和接收者进行解耦。
每个接收者都包含对另一个接收者的引用。
如果一个对象不能处理该请求，就会把请求传给下一个接收者。

意图：
避免请求发送者与接收者耦合在一起，让多个对象都有可能接收请求，
将这些对象连接成一条链，并且沿着这条链传递请求，直到有对象处理它为止。

主要解决：
职责链上的处理者负责处理请求，客户只需要将请求发送到职责链上即可，无须关心请求的处理细节和请求的传递，
所以职责链将请求的发送者和请求的处理者解耦了。

何时使用：
在处理消息的时候以过滤很多道。

如何解决：
拦截的类都实现统一接口。

关键代码：
Handler 里面聚合它自己，在 HandlerRequest 里判断是否合适，如果没达到条件则向下传递，向谁传递之前 set 进去。
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
