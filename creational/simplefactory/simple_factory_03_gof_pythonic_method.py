#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""simple_factory_03_gof_pythonic_method.py
GOF版本简单工厂模式，符合Python风格的重构（v2.0）
去掉了父类产品（Product），去掉了子类产品（ProductA, ProductB）
如果仅仅是需要调用不同子类产品中的函数，直接声明函数，然后在简单工厂中调用即可
去掉了简单工厂类（SimpleFactory），只保留简单工厂类中的函数：get_product(product_name)
根据用户参数，返回不用的函数即可"""

def show_a(): return 'show_a()函数的执行结果'

def show_b(): return 'show_b()函数的执行结果'

def get_method(method_name):
    """
    根据用户参数，调用具体函数
    :param method_name: 函数名称
    :return: 希望调用的函数
    """
    products = dict(a=show_a, b=show_b)
    return products[method_name]

if __name__ == '__main__':
    print(get_method('a')())
    print(get_method('b')())
