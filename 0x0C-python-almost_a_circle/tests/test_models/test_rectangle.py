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
             r10 = Rectangle(8, 3, 2, "and again")
if __name__ == '__main__':
    unittest.main()
