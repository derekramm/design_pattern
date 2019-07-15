#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""observer_gof.py"""
from abc import abstractmethod

class Subject:
    def __init__(self):
        self.observers = []
    def add(self, o): self.observers.append(o)
    def remove(self, o): self.observers.remove(o)
    @abstractmethod
    def notify(self): pass
class SubjectA(Subject):
    def notify(self):
        for o in self.observers:
            o.update()
class Observer:
    def __init__(self, subject):
        self.subject = subject
        self.subject.add(self)
    @abstractmethod
    def update(self): pass
class ObserverA(Observer):
    def update(self): print(self, self.subject)
class ObserverB(Observer):
    def update(self): print(self, self.subject)
if __name__ == '__main__':
    sa = SubjectA()
    oa = ObserverA(sa)
    ob = ObserverB(sa)
    sa.notify()
