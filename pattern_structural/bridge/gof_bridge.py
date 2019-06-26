#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_bridge.py"""

class Product(object):
    def __init__(self): self.funcs = dict()
    def add(self, key, func): self.funcs[key] = func
    def remove(self, key): del self.funcs[key]
    def execute(self, key): return self.__class__.__name__, self.funcs[key].show()

class ConcreteProduct(Product): pass

class Func(object):
    def show(self): pass
class FuncA(Func):
    def show(self): return 'FuncA show()'
class FuncB(Func):
    def show(self): return 'FuncB show()'

if __name__ == '__main__':
    pa = ConcreteProduct()
    fa, fb = FuncA(), FuncB()
    pa.add('a', fa)
    pa.add('b', fb)
    print(pa.execute('a'), pa.execute('b'))
