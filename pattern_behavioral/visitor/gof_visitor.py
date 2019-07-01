#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_visitor.py
访问者模式"""

from abc import abstractmethod, ABCMeta

class Visitor(object, metaclass=ABCMeta):
    """访问者父类"""

    @abstractmethod
    def visit_element_a(self, element_a):
        """
        抽象方法：访问者访问元素A的事件
        :param element_a: 元素A
        :return:
        """
        pass

    @abstractmethod
    def visit_element_b(self, element_b):
        """
        抽象方法：访问者访问元素B的事件
        :param element_b: 元素B
        :return:
        """
        pass

class Visitor01(Visitor):
    """访问者子类01"""

    def visit_element_a(self, element_a):
        """
        实现访问者父类抽象方法
        :param element_a:  被访问元素A
        :return:
        """
        print(self, element_a)

    def visit_element_b(self, element_b):
        """
        实现访问者父类抽象方法
        :param element_b:  被访问元素B
        :return:
        """
        print(self, element_b)

class Visitor02(Visitor):
    """访问者子类01"""

    def visit_element_a(self, element_a):
        """
        实现访问者父类抽象方法
        :param element_a:  被访问元素A
        :return:
        """
        print(self, element_a)

    def visit_element_b(self, element_b):
        """
        实现访问者父类抽象方法
        :param element_b:  被访问元素B
        :return:
        """
        print(self, element_b)

class Element(object, metaclass=ABCMeta):
    """被访问元素父类"""

    @abstractmethod
    def accept(self, visitor):
        """
        抽象方法：接受访问者的访问
        :param visitor: 访问者父类
        :return:
        """
        pass

class ElementA(Element):
    """被访问元素子类A"""

    def accept(self, visitor):
        """
        实现父类抽象方法
        :param visitor: 访问者对象
        :return:
        """
        visitor.visit_element_a(self)

class ElementB(Element):
    """被访问元素子类B"""

    def accept(self, visitor): visitor.visit_element_b(self)

class ObjectStructure(object):
    """对象结构类（调用者类）"""

    def __init__(self):
        """初始化函数中，先将所有被访问者对象添加到列表中"""
        self.elements = [ElementA(), ElementB()]

    def visit(self, visitor):
        """
        访问方法
        :param visitor: 访问者对象
        :return:
        """
        for element in self.elements:  # 遍历所有被访问元素
            element.accept(visitor)  # 接受访问者的访问

# 客户端
if __name__ == '__main__':
    os = ObjectStructure()  # 创建对象结构类
    os.visit(Visitor01())  # 使用访问者01访问所有元素
    os.visit(Visitor02())  # 使用访问者02访问所有元素
