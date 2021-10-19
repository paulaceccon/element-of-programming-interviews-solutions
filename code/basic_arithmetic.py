from typing import List


def int_to_list(number: int) -> List[int]:
    """
    Converts an integer number to a list of ints.

    Args:
        number: number to be converted to list.
    Returns:
        List of ints representing @number.
    """
    return list(map(int, str(number)))


def signal(number: int) -> int:
    """
    Obtains the signal of a number.

    Args:
        number: number we wanna know if positive, negative or no signed.

    Returns:
        -1 for negative, 1 for positive, 0 if @number is 0.
    """
    return number and (-1 if number < 0 else 1)


def extend_list(list_of_ints: List[int], desired_len: int) -> List[int]:
    """
    Extends a given list, inserting 0 in the beginning of it.

    Args:
        list_of_ints: list we want to extend.
        desired_len: desirable length.

    Returns:
        New list, with required size.
    """
    list_len = len(list_of_ints)

    if desired_len <= list_len:
        return list_of_ints

    return [0] * (desired_len - list_len) + list_of_ints


def add(number_a: int, number_b: int) -> int:
    """
    Adds two numbers.

    Args:
        number_a: first number.
        number_b: second number.

    Returns:
        Sum of @number_a + @number_b.
    """
    if signal(number_a) != signal(number_b):
        if signal(number_a) == -1:
            return subtract(number_b, abs(number_a))
        else:
            return subtract(number_a, abs(number_b))

    number_a_list = int_to_list(number_a)
    number_b_list = int_to_list(number_b)

    list_size = max(len(number_a_list), len(number_b_list))
    number_a_list = extend_list(number_a_list, list_size)
    number_b_list = extend_list(number_b_list, list_size)

    addition = [0] * list_size
    carry_on = 0
    for i in reversed(range(len(addition))):
        addition[i] = (carry_on + number_a_list[i] + number_b_list[i]) % 10
        carry_on = (carry_on + number_a_list[i] + number_b_list[i]) / 10

    return int("".join([str(n) for n in addition]))


def subtract(number_a: int, number_b: int) -> int:
    pass
