#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""simple_factory_gof_pythonic.py
GOF版本简单工厂模式，符合Python风格的重构（v1.0）
去掉了父类产品（Product），只保留子类产品（ProductA, ProductB）
去掉了简单工厂类（SimpleFactory），只保留简单工厂类中的函数：get_product(product_name)
根据用户参数，实例具体产品即可"""

class ProductA(object):
    """产品A"""
    pass

class ProductB(object):
    """产品B"""
    pass

def get_product(product_name):
    """
    根据用户参数，实例化具体产品
    :param product_name: 产品名称
    :return: 产品
    """
    products = dict(a=ProductA, b=ProductB)
    return products[product_name]()

if __name__ == '__main__':
    print(get_product('a'))
    print(get_product('b'))
