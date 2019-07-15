#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""singleton_gof.py"""

import time
import random
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if not cls._instance:
            cls._lock.acquire()
            if not cls._instance:
                cls._instance = super().__new__(cls)
            cls._lock.release()
        return cls._instance
def task():
    time.sleep(random.random())
    print(Singleton())
if __name__ == '__main__':
    for _ in range(5):
        threading.Thread(target=task).start()
