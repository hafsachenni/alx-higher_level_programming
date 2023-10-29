import unittest
max_integer = __import__('6-max_integer').max_integer

class MyTestCase(unittest.TestCase):
    def no_arg(self):
        self.assertEqual(max_integer(), None)

    def test_max(self):
        self.assertEqual(max_integer([8, 3, 9, 7]), 9)

        
