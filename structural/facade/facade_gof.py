#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""facade_gof.py"""
class ProductA:
    def show_a(self): print(self.show_a)
class ProductB:
    def show_b(self): print(self.show_b)
class Facade:
    def __init__(self, pa, pb):
        self.pa = pa
        self.pb = pb
    def show(self):
        self.pa.show_a()
        self.pb.show_b()
if __name__ == '__main__':
    Facade(ProductA(), ProductB()).show()
