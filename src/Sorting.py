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


# INSERTION SORT
def insertion_sort(array: list[int]) -> None:
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                tmp = array[j]
                array[j] = array[j-1]
                array[j-1] = tmp


# COMB SORT
def comb_sort(array: list[int]) -> None:
    gap = len(array)
    while gap > 0:
        i = 0
        while gap < len(array):
            if array[i] > array[gap]:
                tmp = array[gap]
                array[gap] = array[i]
                array[i] = tmp
            i += 1
            gap += 1
        gap -= i
        gap = math.floor(gap / 1.3)


# MERGE SORT
def merge(arr: list[int], left: list[int], right: list[int]) -> None:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result.extend(left[i:])
    else:
        result.extend(right[j:])

    arr[:] = result


def merge_sort(array: list[int]) -> None:
    if len(array) <= 1:
        return None

    midpoint = math.floor(len(array) / 2)

    l = array[:midpoint]
    r = array[midpoint:]

    merge_sort(l)
    merge_sort(r)

    merge(array, l, r)


array = numpy.random.randint(-50, 100, 15)
print(f"Before sort: {array}")
merge_sort(array)
print(f"After sort:  {array}")
