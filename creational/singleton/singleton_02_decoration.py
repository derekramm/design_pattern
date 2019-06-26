#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""singleton_01_decoration.py
GOF版本单例模式，保证一个类只允许被实例化一次
常见的应用场景有（@小铭，了解即可）：
1、Windows 的控制面板、任务管理器、回收站
2、网站的计数器，所有人上网只需要一个计数器
3、应用程序的日志应用：log4j、slf4j、logkback
4、项目中配置文件的读取
5、线程池（管理多个线程）
6、数据库连接池（管理多个数据库连接）
7、文件系统"""

# Python中实现单例的方式有很多种，这个案例使用装饰器实现单例
def singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

# 使用装饰器装饰希望实现单例模式的类型即可
@singleton
class MySingleton(object): pass

if __name__ == '__main__':
    s1 = MySingleton()
    s2 = MySingleton()
    print(s1, id(s1))
    print(s2, id(s2))
