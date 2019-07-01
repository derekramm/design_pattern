#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_simple_factory_calculator.py
使用简单工厂实现二元计算器"""

from abc import abstractmethod


class Calculator(object):
    """运算父类"""

    def __init__(self, a, b):
        """
        初始化两个运算数字
        :param a:  第一个运算数字 a
        :param b:  第二个运算数字 b
        """
        self.numa = a
        self.numb = b

    @abstractmethod
    def get_result(self):
        """
        抽象方法，获取两个运算数字的运算结果
        :return: None
        """
        pass


class Add(Calculator):
    """加法运算子类"""

    def get_result(self):
        """
        重写父类抽象方法
        :return: 两个元素数字相【加】的结果
        """
        return self.numa + self.numb


class Sub(Calculator):
    """减法运算子类"""

    def get_result(self):
        """
        重写父类抽象方法
        :return: 两个元素数字相【减】的结果
        """
        return self.numa - self.numb


class Mul(Calculator):
    """乘法运算子类"""

    def get_result(self):
        """
        重写父类抽象方法
        :return: 两个元素数字相【乘】的结果
        """
        return self.numa * self.numb


class Div(Calculator):
    """除法运算子类"""

    def get_result(self):
        """
        重写父类抽象方法
        :return: 两个元素数字相【除】的结果
        """
        if not self.numb:
            return self.numa / self.numb
        raise ZeroDivisionError


class CalculatorFactory(object):
    """简单工厂类"""

    @staticmethod
    def get_calculator(operator):
        """
        根据输入的运算符号，实例化具体运算子类产品
        :param operator: 运算符号
        :return: 运算子类类型（注意：这里没有实例化，只是返回了类型）
        """
        calculators = {'+': Add, '-': Sub, '*': Mul, '/': Div}  # 定义所有运算子类类型的字典
        return calculators[operator]  # 返回对应的运算子类


# 客户端
if __name__ == '__main__':
    # 获取运算符号
    op = input('请输入运算符号：')

    # 获取两个运算数字
    numa = float(input('请输入第一个数字：'))
    numb = float(input('请输入第二个数字：'))

    # 使用工厂，根据运算符号获取运算子类，实例化并赋初始值
    cal = CalculatorFactory.get_calculator(op)(numa, numb)

    # 打印运算结果
    print(f'{numa} {op} {numb} = {cal.get_result()}')
