#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_simple_factory.py"""

class Product(object): pass
class ProductA(Product): pass
class ProductB(Product): pass

class SimpleFactory(object):
    @classmethod
    def get_product(cls, product_name='a'):
        products = dict(a=ProductA(), b=ProductB())
        return products[product_name]

if __name__ == '__main__':
    pa = SimpleFactory.get_product('a')
    pb = SimpleFactory.get_product('b')
    print(pa)
    print(pb)
