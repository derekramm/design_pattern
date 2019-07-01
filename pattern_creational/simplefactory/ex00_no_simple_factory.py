#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex00_no_simple_factory.py
不使用简单工厂的情况"""


class Product(object):
    """父类产品"""
    pass


class ProductA(Product):
    """子类产品A"""
    pass


class ProductB(Product):
    """子类产品B"""
    pass


# 客户端
if __name__ == '__main__':
    pa, pb = ProductA(), ProductB()  # 客户端需要认识所有子类产品以及产品的创建过程
    print(pa, pb)
