#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""interpreter_gof.py"""
from abc import abstractmethod

class Interpreter:
    @abstractmethod
    def interpret(self, context): pass
class InterpreterA(Interpreter):
    def __str__(self): return self.__class__.__name__
    def interpret(self, context): return str(context)
class InterpreterB(Interpreter):
    def interpret(self, context): return eval(context)
if __name__ == '__main__':
    ita = InterpreterA()
    itb = InterpreterB()
    print(ita.interpret(ita))
    print(itb.interpret('InterpreterB()'))
