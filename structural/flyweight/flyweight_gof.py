#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""flyweight_gof.py"""

class FlyWeight(object):
    def show(self, x, y):
        print(f'{self.__class__.__name__} <{x},{y}>')

class FlyweightA(FlyWeight): pass

class FlyweightB(FlyWeight): pass

class FlyweightFactory(object):
    flyweights = dict(a=FlyweightA(), b=FlyweightB())

    @classmethod
    def get_flyweight(cls, name='a'):
        return cls.flyweights[name]

if __name__ == '__main__':
    fa1 = FlyweightFactory.get_flyweight('a')
    fb1 = FlyweightFactory.get_flyweight('b')
    fa2 = FlyweightFactory.get_flyweight('a')

    fa1.show(12, 3)
    fb1.show(12, 4)
    fa2.show(13, 4)

    print(fa1 is fa2)
