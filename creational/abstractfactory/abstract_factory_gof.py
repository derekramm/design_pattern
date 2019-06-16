#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""abstract_factory_gof.py"""
from abc import ABCMeta, abstractmethod

class Product1(object): pass

class Product2(object): pass

class ProductA1(Product1): pass

class ProductA2(Product2): pass

class ProductB1(Product1): pass

class ProductB2(Product2): pass

class AbstractFactory(object, metaclass=ABCMeta):
    @staticmethod
    def choose_factory(factory_name='a'):
        factories = dict(a=FactoryA, b=FactoryB)
        return factories[factory_name]()

    @abstractmethod
    def get_product1(self): raise NotImplementedError

    @abstractmethod
    def get_product2(self): raise NotImplementedError

class FactoryA(AbstractFactory):
    def get_product1(self): return ProductA1()

    def get_product2(self): return ProductA2()

class FactoryB(AbstractFactory):
    def get_product1(self): return ProductB1()

    def get_product2(self): return ProductB2()

if __name__ == '__main__':
    print(AbstractFactory.choose_factory('a').get_product1())
    print(AbstractFactory.choose_factory('a').get_product2())
    print(AbstractFactory.choose_factory('b').get_product1())
    print(AbstractFactory.choose_factory('b').get_product2())
