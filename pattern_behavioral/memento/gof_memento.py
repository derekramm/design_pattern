#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_memento.py"""

class Product(object):
    def __init__(self, name, price): self.name, self.price = name, price
    def save(self): return Memento(self.name, self.price)
    def load(self, m): self.name, self.price = m.name, m.price
class Memento(object):
    def __init__(self, name, price): self.name, self.price = name, price
class Director(object):
    def __init__(self): self.mem = None

if __name__ == '__main__':
    d, p = Director(), Product('A', 10)
    d.mem = p.save()
    p.name, p.price = 'B', 20
    p.load(d.mem)
    print(p.__dict__)



