#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_visitor.py"""

class Visitor(object):
    def visit_element_a(self, element_a): pass
    def visit_element_b(self, element_b): pass

class Visitor01(Visitor):
    def visit_element_a(self, element_a): print(f'{element_a} visit {self}')
    def visit_element_b(self, element_b): print(f'{element_b} visit {self}')

class Visitor02(Visitor):
    def visit_element_a(self, element_a): print(f'{element_a} visit {self}')
    def visit_element_b(self, element_b): print(f'{element_b} visit {self}')

class Element(object):
    def accept(self, visitor): pass

class ElementA(Element):
    def accept(self, visitor): visitor.visit_element_a(self)

class ElementB(Element):
    def accept(self, visitor): visitor.visit_element_b(self)

class ObjectStructure(object):
    def __init__(self):
        self.elements = [ElementA(), ElementB()]
    def visit(self, visitor):
        for element in self.elements: element.accept(visitor)

if __name__ == '__main__':
    os = ObjectStructure()
    os.visit(Visitor01())
    os.visit(Visitor02())