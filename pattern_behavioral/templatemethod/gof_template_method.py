#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_template_method.py"""

class Template(object):
    def show(self): print(f'Template {self.get_content()}')
    def get_content(self): pass
class ProductA(Template):
    def get_content(self): return f'ProductA'
class ProductB(Template):
    def get_content(self): return f'ProductB'

if __name__ == '__main__':
    ProductA().show()
    ProductB().show()