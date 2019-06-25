#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_proxy.py"""

class Target(object):
    @staticmethod
    def show(): return 'Target show'

class Proxy(object):
    def __init__(self):
        self.target = Target()

    def show(self): return self.target.show()

if __name__ == '__main__':
    print(Proxy().show())