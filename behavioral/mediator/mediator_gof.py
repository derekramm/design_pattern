#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""mediator_gof.py"""
from abc import abstractmethod

class Mediator:
    @abstractmethod
    def send(self, message, colleague): pass
class MediatorA(Mediator):
    def __init__(self):
        self.ca = None
        self.cb = None
    def send(self, message, colleague):
        if colleague is self.ca: self.cb.receive(message)
        else: self.ca.receive(message)
class Colleague:
    def __init__(self, mediator): self.mediator = mediator
    @abstractmethod
    def send(self, message): pass
    @abstractmethod
    def receive(self, message): pass
class ColleagueA(Colleague):
    def send(self, message): self.mediator.send(message, self)
    def receive(self, message): print(self, message)
class ColleagueB(Colleague):
    def send(self, message): self.mediator.send(message, self)
    def receive(self, message): print(self, message)
if __name__ == '__main__':
    ma = MediatorA()
    ca = ColleagueA(ma)
    cb = ColleagueB(ma)
    ma.ca = ca
    ma.cb = cb
    ca.send(ca)
    cb.send(cb)
