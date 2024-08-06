import math


# Only if array is sorted
def my_binary_search(array: list[int], v: int) -> int:
    index = 0
    while len(array) != 1:
        n = len(array)
        compare = array[int(n/2)]
        if compare == v:
            return int(n/2) + index
        elif v < compare:
            array = array[:(int(n/2))]
        else:
            array = array[(int(n / 2)):]
            index += int(n / 2)
    return -1


def binary_search(array: list[int], value: int) -> bool:
    lp = 0
    hp = len(array)

    while lp < hp:
        midp = math.floor(lp + (hp - lp) / 2)
        compare = array[midp]

        if value == compare:
            return True
        elif value > compare:
            lp = midp + 1
        else:
            hp = midp

    return False


def two_crystal_balls(breaks: list[bool]) -> int:
    jump = math.floor(math.sqrt(len(breaks)))
    i = jump

    while i < len(breaks):
        if breaks[i]:
            break
        i += jump
    i -= jump

    j = 0
    while j < jump and i < len(breaks):
        if breaks[i]:
            return i
        j += 1
        i += 1

    return -1
