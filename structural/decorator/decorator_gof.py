#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""decorator_gof.py"""
from abc import abstractmethod, ABC

class Component:
    def __init__(self, name): self.name = name
    @abstractmethod
    def show(self): pass
class Product(Component):
    def show(self): return self.name
class Decorator(Component, ABC):
    def __init__(self, name, component):
        super().__init__(name)
        self.component = component
class DecoratorA(Decorator):
    def show(self): return self.name + self.component.show()
class DecoratorB(Decorator):
    def show(self): return self.name + self.component.show()
if __name__ == '__main__':
    p = Product('p')
    da = DecoratorA('da', p)
    db = DecoratorA('db', da)
    print(p.show())
    print(da.show())
    print(db.show())
