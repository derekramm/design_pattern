#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_abstract_factory.py
抽象工厂
环境：系统的产品有多于一个的产品族，而系统只消费其中某一族的产品
问题：解决一系列相关或者相互依赖的子类产品实例化问题
办法：在一个产品族里定义多个产品，在一个工厂里聚合多个同类产品"""

class Product1(object):
    """系列产品1，包含多个子类产品"""
    pass

class Product2(object):
    """系列产品2，包含多个子类产品"""
    pass

class ProductA1(Product1):
    """系列产品1下的子类产品，由工厂A生产"""
    pass

class ProductB1(Product1):
    """系列产品1下的子类产品，由工厂B生产"""
    pass

class ProductA2(Product2):
    """系列产品2下的子类产品，由工厂A生产"""
    pass

class ProductB2(Product2):
    """系列产品2下的子类产品，由工厂B生产"""
    pass

class AbstractFactory(object):
    """抽象工厂"""

    @staticmethod
    def choose_factory(factory_name='a'):
        """
        根据用户参数，选择子类工厂
        :param factory_name: 工厂名称
        :return: 子类工厂
        """
        factories = dict(a=FactoryA, b=FactoryB)  # 创建子类工厂类型的字典
        return factories[factory_name]()  # 不要忘记返回时实例化子类工厂

    def get_product1(self):
        """抽象方法：
        获取1系列的子类产品，具体由子类工厂A和子类工厂B实现"""
        pass

    def get_product2(self):
        """抽象方法：
        获取2系列的子类产品，具体由子类工厂A和子类工厂B实现"""
        pass

class FactoryA(AbstractFactory):
    """子类工厂A"""

    def get_product1(self):
        """
        实现父类工厂的抽象方法，返回1系列产品的具体子类产品
        :return: ProductA1子类产品对象
        """
        return ProductA1()

    def get_product2(self):
        """
        实现父类工厂的抽象方法，返回1系列产品的具体子类产品
        :return: ProductA2子类产品对象
        """
        return ProductA2()

class FactoryB(AbstractFactory):
    """子类工厂B"""

    def get_product1(self):
        """
        实现父类工厂的抽象方法，返回1系列产品的具体子类产品
        :return: ProductB1子类产品对象
        """
        return ProductB1()

    def get_product2(self):
        """
        实现父类工厂的抽象方法，返回1系列产品的具体子类产品
        :return: ProductB2子类产品对象
        """
        return ProductB2()

# 客户端
if __name__ == '__main__':
    fa = AbstractFactory.choose_factory('a')  # 获取子类工厂A
    fb = AbstractFactory.choose_factory('b')  # 获取子类工厂B

    pa1 = fa.get_product1()  # 获取A工厂生产的1系列产品 ProductA1
    pa2 = fa.get_product2()  # 获取A工厂生产的2系列产品 ProductA2

    pb1 = fb.get_product1()  # 获取A工厂生产的1系列产品 ProductB1
    pb2 = fb.get_product2()  # 获取A工厂生产的2系列产品 ProductB2

    # 测试
    print(fa, fb)  # 输出工厂A、工厂B
    print(pa1, pa2)  # 输出产品A1、产品A2
    print(pb1, pb2)  # 输出产品B1、产品B2
