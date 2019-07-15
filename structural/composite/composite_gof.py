#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""composite_gof.py"""
class Component:
    def __init__(self, name): self.name = name
    def add(self, c): raise NotImplementedError()
    def remove(self, c): raise NotImplementedError()
    def show(self, level): print('-' * level + self.name)
class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.components = []
    def add(self, c): self.components.append(c)
    def remove(self, c): self.components.remove(c)
    def show(self, level):
        super().show(level)
        for c in self.components: c.show(level + 1)
class Leaf(Component):
    def add(self, c): pass
    def remove(self, c): pass
if __name__ == '__main__':
    root = Composite('root')
    node_a = Composite('node_a')
    node_b = Composite('node_b')
    node_1 = Leaf('node_1')
    node_2 = Leaf('node_2')
    root.add(node_a)
    root.add(node_b)
    node_a.add(node_1)
    node_a.add(node_2)
    node_b.add(node_1)
    node_b.add(node_2)
    root.show(0)
