#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""simple_factory_gof.py
GOF版本简单工厂模式"""

class Product(object):
    """父类产品"""
    pass

class ProductA(Product):
    """子类产品A"""
    pass

class ProductB(Product):
    """子类产品B"""
    pass

class SimpleFactory(object):
    """简单工厂"""

    @staticmethod
    def get_product(product_name):
        """
        根据用户参数，实例化具体子类产品，以父类类型返回（Python中效果不明显）
        :param product_name: 产品名称
        :return: 子类产品
        """
        products = dict(a=ProductA, b=ProductB)
        return products[product_name]()

if __name__ == '__main__':
    print(SimpleFactory.get_product('a'))
    print(SimpleFactory.get_product('b'))
