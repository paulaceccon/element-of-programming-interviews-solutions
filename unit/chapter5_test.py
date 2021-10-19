import unittest

from chapter5 import *


class Chapter5Test(unittest.TestCase):
    def test_count_bits_on(self):
        output = count_bits_on(9)
        self.assertEqual(output, 2)

    def test_parity_on(self):
        output = parity_on(9)
        self.assertEqual(output, 0)

    def test_parity_ok(self):
        output = parity_ok(9)
        self.assertEqual(output, 0)

    def test_swap_bits_o1(self):
        output = swap_bits_o1(73, 1, 6)
        self.assertEqual(output, 11)

    def test_closest_int_same_bit_count_on(self):
        output = closest_int_same_bit_count_on(8)
        self.assertEqual(output, 4)

    def test_add_on(self):
        # TODO: check this method
        # output = add_on(30, 10)
        # self.assertEqual(output, 40)
        pass

    def test_multiply_on2(self):
        output = multiply_on2(2, 5)
        self.assertEqual(output, 10)

    def test_divide_on(self):
        output = divide_on(5, 2)
        self.assertEqual(output, 2)

        output = divide_on(6, 2)
        self.assertEqual(output, 3)

    def test_power_on(self):
        output = power_on(2, 3)
        self.assertEqual(output, 8)

        output = power_on(2, -2)
        self.assertEqual(output, 0.25)
