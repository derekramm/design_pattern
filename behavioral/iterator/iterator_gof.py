#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""iterator_gof.py"""
from abc import abstractmethod

class Aggregate:
    def __init__(self, *items): self.items = items
    @abstractmethod
    def get_iterator(self): pass
class Iterator:
    @abstractmethod
    def has_next(self): pass
    @abstractmethod
    def next(self): pass
    @abstractmethod
    def current(self): pass
class IteratorA(Iterator):
    def __init__(self, aggregate):
        self.index = 0
        self.aggregate = aggregate
    def has_next(self): return self.index < len(self.aggregate.items)
    def next(self): self.index += 1
    def current(self): return self.aggregate.items[self.index]
class AggregateA(Aggregate):
    def get_iterator(self): return IteratorA(self)
if __name__ == '__main__':
    agg = AggregateA(*'abcde')
    itr = agg.get_iterator()
    while itr.has_next():
        print(itr.current())
        itr.next()
