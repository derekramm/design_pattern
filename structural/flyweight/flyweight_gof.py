#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""flyweight_gof.py"""
class Flyweight:
    def show(self, x, y): return self, x, y
class FlyweightA(Flyweight): pass
class FlyweightB(Flyweight): pass
class UnSharedFlyweight(Flyweight): pass
class FlyweightFactory:
    __flyweights = dict(a=FlyweightA(), b=FlyweightB())
    @classmethod
    def get_flyweight(cls, flyweight_name):
        if flyweight_name in cls.__flyweights: return cls.__flyweights[flyweight_name]
        return UnSharedFlyweight()
if __name__ == '__main__':
    fa1 = FlyweightFactory.get_flyweight('a')
    fa2 = FlyweightFactory.get_flyweight('a')
    fb1 = FlyweightFactory.get_flyweight('b')
    fb2 = FlyweightFactory.get_flyweight('b')
    uf1 = FlyweightFactory.get_flyweight('u')
    uf2 = FlyweightFactory.get_flyweight('u')
    print(fa1.show(1, 1))
    print(fa2.show(1, 2))
    print(fb1.show(2, 1))
    print(fb2.show(2, 2))
    print(uf1.show(3, 1))
    print(uf2.show(3, 2))
    
