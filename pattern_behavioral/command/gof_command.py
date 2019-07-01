#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_command.py"""

class Receiver(object):
    """处理类"""
    def show_a(self): print(f'{self.__class__.__name__} show_a()')
    def show_b(self): print(f'{self.__class__.__name__} show_b()')
class Command(object):
    def __init__(self): self.receiver = Receiver()
    def show(self): pass
class CommandA(Command):
    def show(self): self.receiver.show_a()
class CommandB(Command):
    def show(self): self.receiver.show_b()
class Invoker(object):
    def __init__(self): self.commands = []
    def add(self, c): self.commands.append(c)
    def remove(self, c): self.commands.remove(c)
    def notify(self):
        for c in self.commands: c.show()

if __name__ == '__main__':
    invoker = Invoker()
    invoker.add(CommandA())
    invoker.add(CommandB())
    invoker.notify()