#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_memento.py
备忘录模式
"""


class Product(object):
    """产品类"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        """
        将产品内部的状态存储到备忘录对象
        :return: 备忘录对象
        """
        return Memento(self.name, self.price)

    def load(self, m):
        """
        将备忘录中存储的状态恢复到产品对象中
        :param m: 备忘录对象
        :return:
        """
        self.name, self.price = m.name, m.price


class Memento(object):
    """备忘录"""

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Director(object):
    """导演类"""

    def __init__(self):
        """关联备忘录"""
        self.mem = None


if __name__ == '__main__':
    d, p = Director(), Product('A', 10)
    d.mem = p.save()
    p.name, p.price = 'B', 20
    p.load(d.mem)
    print(p.__dict__)
