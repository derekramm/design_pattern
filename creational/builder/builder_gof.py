#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""builder_gof.py"""

from abc import ABCMeta, abstractmethod

class Builder(object, metaclass=ABCMeta):
    @abstractmethod
    def build_part_a(self): raise NotImplementedError

    @abstractmethod
    def build_part_b(self): raise NotImplementedError

class BuilderA(Builder):
    def build_part_a(self): print(f'BuilderA build_part_a')

    def build_part_b(self): print(f'BuilderA build_part_b')

class BuilderB(Builder):
    def build_part_a(self): print(f'BuilderB build_part_a')

    def build_part_b(self): print(f'BuilderB build_part_b')

class Director(object):
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
