#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""singleton_gof.py"""

import threading, time, random

class Singleton(object):
    _lock = threading.Lock()

    def __init__(self):
        time.sleep(random.random())

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = super().__new__(cls)
        return cls._instance

def task(): print(Singleton())

if __name__ == '__main__':
    for _ in range(10):
        threading.Thread(target=task).start()
