"""
Filling an array from the front is slow, so see if it's possible to write values from the back
Instead of deleting an entry (which requires moving all entries to its left), consider overwriting it.

"""

from typing import List


def split_in_even_odd(arr: List) -> List:
    """
    Splits an array in even|odd parts.
    Time complexity: O(n)

    Idea:
        Two 'pointers', one pointing to the start list, other to the end.
        One is going to look for the next even, the other for the next odd.
        If even check passes, increment even pointer. Otherwise, swap, and decrement odd pointer.
    """
    next_even = 0
    next_odd = len(arr)-1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd]=arr[next_odd], arr[next_even]
            next_odd -= 1

    # while next_even < next_odd:
    #     even = arr[next_even] % 2 == 0
    #     odd = arr[next_odd] % 2 != 0
    #     if even:
    #         next_even += 1
    #     if odd:
    #         next_odd -= 1
    #     if not (even or odd):
    #         aux = arr[next_even]
    #         arr[next_even] = arr[next_odd]
    #         arr[next_odd] = aux

    return arr


def dutch_flag_partition_v1(arr: List, pivot_index: int) -> List:
    """
    Partitions an array based on value at @pivot_index, pivot value, so the array is divided in two parts:
    smaller than pivot value, equal to pivot value, bigger than pivot value.
    Time complexity: O(n2)
    Space complexity: O(1)

    Idea:
        Iterate over the array twice, with nested loops.
        Firstly, looking for smaller values and putting than at the beginning of @arr.
        Secondly, looking for larger values and putting than at the end of @arr.
    """
    pivot_value = arr[pivot_index]

    # Group elements smaller than pivot
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):

            if arr[j] < pivot_value:
                arr[j], arr[i] = arr[i], arr[j]

                break


    # Group elements larger than pivot
    for i in reversed(range(len(arr))):
        for j in reversed(range(i)):
            if arr[j] > pivot_value:
                arr[j], arr[i] = arr[i], arr[j]

                break


    return arr

def dutch_flag_partition_v2(arr: List, pivot_index: int) -> List:
    """
    Partitions an array based on value at @pivot_index, pivot value, so the array is divided in two parts:
    smaller than pivot value, equal to pivot value, bigger than pivot value.
    Time complexity: O(n)
    Space complexity: O(1)

    Idea:
        Iterate over the array twice, avoiding nested loops. For that, we'll store the
        last swap index.
        Firstly, looking for smaller values and putting than at the beginning of @arr.
        Secondly, looking for larger values and putting than at the end of @arr.
    """
    pivot_value = arr[pivot_index]

    smaller = 0
    for i in range(1, len(arr)):
        if arr[i] < pivot_value:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1

    larger = len(arr)-1
    for i in reversed(range(len(arr))):
        if arr[i] > pivot_value:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1

    return arr

