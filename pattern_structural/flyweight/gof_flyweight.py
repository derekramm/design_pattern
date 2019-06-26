#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_flyweight.py"""

class Flyweight(object):
    def show(self, x, y): print(f'{self.__class__.__name__} <{x},{y}>')

class FlyweightA(Flyweight): pass
class FlyweightB(Flyweight): pass
class FlyweightC(Flyweight): pass

class FlyweightFactory(object):
    flyweights = dict(a=FlyweightA(), b=FlyweightB())
    @classmethod
    def get_flyweight(cls, name='c'): return cls.flyweights[name] if name in ('a', 'b') else FlyweightC()

if __name__ == '__main__':
    FlyweightFactory.get_flyweight('a').show(1,1)
    FlyweightFactory.get_flyweight('b').show(2,1)
    FlyweightFactory.get_flyweight('c').show(3,1)
