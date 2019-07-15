#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""factory_method_gof.py"""
from abc import abstractmethod

class Product: pass
class ProductA(Product): pass
class ProductB(Product): pass
class Factory:
    @staticmethod
    def choose_factory(factory_name):
        factories = dict(a=FactoryA, b=FactoryB)
        return factories[factory_name]()
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
