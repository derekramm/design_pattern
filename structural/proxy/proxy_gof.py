#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""proxy_gof.py"""

from abc import ABCMeta, abstractmethod

class IFunc(metaclass=ABCMeta):
    @abstractmethod
    def handle(self): raise NotImplementedError()
class Subject(IFunc):
    def handle(self): return self.handle;
class Proxy(IFunc):
    def __init__(self): self.__subject = Subject()
    def handle(self): return self.__subject.handle()
if __name__ == '__main__':
    print(Proxy().handle())
