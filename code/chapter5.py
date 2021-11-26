from typing import Optional


def count_bits_on(x: int) -> int:
    """
    Counts the number of bits that are set to 1 in O(n).
    """
    print("Counting number of 1 bits in", x)
    result = 0
    while x:
        result += x & 1
        x >>= 1
    return result


def parity_on(x: int) -> int:
    """
    Counts the parity in O(n).
    """
    print("Counting the parity of", x)
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


def parity_ok(x: int) -> int:
    """
    Obtains the parity in O(k), where k is
    the number of bits set to 1.
    """
    print("Counting the parity of", x)
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


def swap_bits_o1(x: int, i: int, j: int) -> int:
    """
    Swaps bits in O(1)
    """
    print("Swapping the", i, "and", j, "bits of", x)
    if ((x >> i) & 1) != ((x >> j) & 1):
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


def closest_int_same_bit_count_on(x: int, k_num_unsign_bits: Optional[int] = 64):
    """
    Finds the closest int with the same number of bits on in O(n).
    """
    print("Finding the closest number of", x, "with the same number of bits on")
    for i in range(0, k_num_unsign_bits - 1):
        if ((x >> 1) & 1) != ((x >> i + 1) & 1):
            bit_mask = (1 << i) | (1 << i + 1)
            return x ^ bit_mask
    print("All bits are 0s or 1s")


def add_on(a: int, b: int) -> int:
    """
    Adds @a and @b without arithmetical operators, in O(n).
    """
    print("Adding", a, "and", b, "without arithmetical operators")
    running_sum = 0
    carryin = 0
    k = 1
    temp_a = a
    temp_b = b
    while temp_a or temp_b:
        ak = a & k
        bk = b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        running_sum |= ak ^ bk ^ carryin
        carryin = carryout << 1
        k = k << 1
        temp_a = temp_a >> 1
        temp_b = temp_b >> 1
    return running_sum | carryin


def multiply_on2(x: int, y: int) -> int:
    """
    Multiplies @x and @y without arithmetical operators in O(n2).
    """
    print("Multiplying", x, "and", y, "without arithmetical operators")
    sum_ = 0
    while x:
        if x & 1:
            sum_ = add_on(sum_, y)
        x >>= 1
        y <<= 1
    return sum_


def divide_on(x: int, y: int):
    """
    Divides @x by @y using only the addition, subtraction
    and shifting operators, in O(n)
    """
    print(
        "Dividing",
        x,
        "and",
        y,
        "using only the addition, subtraction and shifting operators",
    )
    result = 0
    power = 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
        result += 1 << power
        x -= y_power
    return result


def power_on(x: int, y: int):
    """
    Computes @x to the power of @y in O(n)
    """
    print("Computing", x, "to the power of", y)
    result = 1.0
    power = y
    if y < 0:
        power = -power
        x = 1.0 / x
    while power:
        if power & 1:
            result *= x
        x *= x
        power >>= 1
    return result
