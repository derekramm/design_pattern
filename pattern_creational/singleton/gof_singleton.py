#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""gof_singleton.py"""

import threading

class Singleton(object):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._lock.acquire()
            if not cls._instance:
                cls._instance = super().__new__(cls)
            cls._lock.release()
        return cls._instance

if __name__ == '__main__':
    s1, s2 = Singleton(), Singleton()
    print(s1, s2)