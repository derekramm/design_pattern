#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_factory_method.py"""

class Product(object): pass
class ProductA(Product): pass
class ProductB(Product): pass

class Factory(object):
    @staticmethod
    def choose_factory(factory_name='a'): return dict(a=FactoryA(), b=FactoryB())[factory_name]
    def get_product(self): pass

class FactoryA(Factory):
    def get_product(self): return ProductA()

class FactoryB(Factory):
    def get_product(self): return ProductB()

if __name__ == '__main__':
    print(Factory.choose_factory('a').get_product())
    print(Factory.choose_factory('b').get_product())