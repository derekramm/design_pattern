#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""bridge_gof.py"""
from abc import abstractmethod, ABCMeta

class IFunc(metaclass=ABCMeta):
    @abstractmethod
    def handle(self): raise NotImplementedError()
class FuncA(IFunc):
    def handle(self): return self.handle
class FuncB(IFunc):
    def handle(self): return self.handle
class Product:
    def __init__(self): self.__funcs = dict()
    def add(self, key, func): self.__funcs[key] = func
    def remove(self, key): del self.__funcs[key]
    def get(self, key): return self.__funcs[key]
    @abstractmethod
    def request(self, key): pass
class ProductA(Product):
    def request(self, key): print(self.request, self.get(key).handle())
if __name__ == '__main__':
    pa = ProductA()
    pa.add('a', FuncA())
    pa.add('b', FuncB())
    pa.request('a')
    pa.request('b')
