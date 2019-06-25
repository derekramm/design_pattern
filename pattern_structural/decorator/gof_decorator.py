#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_decorator.py"""

from abc import ABCMeta, abstractmethod, ABC

class Product(object, metaclass=ABCMeta):
    @abstractmethod
    def show(self): pass
class ProductA(Product):
    def show(self): return 'ProductA'
class ProductB(Product):
    def show(self): return 'ProductB'

class Decorator(Product, ABC):
    def __init__(self):
        self.component = None
class DecoratorA(Decorator):
    def show(self): return 'DecoratorA', self.component.show()
class DecoratorB(Decorator):
    def show(self): return 'DecoratorB', self.component.show()

if __name__ == '__main__':
    pa, pb = ProductA(), ProductB()
    da, db = DecoratorA(), DecoratorB()
    print(pa.show(), pb.show())
    da.component = pa
    db.component = da
    print(da.show(), db.show())
    db.component = pb
    da.component = db
    print(da.show(), db.show())
