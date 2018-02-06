#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Erichen'


import time, functools, sys, random
from functools import reduce
from enum import Enum, unique

#########START#########

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')




#########END#########
if __name__=='__main__':
    pass