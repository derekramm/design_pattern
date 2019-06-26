#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""factory_method_01_gof.py
GOF版本工厂方法模式"""

from abc import ABCMeta, abstractmethod

class Product(object):
    """父类产品"""
    pass

class ProductA(Product):
    """子类产品A"""
    pass

class ProductB(Product):
    """子类产品B"""
    pass

class Factory(object, metaclass=ABCMeta):
    """工厂类：将子类产品的实例化过程延迟到更小一级的子类工厂实现"""

    @staticmethod
    def choose_factory(factory_name):
        """
        根据用户参数选择具体的子类工厂
        :param factory_name: 子类工厂名
        :return: 子类工厂的对象实例
        """
        factories = dict(a=FactoryA(), b=FactoryB())  # 定义字典，存储已经实例化好的子类工厂
        return factories[factory_name]  # 根据用户提供的参数，返回具体子类工厂

    @abstractmethod
    def get_product(self):
        """
        抽象方法：获取产品
        :return: 由子类实现该方法，不同的子类工厂（FactoryA，FactoryB）返回各自对应的子类产品
        """
        pass

class FactoryA(Factory):
    """子类工厂A"""

    def get_product(self):
        """
        实现父类工厂的抽象方法
        :return: 具体子类产品（ProductA）
        """
        return ProductA()

class FactoryB(Factory):
    """子类工厂B"""

    def get_product(self):
        """
        实现父类工厂的抽象方法
        :return: 具体子类产品（ProductA）
        """
        return ProductB()

if __name__ == '__main__':
    fa = Factory.choose_factory('a')  # 获取子类工厂（FactoryA）
    fb = Factory.choose_factory('b')  # 获取子类工厂（FactoryB）
    pa = fa.get_product()  # 获取子类产品（ProductA）
    pb = fb.get_product()  # 获取子类产品（ProductB）
    print(fa, fb)
    print(pa, pb)
