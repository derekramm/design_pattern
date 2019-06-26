#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""simple_factory_04_calculator.py
通过简单工厂实现二元运算器"""

numa, numb = 0, 0  # 定义两个数字变量的初始值

def add():
    """

    :return:
    """
    return numa + numb  # 加法

def sub(): return numa - numb  # 减法

def mul(): return numa * numb  # 乘法

def div():  # 除法
    try:
        return numa / numb
    except ZeroDivisionError as ex:
        print(ex)

def get_calculator(op):
    """
    根据运算符号，返回对应的函数
    :param op: 运算符号
    :return: 函数引用
    """
    calculators = {'+': add, '-': sub, '*': mul, '/': div}
    return calculators[op]

if __name__ == '__main__':
    numa = float(input('请输入第一个数字：'))
    numb = float(input('请输入第二个数字：'))
    operator = input('请输入运算符号：')
    cal = get_calculator(operator)  # 根据参数获取函数引用
    result = cal()  # 执行函数获取运算结果
    print(f'{numa} {operator} {numb} = {result}')
