#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""strategy_gof.py"""
from abc import ABCMeta, abstractmethod

class IFunc(metaclass=ABCMeta):
    @abstractmethod
    def handle(self): pass
class FuncA(IFunc):
    def handle(self): return self.handle
class FuncB(IFunc):
    def handle(self): return self.handle
class Product:
    def __init__(self, func): self.func = func
    def request(self):  print(self, self.func.handle())
if __name__ == '__main__':
    p = Product(FuncA())
    p.request()
    p.func = FuncB()
    p.request()
