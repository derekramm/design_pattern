#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""prototype_gof.py"""

from copy import copy, deepcopy

class Prototype(object):
    def __init__(self, name, nums):
        self.name = name
        self.nums = nums

    def clone(self): return copy(self)

    def deep_clone(self): return deepcopy(self)

if __name__ == '__main__':
    p = Prototype('name', [12, 3])
    p1 = p.clone()
    p2 = p.deep_clone()
    p.name = 'python'
    p.nums[0] = 18
    print(p.__dict__)
    print(p1.__dict__)
    print(p2.__dict__)
