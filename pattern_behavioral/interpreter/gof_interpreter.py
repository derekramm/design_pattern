#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_interpreter.py"""

class Variables(object):
    def __init__(self): self.variables = {}
    def put(self, variable, value): self.variables[variable] = value
    def get(self, variable): return self.variables[variable]

class Expression(object):
    def interpret(self, variables): pass

class VariableExpression(Expression):
    def __init__(self, value): self.variable = value

    def interpret(self, variables):
        return variables.get(self.variable)

class PlusExpression(Expression):
    def __init__(self, left, right): self.left, self.right = left, right

    def interpret(self, variables): return self.left.interpret(variables) + self.right.interpret(variables)

class SubExpression(Expression):
    def __init__(self, left, right): self.left, self.right = left, right

    def interpret(self, variables):
        return self.left.interpret(variables) - self.right.interpret(variables)

class MulExpression(Expression):
    def __init__(self, left, right): self.left, self.right = left, right

    def interpret(self, variables):
        return self.left.interpret(variables) * self.right.interpret(variables)

class DivExpression(Expression):
    def __init__(self, left, right): self.left, self.right = left, right

    def interpret(self, variables):
        return self.left.interpret(variables) / self.right.interpret(variables)

if __name__ == '__main__':
    variables = Variables()
    variables.put('a',1)
    variables.put('b',2)
    variables.put('c',3)
    variables.put('d',4)

    a = VariableExpression('a')
    b = VariableExpression('b')
    c = VariableExpression('c')
    d = VariableExpression('d')

    print(PlusExpression(a, b).interpret(variables))
