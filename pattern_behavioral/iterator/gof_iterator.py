#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_iterator.py"""

class Iterator(object):
    def has_next(self): pass
    def next(self): pass
    def current(self): pass
    def first(self): pass

class Aggregate(object):
    def __init__(self): self.items = []
    def get_iterator(self): pass

class ConcreteIterator(Iterator):
    def __init__(self, aggregate): self.index, self.aggregate = 0, aggregate
    def has_next(self): return self.index < len(self.aggregate.items)
    def next(self):
        if self.index < len(self.aggregate.items):
            result = self.aggregate.items[self.index]
            self.index += 1
            return result
    def current(self): return self.aggregate.items[self.index]
    def first(self): return self.aggregate[0]

class ConcreteAggregate(Aggregate):
    def __init__(self):
        super().__init__()
        self.iterator = ConcreteIterator(self)

if __name__ == '__main__':
    ca = ConcreteAggregate()
    ca.items.append('a')
    ca.items.append('b')
    ca.items.append('c')
    itor = ca.iterator
    while itor.has_next():
        print(itor.next())