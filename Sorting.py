import numpy


def bubblesort(array: list[int]) -> None:
    for i in range(len(array), 0, -1):
        for j in range(0, i-1, 1):
            if array[j+1] < array[j]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp




array = numpy.random.randint(0, 100, 20)
print(f"Before sort: {array}")
bubblesort(array)
print(f"After sort: {array}")