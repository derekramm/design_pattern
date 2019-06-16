#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""bridge_gof.py"""

from abc import ABCMeta, abstractmethod

class Product(object, metaclass=ABCMeta):
    def __init__(self):
        self.funcs = {}

    def add_func(self, key, func): self.funcs[key] = func

    def remove_func(self, key): del self.funcs[key]

    @abstractmethod
    def execute(self, key): raise NotImplementedError

class ProductA(Product):
    def execute(self, key): return self.__class__.__name__, self.funcs[key].show()

class ProductB(Product):
    def execute(self, key): return self.__class__.__name__, self.funcs[key].show()

class Func(object, metaclass=ABCMeta):
    @abstractmethod
    def show(self): raise NotImplementedError

class FuncA(Func):
    def show(self): return f'{self.__class__.__name__} show'

class FuncB(Func):
    def show(self): return f'{self.__class__.__name__} show'

if __name__ == '__main__':
    pa, pb = ProductA(), ProductB()
    pa.add_func('a', FuncA())
    pa.add_func('b', FuncB())
    pb.add_func('a', FuncA())
    pb.add_func('b', FuncB())
    print(pa.execute('a'))
    print(pa.execute('b'))
    print(pb.execute('a'))
    print(pb.execute('b'))
