#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_facade.py"""

class ProductA(object):
    def show_a(self): print(f'{self.__class__.__name__} show_a()')

class ProductB(object):
    def show_b(self): print(f'{self.__class__.__name__} show_b()')

class Facade(object):
    def __init__(self): self.pa, self.pb = ProductA(), ProductB()

    def show(self):
        self.pa.show_a()
        self.pb.show_b()

if __name__ == '__main__':
    Facade().show()
