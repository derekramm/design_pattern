#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""abstract_factory_gof.py"""
from abc import abstractmethod

class IProduct1: pass
class IProduct2: pass
class ProductA1(IProduct1): pass
class ProductA2(IProduct2): pass
class ProductB1(IProduct1): pass
class ProductB2(IProduct2): pass
class AbstractFactory:
    @staticmethod
    def choose_factory(factory_name):
        factories = dict(a=FactoryA, b=FactoryB)
        return factories[factory_name]()
    @abstractmethod
    def get_product1(self): pass
    @abstractmethod
    def get_product2(self): pass
class FactoryA(AbstractFactory):
    def get_product1(self): return ProductA1()
    def get_product2(self): return ProductA2()
class FactoryB(AbstractFactory):
    def get_product1(self): return ProductB1()
    def get_product2(self): return ProductB2()
if __name__ == '__main__':
    fa = AbstractFactory.choose_factory('a')
    fb = AbstractFactory.choose_factory('b')
    print(fa)
    print(fb)
    pa1 = fa.get_product1()
    pa2 = fa.get_product2()
    pb1 = fb.get_product1()
    pb2 = fb.get_product2()
    print(pa1)
    print(pa2)
    print(pb1)
    print(pb2)
