#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_factory_method.py
工厂方法
环境：所有子类具备相同父类外观
问题：希望隐藏具体子类的实例化过程，并延迟到更小一级的子类工厂
办法：根据用户参数，选择子类工厂，再由子类工厂生产具体子类产品"""

class Product(object):
    """父类产品"""
    pass

class ProductA(Product):
    """子类产品A"""
    pass

class ProductB(Product):
    """子类产品B"""
    pass

class Factory(object):
    """父类工厂"""

    @staticmethod
    def choose_factory(factory_name):
        """
        根据用户参数，选择子类工厂（注意：是子类工厂而不是产品）
        :param factory_name: 工厂名称
        :return: 子类工厂对象
        """
        factories = dict(a=FactoryA(), b=FactoryB())
        return factories[factory_name]

    def get_product(self):
        """
        抽象方法，获取产品，由子类工厂实现
        这个抽象方法实现了延迟的效果
        :return: None
        """
        pass

class FactoryA(Factory):
    """子类工厂A"""

    def get_product(self):
        """
        实现父类抽象方法
        :return: 返回具体子类产品A
        """
        return ProductA()

class FactoryB(Factory):
    """子类工厂B"""

    def get_product(self):
        """
        实现父类抽象方法
        :return: 返回具体子类产品A
        """
        return ProductB()

# 客户端
if __name__ == '__main__':

    fa = Factory.choose_factory('a')  # 获取子类工厂A
    fb = Factory.choose_factory('b')  # 获取子类工厂B

    pa = fa.get_product()  # 获取子类产品A
    pb = fb.get_product()  # 获取子类产品B

    # 测试
    print(fa, fb)
    print(pa, pb)
