import numpy
import math


# BUBBLESORT
def bubblesort(array: list[int]) -> None:
    for i in range(len(array), 0, -1):
        for j in range(0, i-1, 1):
            if array[j+1] < array[j]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp


# QUICKSORT
def qs(array: list[int], low: int, high: int) -> None:
    if low >= high:
        return

    pivot_idx = partition(array, low, high)
    qs(array, low, pivot_idx - 1)
    qs(array, pivot_idx + 1, high)


def partition(array: list[int], low: int, high: int) -> int:
    pivot = array[math.floor(high / 2)]

    array[math.floor(high / 2)] = array[high]
    array[high] = pivot

    idx = low - 1

    for i in range(low, high):
        if array[i] <= pivot:
            idx += 1
            tmp = array[i]
            array[i] = array[idx]
            array[idx] = tmp
    idx += 1
    array[high] = array[idx]
    array[idx] = pivot

    return idx


def quicksort(array: list[int]) -> None:
    qs(array, 0, len(array)-1)


# MERGE SORT
def merge_sort():
    pass


# COMB SORT
def comb_sort():
    pass


array = numpy.random.randint(0, 100, 20)
print(f"Before sort: {array}")
quicksort(array)
print(f"After sort:  {array}")
