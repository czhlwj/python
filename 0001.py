#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Ericooou'


import time, functools, sys, random, unittest
from functools import reduce
from enum import Enum, unique

########### START ###########

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if 100 >= self.score >= 0:
            if 79 >= self.score >= 60:
                return 'B'
            elif 100 >= self.score >= 80:
                return 'A'
            else:
                return 'C'
        else:
            raise ValueError("The Score must between 0 and 100!")

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            raise s1.get_grade()
        with self.assertRaises(ValueError):
            raise s2.get_grade()


########### END ###########

# 测试:
if __name__ == '__main__':
    unittest.main()