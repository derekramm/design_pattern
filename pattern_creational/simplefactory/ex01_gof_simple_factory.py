#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_gof_simple_factory.py
简单工厂（静态方法工厂）：
环境：所有子类具备相同父类外观时
问题：希望隐藏具体子类的实例化的过程
办法：根据用户参数，实例化具体子类产品，以父类产品的类型返回"""


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
    """简单工厂类"""

    @staticmethod
    def get_product(product_name):
        """
        根据用户参数实例化具体子类产品
        :param product_name: 产品名称
        :return: 具体子类产品
        """
        products = dict(a=ProductA, b=ProductB)  # 定义子类产品字典
        return products[product_name]()  # 实例化并返回子类产品


# 客户端
if __name__ == '__main__':
    pa = SimpleFactory.get_product('a')  # 获取子类产品A
    pb = SimpleFactory.get_product('b')  # 获取子类产品B

    # 测试
    print(pa, pb)
