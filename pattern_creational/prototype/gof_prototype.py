#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_prototype.py"""

from copy import copy, deepcopy

class Prototype(object):
    def __init__(self, val, ref):
        self.val = val
        self.ref = ref
    def clone(self): return copy(self)
    def deep_clone(self): return deepcopy(self)

if __name__ == '__main__':
    p = Prototype('p', ['p'])
    p1, p2 = p.clone(), p.deep_clone()
    print(p.__dict__, p1.__dict__, p2.__dict__)
    p.val = 'prototype'
    p.ref[0] = ['prototype']
    print(p.__dict__, p1.__dict__, p2.__dict__)
