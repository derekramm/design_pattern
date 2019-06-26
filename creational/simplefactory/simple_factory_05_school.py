#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""simple_factory_05_school.py
使用简单工厂实现学生和老师类的创建"""

from abc import ABCMeta, abstractclassmethod, abstractmethod

class Person(object, metaclass=ABCMeta):
    """父类产品：人类"""

    def __init__(self, name):
        """
        初始化函数中可以为姓名赋初始值
        :param name: 姓名
        """
        self.name = name

    def self_introduce(self):
        """
        打招呼的方法
        调用了另一个函数（_get_person_type()），用来获取具体的类型是老师还是学生
        :return:
        """
        return f'我是一名{self._get_person_type()}，我叫{self.name}'

    @abstractmethod
    def _get_person_type(self):
        """
        抽象方法
        :return: 由子类实现，返回老师或学生
        """
        pass

class Teacher(Person):
    """老师类，是Person的子类"""

    def _get_person_type(self):
        """
        实现父类抽象方法
        :return: 返回老师文本
        """
        return f'老师'

class Student(Person):
    """学生类，是Person的子类"""

    def _get_person_type(self):
        """
        实现父类抽象方法
        :return: 返回学生文本
        """
        return f'学生'

class PersonFactory(object):
    """简单工厂，用来根据参数获取Teacher或者Student子类"""

    @staticmethod
    def get_person(person_type='student'):
        """
        根据用户参数返回具体子类
        注意返回的是子类的类型，并不是子类实例化后的对象实例
        :param person_type: 默认值参数，表示需要Teacher还是Student
        :return: Teacher或Student的类型
        """
        persons = dict(teacher=Teacher, student=Student)
        return persons[person_type]

if __name__ == '__main__':
    # 根据参数返回子类类型后，直接实例化，可以通过构造函数给name属性赋初始值
    t = PersonFactory.get_person('teacher')('大蜥蜴')
    s1 = PersonFactory.get_person('student')('小铭')
    s2 = PersonFactory.get_person('student')('米沙')

    # 输出时，调用各个子类对象的方法即可
    print(t.self_introduce())
    print(s1.self_introduce())
    print(s2.self_introduce())

    # 扩展，将创建类型和姓名通过输入实现
    person_type = input('请输入类型（teacher | student）：')
    person_name = input('请输入姓名：')
    p = PersonFactory.get_person(person_type)(person_name)
    print(p.self_introduce())
