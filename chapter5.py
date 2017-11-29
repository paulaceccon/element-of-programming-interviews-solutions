def Coun1Bits_On(x):
    """
    Count the number of bits that are set to 1 in O(n).
    """
    result = 0
    while x:
        result += x & 1
        x >>= 1
    return result


def Parity_On(x):
    """
    Count the parity in O(n).
    """
    result = 0
    while x:
        result ^= (x & 1)
        x >>= 1
    return result


def Parity_Ok(x):
    """
    Obtain the parity in O(k), where k is 
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


def ClosestIntSameBitCount_On(x, kNumUnsignBits=64):
    """
    Find the closest int with the same number of bits on in O(n).
    """
    for i in range(0, kNumUnsignBits-1):
        if ((x >> 1) & 1) != ((x >> i+1) & 1):
            bit_mask = (1 << i) | (1 << i+1)
            return x ^ bit_mask
 

def Add_On(a, b):
    """
    Add a and b without arithmetical operators, in O(n).
    """
    sum_ = 0
    carryin = 0
    k = 1
    temp_a = a
    temp_b = b
    print('------', a, b)
    while (temp_a or temp_b):
        ak = a & k
        bk = b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        print(temp_a, temp_b, ak, bk, sum_)
        sum_ |= (ak ^ bk ^ carryin)
        carryin << carryout << 1
        k <<= 1
        temp_a >>= 1
        temp_b >>= 1
        print(sum_)
    return sum_

def Multiply_On2(x, y):
    """
    Multiply x and y without arithmetical operators in O(n2).
    """
    sum_ = 0
    while x:
        if (x & 1):
            sum_ = Add(sum_, y)
        x >>= 1
        y <<= 1
        print('xxx',sum_)
    return sum_


if __name__ == '__main__':
    print(Coun1Bits_On(9))
    print(Parity_Ok(9))
    print(SwapBits_O1(73, 1, 6))
    print(ClosestIntSameBitCount_On(8, 4))
    print(Multiply_On2(2, 5))