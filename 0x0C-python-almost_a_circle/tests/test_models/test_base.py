#!/usr/bin/python3
'''
unittest for base class
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Testbase(unittest.TestCase):
    '''
    tests for base class
    '''
    def test_id(self):
        '''testing with no id'''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 6)
        self.assertEqual(b2.id, 7)
        self.assertEqual(b3.id, 8)
        self.assertEqual(b4.id, 9)


    def test_given_id(self):
        '''test with given id'''
        b = Base(36)
        self.assertEqual(b.id, 36)

    def test_str(self):
        '''test str'''
        o = "hello"
        b = Base(o)
        self.assertEqual(b.id, o)

    def test_negative(self):
        '''test negative id'''
        b = Base(-9)
        self.assertEqual(b.id, -9)


    def test_2args(self):
        '''test 2args'''
        with self.assertRaises(TypeError):
             b = Base(6, 5)

    def testfloat(self):
        '''test float id'''
        self.assertEqual(Base(6.4).id, 6.4)


    def test0args(self):
        '''test0args'''
        r1 = Base(None)
        r2 = Base()
        r3 = Base()
        r4 = Base(None)
        r5 = Base()
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r1.id, r5.id - 4)
       

if __name__ == '__main__':
    unittest.main()
