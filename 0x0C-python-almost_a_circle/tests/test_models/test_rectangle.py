#!/usr/bin/python3
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestRecatngle(unittest.TestCase):
    def test_id_rec(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_all_arg(self):
        r1 = Rectangle(45, 8, 0, 0, 9)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.width, 45)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 9)

    def test_extra(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 9, 0, 0, 85, 75)

    def testint(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("hi", 4, 5, 8, 9)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2 = Rectangle(4, "better")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(0, 5)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r4 = Rectangle(5, 0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5 = Rectangle(-9, 5)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r6 = Rectangle(5, -9)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r7 = Rectangle(2, 8, -9)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r8 = Rectangle(8, 6, 5, -9)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r9 = Rectangle(8, 9, "hi again", 7)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r10 = Rectangle(8, 3, 2, "and againn")

    def testarea(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def testdisplay(self):
        r1 = Rectangle(3, 4)
        with self.assertRaises(TypeError):
            r1.display(2)

    def test_str(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_1_arg_str(self):
        r1 = Rectangle(4, 6, 2, 1, 18)
        with self.assertRaises(TypeError):
            r1.__str__(4)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        '''testing only with id'''
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

        '''test with id + width'''
        r1.update(89, 9)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 9/10")

        ''' + height'''
        r1.update(89, 9, 8)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 9/8")

        '''testing all atrr'''
        r1.update(89, 9, 8, 4, 5)
        self.assertEqual(r1.__str__(),  "[Rectangle] (89) 4/5 - 9/8")

        '''testing update several amount of times'''
        r1.update(78)
        r1.update(85)
        r1.update(54)
        self.assertEqual(r1.__str__(), "[Rectangle] (54) 4/5 - 9/8")

    def test_update_withkwargs(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=14)
        self.assertEqual(r1.__str__(), "[Rectangle] (14) 10/10 - 10/10")
        '''test with 2kwargs'''
        r1.update(id=14, width=8)
        self.assertEqual(r1.__str__(), "[Rectangle] (14) 10/10 - 8/10")

        '''3kwargs'''
        r1.update(id=14, width=8, height=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (14) 10/10 - 8/4")

        '''4kwags'''
        r1.update(id=14, width=8, height=4, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (14) 2/10 - 8/4")

        '''5kwargs'''
        r1.update(id=14, width=8, height=4, x=2, y=3)
        self.assertEqual(r1.__str__(), "[Rectangle] (14) 2/3 - 8/4")


if __name__ == '__main__':
    unittest.main()
