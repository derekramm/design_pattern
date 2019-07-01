#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_strategy.py"""

class Context(object):
    def __init__(self):
        self.strategy = None
    def execute(self):
        return self, self.strategy.show()

class Strategy(object):
    def show(self): pass

class StrategyA(Strategy):
    def show(self): return 'StrategyA show()'

class StrategyB(Strategy):
    def show(self): return 'StrategyB show()'

if __name__ == '__main__':
    ctx = Context()
    ctx.strategy = StrategyA()
    print(ctx.execute())
    ctx.strategy = StrategyB()
    print(ctx.execute())