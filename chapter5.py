def Coun1Bits_On(x):
    """
    Counts the number of bits that are set to 1 in O(n).
    """
    result = 0
    while x:
        result += x & 1
        x >>= 1
    return result


def Parity_On(x):
    """
    Counts the parity in O(n).
    """
    result = 0
    while x:
        result ^= (x & 1)
        x >>= 1
    return result


def Parity_Ok(x):
    """
    Counts the parity in O(k), where k is 
    the number of bits set to 1.
    """
    result = 0
    while x:
        result ^= 1
        x &= (x - 1)
    return result


def SwapBits_O1(x, i, j):
    """
    Swap bits in O(1)
    """
    if ((x >> i) & 1) != ((x >> j) & 1):
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


if __name__ == '__main__':
    print(Coun1Bits_On(9))
    print(Parity_Ok(9))
    print(SwapBits_O1(73, 1, 6))