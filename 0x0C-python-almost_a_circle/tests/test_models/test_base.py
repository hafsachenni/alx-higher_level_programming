#!/usr/bin/python3
import unittest
from models.base import Base

class Testbase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)


    def test_given_id(self):
        b = Base(36)
        self.assertEqual(b.id, 36)

    def test_str(self):
        o = "hello"
        b = Base(o)
        self.assertEqual(b.id, o)

    def test_negative(self):
        b = Base(-9)
        self.assertEqual(b.id, -9)


    def test_2args(self):
        with self.assertRaises(TypeError):
             b = Base(6, 5)

    def testfloat(self):
        self.assertEqual(Base(6.4).id, 6.4)
       

if __name__ == '__main__':
    unittest.main()
