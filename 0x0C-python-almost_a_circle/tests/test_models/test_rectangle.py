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
         self.assertEqual(r2.id, 5)
         self.assertEqual(r1.x, 0)




if __name__ == '__main__':
    unittest.main()
