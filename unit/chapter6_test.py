import unittest
from code.chapter6 import *


class Chapter6Test(unittest.TestCase):
    def test_split_in_even_odd(self):
        output = split_in_even_odd([1, 3, 5, 7, 2, 4, 9, 8])
        self.assertEqual(output, [8, 4, 2, 7, 5, 9, 3, 1])

    def test_dutch_flag_partition_v1(self):
        arr = [2, 0, 0, 2, 2, 1, 1]

        output = dutch_flag_partition_v1(arr.copy(), 1)  # value 0
        self.assertEqual(output, [0, 0, 1, 2, 2, 2, 1])

        output = dutch_flag_partition_v1(arr.copy(), 5)  # value 1
        self.assertEqual(output, [0, 0, 1, 1, 2, 2, 2])

        output = dutch_flag_partition_v1(arr.copy(), 0)  # value 2
        self.assertEqual(output, [0, 0, 1, 1, 2, 2, 2])

    def test_dutch_flag_partition_v2(self):
        arr = [2, 0, 0, 2, 2, 1, 1]

        output = dutch_flag_partition_v2(arr.copy(), 1)  # value 0
        self.assertEqual(output, [0, 0, 2, 2, 2, 1, 1])

        output = dutch_flag_partition_v2(arr.copy(), 5)  # value 1
        self.assertEqual(output, [0, 0, 1, 1, 2, 2, 2])

        output = dutch_flag_partition_v2(arr.copy(), 0)  # value 2
        self.assertEqual(output, [0, 0, 1, 1, 2, 2, 2])
