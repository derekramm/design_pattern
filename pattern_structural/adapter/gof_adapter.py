#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_adapter.py"""

class Target(object):
    def show(self): pass

class Adaptee(object):
    def request(self): return f'{self.__class__.__name__} request()'

class Adapter(Target):
    def __init__(self): self.adaptee = Adaptee()
    def show(self): return 'Adapter with', self.adaptee.request()

if __name__ == '__main__':
    print(Adapter().show())