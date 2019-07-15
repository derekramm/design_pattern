#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""command_gof.py"""
from abc import abstractmethod

class Receiver:
    def handle_a(self): print(self.handle_a)
    def handle_b(self): print(self.handle_b)
class Command:
    def __init__(self, receiver): self.receiver = receiver
    @abstractmethod
    def request(self): pass
class CommandA(Command):
    def request(self): self.receiver.handle_a()
class CommandB(Command):
    def request(self): self.receiver.handle_b()
class Invoker:
    def __init__(self):
        self.__commands = []
    def add(self, c): self.__commands.append(c)
    def remove(self, c): self.__commands.remove(c)
    def notify(self):
        for c in self.__commands: c.request()
if __name__ == '__main__':
    r = Receiver()
    ca = CommandA(r)
    cb = CommandB(r)
    ivkr = Invoker()
    ivkr.add(ca)
    ivkr.add(cb)
    ivkr.notify()
