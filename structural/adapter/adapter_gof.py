#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""adapter_gof.py"""

class Adaptee(object):
    def adaptee_show(self): print(f'{self.__class__.__name__} show')

class Target(object):
    def target_show(self): print(f'{self.__class__.__name__} show')

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def target_show(self):
        super().target_show()
        self.adaptee.adaptee_show()

if __name__ == '__main__':
    Adapter(Adaptee()).target_show()
