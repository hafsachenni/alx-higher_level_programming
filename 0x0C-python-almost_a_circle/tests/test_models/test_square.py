#!/usr/bin/python3
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class Testsquare(unittest.TestCase):
    def test_ini(self):
        s1 = Square(8)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.height, 8)
        self.assertEqual(s1.width, 8)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.x, 0)


    def test_str(self):
        s1 = Square(5, 6, 4, 8)
        self.assertEqual(str(s1), "[Square] (8) 6/4 - 5")


    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)


    def test_size_setter(self):
         s1 = Square(3, 2, 5, 1)
         s1.update(21)
         self.assertEqual(str(s1), "[Square] (21) 2/5 - 3")


    def test_update(self):
        s1 = Square(3, 2, 5, 1)
        s1.update(21, 7)
        self.assertEqual(str(s1), "[Square] (21) 2/5 - 7")
