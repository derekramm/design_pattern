#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""prototype_01_gof.py
GOD版本原型模式
通过已经创建好的对象为原型，使用克隆的方法在内存开辟新的对象实例"""

from copy import copy, deepcopy

class Prototype(object):
    """原型类"""
    def __init__(self, val_arg, ref_arg):
        self.val_arg = val_arg  # 值类型的参数
        self.ref_arg = ref_arg  # 引用类型的参数（通常是列表、字典等）
    def clone(self):
        """
        浅表复制，只赋值对象的引用地址
        :return: 新的对象副本
        """
        return copy(self)
    def deep_clone(self):
        """
        深表复制，原有对象中如果有地址指向新的空间，连同指向的空间内容一同赋值出新的副本
        :return: 新的对象副本
        """
        return deepcopy(self)

if __name__ == '__main__':
    # 通过浅表复制克隆新的副本
    p = Prototype('小铭', ['唱歌', '吃好吃的', '睡觉觉'])
    p1 = p.clone()
    print(p, p1)  # 显示的地址是不同的
    p.val_arg = '米沙'  # 修改最初始的对象的属性
    print(p.__dict__, p1.__dict__)  # 克隆出来的对象的属性不会发生变化
    p.ref_arg[2] = '好好学习'
    print(p.__dict__, p1.__dict__)  # 克隆出来的对象会一起变化，因为地址指向同一个空间

    # 通过深表复制克隆新的副本
    p = Prototype('小铭', ['唱歌', '吃好吃的', '睡觉觉'])
    p2 = p.deep_clone()
    print(p, p2)  # 显示的地址是不同的
    p.val_arg = '米沙'  # 修改最初始的对象的属性
    print(p.__dict__, p2.__dict__)  # 克隆出来的对象的属性不会发生变化
    p.ref_arg[2] = '好好学习'
    print(p.__dict__, p2.__dict__)  # 克隆出来的对象也不会发生变化，因为地址指向的空间也克隆出一个新的副本