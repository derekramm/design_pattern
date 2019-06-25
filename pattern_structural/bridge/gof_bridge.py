#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_bridge.py"""

from abc import ABCMeta, abstractmethod

class Product(object):
    def __init__(self):
        self.funcs = dict()
    def add(self, key, func): self.funcs[key] = func
    def remove(self, key): del self.funcs[key]
    def execute(self, key): return self.__class__.__name__, self.funcs[key].show()

class ProductA(Product): pass
class ProductB(Product): pass

class Func(object, metaclass=ABCMeta):
    @abstractmethod
    def show(self): pass
class FuncA(Func):
    def show(self): return 'FuncA show'
class FuncB(Func):
    def show(self): return 'FuncB show'

if __name__ == '__main__':
    pa, pb = ProductA(), ProductB()
    fa, fb = FuncA(), FuncB()
    pa.add('a', fa)
    pa.add('b', fb)
    pb.add('a', fa)
    pb.add('b', fb)
    print(pa.execute('a'))
    print(pa.execute('b'))
    print(pb.execute('a'))
    print(pb.execute('b'))
