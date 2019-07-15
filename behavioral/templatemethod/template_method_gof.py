#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""template_method_gof.py"""
from abc import abstractmethod

class Template:
    def show(self): print(f'Template {self._get_product()}')
    @abstractmethod
    def _get_product(self): pass
class ProductA(Template):
    def _get_product(self): return self
class ProductB(Template):
    def _get_product(self): return self
if __name__ == '__main__':
    pa = ProductA()
    pb = ProductB()
    pa.show()
    pb.show()
