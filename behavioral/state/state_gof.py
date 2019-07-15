#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""state_gof.py"""
from abc import abstractmethod

class Context:
    def __init__(self, data, state):
        self.data = data
        self.state = state
    def request(self):
        self.state.handle(self)
class State:
    @abstractmethod
    def handle(self, context): pass
class StateA(State):
    def handle(self, context):
        if isinstance(context.data, bool):
            print(self, context.data)
        else:
            context.state = StateB()
            context.request()
class StateB(State):
    def handle(self, context):
        if isinstance(context.data, (int, float, complex)):
            print(self, context.data)
        else:
            context.state = StateC()
            context.request()
class StateC(State):
    def handle(self, context): print(self, context.data)
if __name__ == '__main__':
    Context(True, StateA()).request()
    Context(18, StateA()).request()
    Context('abc', StateA()).request()
