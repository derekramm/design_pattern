#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""simple_factory_gof.py"""

class Product(object): pass
class ProductA(Product): pass
class ProductB(Product): pass

class SimpleFactory(object):
    @staticmethod
    def get_product(product_name):
        if product_name == 'a': return ProductA()
        elif product_name == 'b': return ProductB()
        else: return None

if __name__ == '__main__':
    print(SimpleFactory.get_product('a'))
    print(SimpleFactory.get_product('b'))
