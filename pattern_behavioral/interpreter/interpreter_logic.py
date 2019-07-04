#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""interpreter_logic.py"""

from abc import ABCMeta, abstractmethod

class Expression(object, metaclass=ABCMeta):
    @abstractmethod
    def interpret(self, context): pass

class TerminalExpression(Expression):
    def __init__(self, data): self.data = data

    def interpret(self, context):
        return self.data in context
