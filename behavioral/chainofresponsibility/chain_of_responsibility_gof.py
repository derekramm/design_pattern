#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""chain_of_responsibility_gof.py"""
from abc import abstractmethod

class Chain:
    def __init__(self, level):
        self.level = level
        self.next = None
    @abstractmethod
    def handle(self, number): pass
class ChainA(Chain):
    def handle(self, number):
        if self.level >= number:
            print(self, number)
        elif self.next:
            self.next.handle(number)
        else:
            pass
class ChainB(Chain):
    def handle(self, number):
        if self.level >= number:
            print(self, number)
        elif self.next:
            self.next.handle(number)
        else:
            pass
if __name__ == '__main__':
    ca = ChainA(10)
    cb = ChainB(100)
    ca.next = cb
    ca.handle(10)
    ca.handle(100)
