import unittest
max_integer = __import__('6-max_integer').max_integer

class MyTestCase(unittest.TestCase):
    def test_no_arg(self):
        self.assertEqual(max_integer(), None)

    def test_max(self):
        self.assertEqual(max_integer([8, 3, 9, 7]), 9)
        self.assertEqual(max_integer([56]), 56)

    def test_value(self):
        self.assertRaises(TypeError, max_integer(), [5, "hi", 0])
