#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_builder.py"""

from abc import ABCMeta, abstractmethod

class Product(object):
    def __init__(self):
        self.part_a = None
        self.part_b = None
        self.part_c = None

class Builder(object, metaclass=ABCMeta):
    def __init__(self):
        self.product = Product()

    @abstractmethod
    def build_part_a(self): pass

    @abstractmethod
    def build_part_b(self): pass

    @abstractmethod
    def build_part_c(self): pass

class BuilderA(Builder):
    def build_part_a(self):
        self.product.part_a = 'BuilderA build part_a'
        return self

    def build_part_b(self):
        self.product.part_b = 'BuilderA build part_b'
        return self

    def build_part_c(self):
        self.product.part_c = 'BuilderA build part_c'
        return self

class BuilderB(Builder):
    def build_part_a(self):
        self.product.part_a = 'BuilderB build part_a'
        return self

    def build_part_b(self):
        self.product.part_b = 'BuilderB build part_b'
        return self

    def build_part_c(self):
        self.product.part_c = 'BuilderB build part_c'
        return self

class Director(object):
    def __init__(self):
        self.builder = None
    def build(self):
        self.builder.build_part_a().build_part_b().build_part_c()
        return self.builder.product

if __name__ == '__main__':
    d = Director()
    d.builder = BuilderA()
    pa = d.build()
    d.builder = BuilderB()
    pb = d.build()
    print(pa.__dict__)
    print(pb.__dict__)