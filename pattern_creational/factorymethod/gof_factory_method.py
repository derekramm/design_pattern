#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_factory_method.py
工厂方法
环境：所有子类具备相同父类外观
问题：希望隐藏具体子类的实例化过程，并延迟到更小一级的子类工厂
办法：根据用户参数，选择子类工厂，再由子类工厂生产具体子类产品"""

class Product(object): pass  # 父类产品
class ProductA(Product): pass  # 子类产品A
class ProductB(Product): pass  # 子类产品B

# 父类工厂
class Factory(object):
    @staticmethod
    # 根据用户参数，选择子类工厂
    def choose_factory(factory_name='a'): return dict(a=FactoryA(), b=FactoryB())[factory_name]
    # 抽象方法，获取产品，由子类工厂实现
    def get_product(self): pass

# 子类工厂A
class FactoryA(Factory):
    def get_product(self): return ProductA()

class FactoryB(Factory):
    def get_product(self): return ProductB()

if __name__ == '__main__':
    print(Factory.choose_factory('a').get_product())
    print(Factory.choose_factory('b').get_product())