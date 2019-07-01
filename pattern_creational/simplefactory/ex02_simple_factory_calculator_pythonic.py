#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_simple_factory_calculator.py
使用简单工厂实现二元计算器_Python风格"""

# 初始化两个运算数字
numa, numb = 12, 3


def add():
    """
    加法运算
    :return: 两个元素数字相【加】的结果
    """
    return numa + numb


def sub():
    """
    减法运算
    :return: 两个元素数字相【减】的结果
    """
    return numa - numb


def mul():
    """
    乘法运算
    :return: 两个元素数字相【乘】的结果
    """
    return numa * numb


def div():
    """
    除法运算
    :return: 两个元素数字相【除】的结果
    """
    print(numb)
    if numb:  # 如果 numb 不等于 0
        return numa / numb
    raise ZeroDivisionError


def get_calculator(operator='+'):
    """
    获取运算方法
    :param operator: 运算符号
    :return: 运算方法
    """
    calculators = {'+': add, '-': sub, '*': mul, '/': div}  # 定义所有运算函数的字典
    return calculators[operator]()  # 返回对应的运算方法


# 客户端
if __name__ == '__main__':
    # 获取运算符号
    op = input('请输入运算符号：')

    # 获取两个运算数字
    numa = float(input('请输入第一个数字：'))
    numb = float(input('请输入第二个数字：'))

    # 使用工厂，根据运算符号获取运算子类，实例化并赋初始值
    cal = get_calculator(op)

    # 打印运算结果
    print(f'{numa} {op} {numb} = {cal}')
