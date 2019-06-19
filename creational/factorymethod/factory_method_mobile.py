#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""factory_method_mobile.py"""

from enum import Enum, unique

@unique
class Brand(Enum):
    HuaWei = 0
    Apple = 1

class HuaWei(object):
    @staticmethod
    def create_mobile(): return f'华为手机'

class Apple(object):
    @staticmethod
    def create_mobile(): return f'苹果手机'

def get_mobile(brand='HuaWei'):
    return dict(HuaWei=HuaWei, Apple=Apple)[brand]()

if __name__ == '__main__':
    print(get_mobile(Brand.HuaWei.name).create_mobile())
    print(get_mobile(Brand.Apple.name).create_mobile())
