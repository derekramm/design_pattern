#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""gof_mediator.py"""

class Mediator(object):
    def send(self, c, m): pass

class MediatorA(Mediator):
    def __init__(self): self.ca = self.cb = None
    def send(self, c, m): self.cb.receive(m) if c is self.ca else self.ca.receive(m)

class Colleague(object):
    def __init__(self, m): self.mediator = m

class ColleagueA(Colleague):
    def send(self, message): self.mediator.send(self, message)
    def receive(self, message): print(f'{self.__class__.__name__} received {message}')

class ColleagueB(Colleague):
    def send(self, message): self.mediator.send(self, message)
    def receive(self, message): print(f'{self.__class__.__name__} received {message}')

if __name__ == '__main__':
    ma = MediatorA()
    ca, cb = ColleagueA(ma), ColleagueB(ma)
    ma.ca, ma.cb = ca, cb
    ca.send('message from ColleagueA')
    cb.send('message from ColleagueB')