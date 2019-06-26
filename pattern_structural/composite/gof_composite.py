#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_composite.py"""

class Component(object):
    def __init__(self, name): self.name = name
    def show(self, level):print('-' * level + self.name)

    def add(self, c): pass
    def remove(self, c): pass

class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.components = []

    def remove(self, c): self.components.remove(c)
    def add(self, c): self.components.append(c)

    def show(self, level):
        super().show(level)
        for c in self.components: c.show(level + 1)

class Leaf(Component): pass

if __name__ == '__main__':
    root = Composite('root')
    na, nb = Composite('na'), Composite('nb')
    n1, n2 = Leaf('n1'), Leaf('n2')
    root.add(na)
    root.add(nb)
    na.add(n1)
    na.add(n2)
    nb.add(n1)
    nb.add(n2)
    root.show(0)