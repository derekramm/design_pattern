#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""memento_gof.py"""
class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
    def save(self): return Memento(self.price, self.count)
    def load(self, memento):
        self.price = memento.price
        self.count = memento.count
class Memento:
    def __init__(self, price, count):
        self.price = price
        self.count = count
class Director:
    def __init__(self, **mementos):
        self.mementos = mementos
    def add(self, key, memento): self.mementos[key] = memento
    def remove(self, key): del self.mementos[key]
    def get(self, key): return self.mementos[key]
if __name__ == '__main__':
    d = Director()
    pa = Product('a', 10, 1)
    pb = Product('b', 20, 2)
    d.add(pa.name, pa.save())
    d.add(pb.name, pb.save())
    pa.price *= 10
    pa.count *= 10
    pb.price *= 10
    pb.count *= 10
    pa.load(d.get(pa.name))
    pb.load(d.get(pb.name))
    print(pa.__dict__)
    print(pb.__dict__)
