#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""prototype_gof.py"""
from copy import copy, deepcopy

class Prototype:
    def __init__(self, val, ref):
        self.val = val
        self.ref = ref
    def clone(self): return copy(self)
    def deepclone(self): return deepcopy(self)
if __name__ == '__main__':
    p = Prototype('a', [1, 2, 3])
    p1 = p.clone()
    p2 = p.deepclone()
    p.val = 'b'
    p.ref[:] = [4, 5, 6]
    print(p.__dict__)
    print(p1.__dict__)
    print(p2.__dict__)
