#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""simple_factory_calculator.py"""

numa, numb = 12, 3

def add(): return numa + numb
def sub(): return numa - numb
def mul(): return numa * numb
def div(): return numa / numb

def get_cal(operator='+'):
    calculators = {'+': add, '-': sub, '*': mul, '/': div}
    return calculators[operator]()

if __name__ == '__main__':
    numa = int(input('请输入第一个数字：'))
    numb = int(input('请输入第二个数字：'))
    op = input('请输入运算符号：')
    result = get_cal(op)
    print(f'{numa} {op} {numb} = {result}')
