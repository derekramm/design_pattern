#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""visitor_gof.py"""
from abc import abstractmethod

class Visitor:
    @abstractmethod
    def visit_element_a(self, ea): pass
    @abstractmethod
    def visit_element_b(self, eb): pass
class Element:
    @abstractmethod
    def accept(self, visitor): pass
class Visitor1(Visitor):
    def visit_element_a(self, ea): print(self, ea)
    def visit_element_b(self, eb): print(self, eb)
class Visitor2(Visitor):
    def visit_element_a(self, ea): print(self, ea)
    def visit_element_b(self, eb): print(self, eb)
class ElementA(Element):
    def accept(self, visitor): visitor.visit_element_a(self)
class ElementB(Element):
    def accept(self, visitor): visitor.visit_element_b(self)
class Director:
    def __init__(self, *elements): self.elements = elements
    def visit(self, visitor):
        for element in self.elements: element.accept(visitor)
if __name__ == '__main__':
    d = Director(ElementA(), ElementB())
    d.visit(Visitor1())
    d.visit(Visitor2())
