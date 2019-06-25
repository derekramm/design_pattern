#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_factory_method.py"""

from abc import ABCMeta, abstractmethod

class Product(object): pass
class ProductA(Product): pass
class ProductB(Product): pass

class Factory(object, metaclass=ABCMeta):
    @classmethod
    def choose_factory(cls, factory_name='a'):
        factories = dict(a=FactoryA(), b=FactoryB())
        return factories[factory_name]

    @abstractmethod
    def get_product(self): pass

class FactoryA(Factory):
    def get_product(self): return ProductA()

class FactoryB(Factory):
    def get_product(self): return ProductB()

if __name__ == '__main__':
    fa = Factory.choose_factory('a')
    fb = Factory.choose_factory('b')
    print(fa)
    print(fb)

    pa = fa.get_product()
    pb = fb.get_product()
    print(pa)
    print(pb)
