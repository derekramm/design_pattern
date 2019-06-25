#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_adapter.py"""

class Target(object):
    def show(self): pass

class Adaptee(object):
    @classmethod
    def request(cls): return 'Adaptee request'

class Adapter(Target):
    def __init__(self): self.adaptee = Adaptee()
    def show(self): return 'Adapter with', self.adaptee.request()

if __name__ == '__main__':
    print(Adapter().show())