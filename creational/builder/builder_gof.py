#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""builder_gof.py"""
from abc import abstractmethod

class Builder:
    @abstractmethod
    def build_part_a(self): pass
    @abstractmethod
    def build_part_b(self): pass
class BuilderA(Builder):
    def build_part_a(self): print(self.build_part_a)
    def build_part_b(self): print(self.build_part_b)
class BuilderB(Builder):
    def build_part_a(self): print(self.build_part_a)
    def build_part_b(self): print(self.build_part_b)
class Director:
    def __init__(self, builder):
        self.builder = builder
    def build(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
if __name__ == '__main__':
    d = Director(BuilderA())
    d.build()
    d.builder = BuilderB()
    d.build()
