#!/usr/bin/python3
import unittest
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




if __name__ == '__main__':
    unittest.main()
