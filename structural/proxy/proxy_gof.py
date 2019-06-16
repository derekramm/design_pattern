#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""proxy_gof.py"""

from abc import ABCMeta, abstractmethod

class Subject(object, metaclass=ABCMeta):
    @abstractmethod
    def show(self): raise NotImplementedError

class Target(Subject):
    def show(self): return f'{self.__class__.__name__} show'

class Proxy(Subject):
    def __init__(self):
        self.target = None

    def show(self):
        if self.target:
            return self.target.show()

if __name__ == '__main__':
    proxy = Proxy()
    proxy.target = Target()
    print(proxy.show())
