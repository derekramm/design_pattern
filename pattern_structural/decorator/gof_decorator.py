#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_decorator.py"""

class Component(object):
    def show(self): pass
class Product(Component):
    def show(self): return 'ProductA'

class Decorator(Component):
    def __init__(self): self.component = None
class DecoratorA(Decorator):
    def show(self): return 'DecoratorA', self.component.show()
class DecoratorB(Decorator):
    def show(self): return 'DecoratorB', self.component.show()

if __name__ == '__main__':
    p = Product()
    da, db = DecoratorA(), DecoratorB()
    da.component = p
    db.component = da
    print(db.show())
