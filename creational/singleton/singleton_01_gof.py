#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""singleton_01_gof.py
GOF版本单例模式，保证一个类只允许被实例化一次
常见的应用场景有（@小铭，了解即可）：
1、Windows 的控制面板、任务管理器、回收站
2、网站的计数器，所有人上网只需要一个计数器
3、应用程序的日志应用：log4j、slf4j、logkback
4、项目中配置文件的读取
5、线程池（管理多个线程）
6、数据库连接池（管理多个数据库连接）
7、文件系统"""

# Python中实现单例的方式有很多种，这个案例使用传统的懒汉模式实现
import random
import threading
import time

class Singleton(object):
    """创建单例模式类"""
    _instance = None  # 保存Singleton的对象实例，用来判断是否实例化过
    _lock = threading.Lock()  # 用来锁定线程

    def __init__(self):  # 这里的初始化函数仅仅为了延时显式效果
        time.sleep(random.random())

    # 方法在创建对象时被调用，比 __init__ 方法还靠前
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # 外侧判断是否需要线程排队
            cls._lock.acquire()  # 锁定线程

            # 内侧判断是否需要创建对象
            # 如果曾经创建过该对象，就不在创建
            if cls._instance is None:
                # 固定语法，通过调用父类的 __new__ 方法创建 Singleton这个类的实例
                cls._instance = super().__new__(cls)

            cls._lock.release()  # 释放线程锁

        return cls._instance  # 返回对象实例

def task():
    """
    定义一个方法，用来创建单例模式类型的对象
    并输出该对象的地址
    :return:
    """
    s = Singleton()
    print(s, id(s))

if __name__ == '__main__':
    # 循环10次，每次开启一个线程，调用 task 函数创建 Singleton 的对象实例
    for _ in range(10):
        threading.Thread(target=task).start()
