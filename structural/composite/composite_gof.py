#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""composite_gof.py"""

from abc import ABCMeta, abstractmethod

class Component(object, metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add(self, c): raise NotImplementedError

    @abstractmethod
    def remove(self, c): raise NotImplementedError

    def show(self, level):
        print('-' * level + self.name)

class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.components = []

    def add(self, c):
        self.components.append(c)
        return self

    def remove(self, c):
        self.components.remove(c)
        return self

    def show(self, level):
        super(Composite, self).show(level)
        for c in self.components:
            c.show(level + 1)

class Leaf(Component):
    def add(self, c): raise NotImplementedError

    def remove(self, c): raise NotImplementedError

if __name__ == '__main__':
    root = Composite('root')
    node_a, node_b = Composite('nodeA'), Composite('nodeB')
    node_1, node_2 = Leaf('node1'), Leaf('node2')
    root.add(node_a.add(node_1).add(node_2)).add(node_b.add(node_1).add(node_2))
    root.show(0)
