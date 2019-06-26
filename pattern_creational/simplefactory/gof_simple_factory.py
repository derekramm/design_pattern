#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_simple_factory.py"""

class Product(object): pass
class ProductA(Product): pass
class ProductB(Product): pass

class SimpleFactory(object):
    @classmethod
    def get_product(cls, product_name='a'): return dict(a=ProductA(), b=ProductB())[product_name]

if __name__ == '__main__':
    print(SimpleFactory.get_product('a'))
    print(SimpleFactory.get_product('b'))
