#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""factory_method_git.py"""

class GreekGetter(object):
    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")
    def get(self, msgid): return self.trans.get(msgid, str(msgid))

class ChineseGetter(object):
    def __init__(self): self.trans = dict(dog="小狗", cat="小猫")
    def get(self, msgid): return self.trans.get(msgid, str(msgid))

class EnglishGetter(object):
    @staticmethod
    def get(msgid): return str(msgid)

def get_localizer(language='English'):
    languages = dict(English=EnglishGetter, Greek=GreekGetter, Chinese=ChineseGetter)
    return languages[language]()

if __name__ == '__main__':
    e = get_localizer(language='English')
    g = get_localizer(language='Greek')
    c = get_localizer(language='Chinese')
    for mid in 'dog parrot cat bear'.split():
        print(e.get(mid), g.get(mid), c.get(mid))
