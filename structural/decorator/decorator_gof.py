#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""decorator_gof.py"""

from abc import ABCMeta, abstractmethod, ABC

class Component(object, metaclass=ABCMeta):
    @abstractmethod
    def show(self): raise NotImplementedError

class ProductA(Component):
    def show(self): return 'ProductA'

class ProductB(Component):
    def show(self): return 'ProductB'

class Decorator(Component, ABC):
    def __init__(self):
        self.target = None

class DecoratorA(Decorator):
    def show(self): return f'<<{self.target.show()}>>'

class DecoratorB(Decorator):
    def show(self): return f'[[{self.target.show()}]]'

if __name__ == '__main__':
    pa, pb = ProductA(), ProductB()
    da, db = DecoratorA(), DecoratorB()
    da.target = pa
    print(da.show())
    db.target = da
    print(db.show())
    db.target = pb
    print(db.show())
    da.target = db
    print(da.show())
