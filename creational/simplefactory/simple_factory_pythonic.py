#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""simple_factory_pythonic.py"""


class ProductA(object): pass
class ProductB(object): pass

def get_product(product_name):
    if product_name == 'a': return ProductA()
    elif product_name == 'b': return ProductB()
    else: return None

if __name__ == '__main__':
    print(get_product('a'))
    print(get_product('b'))
