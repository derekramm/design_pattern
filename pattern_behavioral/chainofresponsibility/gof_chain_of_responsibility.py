#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_chain_of_responsibility.py"""

class Chain(object):
    def __init__(self, level): self.level, self.next = level, None
    def handle(self, number):
        if self.level>=number: print(f'{self.__class__.__name__} handle {number}')
        elif self.next: self.next.handle(number)
        else: pass
class ChainA(Chain): pass
class ChainB(Chain): pass

if __name__ == '__main__':
    ca, cb = ChainA(10), ChainB(100)
    ca.next = cb
    ca.handle(10)
    ca.handle(100)