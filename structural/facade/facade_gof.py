#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""facade_gof.py"""

class ProductA(object):
    def show(self): print(f'{self.__class__.__name__} show')

class ProductB(object):
    def show(self): print(f'{self.__class__.__name__} show')

class ProductC(object):
    def show(self): print(f'{self.__class__.__name__} show')

class Facade(object):
    def __init__(self, *products):
        self.products = products

    def show(self):
        for p in self.products:
            p.show()

if __name__ == '__main__':
    Facade(ProductA(), ProductB(), ProductC()).show()
