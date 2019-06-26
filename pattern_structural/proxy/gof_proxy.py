#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_proxy.py"""

class Target(object):
    def show(self): return f'{self.__class__.__name__} show()'

class Proxy(object):
    def __init__(self): self.target = Target()
    def show(self): return self.target.show()

if __name__ == '__main__':
    print(Proxy().show())
