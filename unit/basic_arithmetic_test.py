import unittest
from code.basic_arithmetic import *


class BasicArithmeticTest(unittest.TestCase):
    def test_int_to_list(self):
        number = 123456
        output = int_to_list(number)
        self.assertEqual(output, [1, 2, 3, 4, 5, 6])

    def test_signal(self):
        number = -123456
        output = signal(number)
        self.assertEqual(output, -1)

        number = 0
        output = signal(number)
        self.assertEqual(output, 0)

        number = 123456
        output = signal(number)
        self.assertEqual(output, 1)

    def test_extend_list(self):
        my_list = [1, 2, 3]
        output = extend_list(my_list, 5)
        self.assertEqual(output, [0, 0, 1, 2, 3])

        output = extend_list(my_list, 2)
        self.assertEqual(output, [1, 2, 3])
