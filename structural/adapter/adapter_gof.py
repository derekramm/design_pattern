#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""adapter_gof.py"""
class Adaptee:
    def adaptee_show(self): return self.adaptee_show;
class Target:
    def target_show(self): pass
class Adapter(Target):
    def __init__(self): self.__adaptee = Adaptee()
    def target_show(self):
        print(super().target_show)
        print(self.target_show)
        print(self.__adaptee.adaptee_show())
if __name__ == '__main__':
    Adapter().target_show()
