#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""adapter_git.py"""

class Dog(object):
    def __init__(self): self.name = "Dog"
    @staticmethod
    def bark(): return "woof!"

class Cat(object):
    def __init__(self): self.name = "Cat"
    @staticmethod
    def meow(): return "meow!"

class Human(object):
    def __init__(self): self.name = "Human"
    @staticmethod
    def speak(): return "'hello'"

class Car(object):
    def __init__(self): self.name = "Car"
    @staticmethod
    def make_noise(octane_level): return "vroom{0}".format("!" * octane_level)

class Adapter(object):
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)
    def __getattr__(self, attr): return getattr(self.obj, attr)
    def original_dict(self): return self.obj.__dict__

if __name__ == '__main__':
    objects = []
    dog = Dog()
    print(dog.__dict__)
    objects.append(Adapter(dog, make_noise=dog.bark))
    print(objects[0].__dict__['obj'], objects[0].__dict__['make_noise'])
    print(objects[0].original_dict())
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))
    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))
