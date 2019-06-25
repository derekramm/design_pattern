#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_composite.py"""

from abc import ABCMeta, abstractmethod

class Component(object, metaclass=ABCMeta):
    def __init__(self, name): self.name = name
    def show(self, level):print('-' * level + self.name)

    @abstractmethod
    def add(self, c): pass

    @abstractmethod
    def remove(self, c): pass

class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.components = []

    def remove(self, c): self.components.remove(c)
    def add(self, c):
        self.components.append(c)
        return self

    def show(self, level):
        super().show(level)
        for c in self.components:
            c.show(level + 1)

class Leaf(Component):
    def add(self, c): raise NotImplementedError
    def remove(self, c): raise NotImplementedError

if __name__ == '__main__':
    root = Composite('root')
    na = Composite('na')
    nb = Composite('nb')
    n1 = Leaf('n1')
    n2 = Leaf('n2')
    root.add(na.add(n1).add(n2)).add(nb.add(n1).add(n2))
    root.show(1)

