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
    def get_flyweight(cls, name='c'):
        if name in ('a', 'b'):
            return cls.flyweights[name]
        else:
            return FlyweightC()

if __name__ == '__main__':
    fa1 = FlyweightFactory.get_flyweight('a')
    fa2 = FlyweightFactory.get_flyweight('a')
    fb1 = FlyweightFactory.get_flyweight('b')
    fb2 = FlyweightFactory.get_flyweight('b')
    fc1 = FlyweightFactory.get_flyweight('c')
    fc2 = FlyweightFactory.get_flyweight('c')
    fa1.show(1, 1), fa2.show(1, 2)
    fb1.show(2, 1), fb2.show(2, 2)
    fc1.show(3, 1), fc2.show(3, 2)
    print(id(fa1), id(fa2))
    print(id(fb1), id(fb2))
    print(id(fc1), id(fc2))
