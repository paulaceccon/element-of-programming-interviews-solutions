def Coun1Bits_On(x):
    """
    Count the number of bits that are set to 1 in O(n).
    """
    print("Counting number of 1 bits in", x)
    result = 0
    while x:
        result += x & 1
        x >>= 1
    return result


def Parity_On(x):
    """
    Count the parity in O(n).
    """
    print("Couting the parity of", x)
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
    print("Couting the parity of", x)
    result = 0
    while x:
        result ^= 1
        x &= (x - 1)
    return result


def SwapBits_O1(x, i, j):
    """
    Swap bits in O(1)
    """
    print("Swapping the", i, "and", j, "bits of", x)
    if ((x >> i) & 1) != ((x >> j) & 1):
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


def ClosestIntSameBitCount_On(x, kNumUnsignBits=64):
    """
    Find the closest int with the same number of bits on in O(n).
    """
    print("Finding the closest number of", x, "with the same number of bits on")
    for i in range(0, kNumUnsignBits-1):
        if ((x >> 1) & 1) != ((x >> i+1) & 1):
            bit_mask = (1 << i) | (1 << i+1)
            return x ^ bit_mask
    print("All bits are 0s or 1s")
 

def Add_On(a, b):
    """
    Add a and b without arithmetical operators, in O(n).
    """
    print("Adding", a, "and", b, "without arithmetical operators")
    sum_ = 0
    carryin = 0
    k = 1
    temp_a = a
    temp_b = b
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
    print("Multiplying", x, "and", y,"without arithmetical operators")
    sum_ = 0
    while x:
        if (x & 1):
            sum_ = Add_On(sum_, y)
        x >>= 1
        y <<= 1
    return sum_


def Divide_On(x, y):
    """
    Divide x by y using only the addition, subtraction 
    and shifting operators, in O(n)
    """
    print("Dividing", x, "and", y, "using only the addition, subtraction and shifting operators")
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


def Power_On(x, y):
    """
    Compute x to the power of y in O(n)
    """
    print("Computing", x, "to the power of", y)
    result = 1.0
    power = y
    if y < 0:
        power = -power
        x = 1.0 / x
    while power:
        if (power & 1):
            result *= x
        x *= x
        power >>= 1
    return result


if __name__ == '__main__':
    print(Coun1Bits_On(9))
    print(Parity_Ok(9))
    print(SwapBits_O1(73, 1, 6))
    print(ClosestIntSameBitCount_On(8, 4))
    print(Multiply_On2(2, 5))
    print(Divide_On(5, 2))
    print(Power_On(2, 3))
    print(Power_On(2, 4))
    print(Power_On(2, -2))