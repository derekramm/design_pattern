#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_template_method.py
模板方法：
环境：有多个子类共有的方法，且逻辑相同
问题：定义一个操作中的算法骨架，将一些步骤延迟到子类
办法：将通用算法抽象出来"""

class Template(object):
    """模板方法类"""

    def show(self):
        """
        通用算法骨架
        :return:
        """
        return self, {self.get_content()}

    def get_content(self):
        """
        定义抽象方法，由子类实现特有功能
        :return:
        """
        pass

class ProductA(Template):
    """子类产品A"""

    def get_content(self):
        """
        重写父类抽象方法
        :return:
        """
        return self

class ProductB(Template):
    """子类产品B"""

    def get_content(self):
        """
        重写父类抽象方法
        :return:
        """
        return self

if __name__ == '__main__':
    print(ProductA().show())
    print(ProductB().show())
