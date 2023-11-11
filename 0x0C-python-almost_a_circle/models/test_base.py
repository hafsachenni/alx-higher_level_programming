#!/usr/bin/python3
import unittest

import os

class base_test(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
