#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""factory_method_gof.py"""
from abc import abstractmethod, ABCMeta

class Product(object): pass

class ProductA(Product): pass

class ProductB(Product): pass

class Factory(object, metaclass=ABCMeta):
    @staticmethod
    def choose_factory(factory_name='a'):
        factories = dict(a=FactoryA, b=FactoryB)
        return factories[factory_name]()

    @abstractmethod
    def get_product(self): raise NotImplementedError

class FactoryA(Factory):
    def get_product(self): return ProductA()

class FactoryB(Factory):
    def get_product(self): return ProductB()

if __name__ == '__main__':
    print(Factory.choose_factory('a').get_product())
    print(Factory.choose_factory('b').get_product())
