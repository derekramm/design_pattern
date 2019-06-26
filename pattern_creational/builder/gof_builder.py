#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_builder.py"""

class Builder(object):
    def __init__(self): pass
    def build_part_a(self): pass
    def build_part_b(self): pass
    def build_part_c(self): pass

class BuilderA(Builder):
    def build_part_a(self): print('BuilderA build_part_a()')
    def build_part_b(self): print('BuilderA build_part_b()')
    def build_part_c(self): print('BuilderA build_part_c()')

class BuilderB(Builder):
    def build_part_a(self): print('BuilderB build_part_a()')
    def build_part_b(self): print('BuilderB build_part_b()')
    def build_part_c(self): print('BuilderB build_part_c()')

class Director(object):
    def __init__(self): self.builder = None
    def build(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()

if __name__ == '__main__':
    d = Director()
    d.builder = BuilderA()
    d.build()
    d.builder = BuilderB()
    d.build()