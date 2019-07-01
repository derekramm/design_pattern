#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_observer.py"""

class Subject(object):
    def __init__(self): self.observers = []
    def add(self, o): self.observers.append(o)
    def remove(self, o): self.observers.remove(o)
    def notify(self):
        for o in self.observers: o.update()
class ConcreteSubject(Subject): pass
class Observer(object):
    def update(self): pass
class ObserverA(Observer):
    def __init__(self, s):
        self.concrete_subject = s
        self.concrete_subject.add(self)
    def update(self): print(f'{self.__class__.__name__} update {self.concrete_subject.__class__.__name__}')
class ObserverB(Observer):
    def __init__(self, s):
        self.concrete_subject = s
        self.concrete_subject.add(self)
    def update(self): print(f'{self.__class__.__name__} update {self.concrete_subject.__class__.__name__}')

if __name__ == '__main__':
    cs = ConcreteSubject()
    oa, ob = ObserverA(cs), ObserverB(cs)
    cs.notify()