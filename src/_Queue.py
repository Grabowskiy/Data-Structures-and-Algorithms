import math


class QNode:
    value = None
    next = None

    def __init__(self, item=None):
        self.value = item


class Queue:
    length = 0
    head = QNode()
    tail = QNode()

    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def enqueu(self, item):
        node = QNode(item)
        self.length += 1
        if self.length == 1:
            self.tail = self.head = node
            return

        self.tail.next = node
        self.tail = node

    def deque(self) -> QNode.value or None:
        if not self.head:
            return None

        self.length -= 1

        head = self.head
        self.head = self.head.next

        head.next = None

        return head.value

    def peek(self) -> QNode.value or None:
        if self.head.value:
            return self.head.value


class PriorityQue:
    def _parent(self, idx: int) -> int:
        return math.floor((idx - 1) / 2)

    def _left(self, idx: int) -> int:
        return 2 * idx + 1

    def _right(self, idx: int) -> int:
        return 2 * idx + 2


class MinHeap(PriorityQue):
    def __init__(self):
        self.data = []
        self.length = 0

    def __heapify_down(self, idx: int) -> None:
        lidx = self._left(idx)
        ridx = self._right(idx)
        if idx >= self.length or lidx >= self.length:
            return

        # If left child is the smallest
        if self.data[lidx] < self.data[ridx] and self.data[idx] > self.data[lidx]:
            tmp = self.data[idx]
            self.data[idx] = self.data[lidx]
            self.data[lidx] = tmp

            self.__heapify_down(lidx)
        # If right child is the smallest
        elif self.data[lidx] > self.data[ridx] and self.data[idx] > self.data[ridx]:
            tmp = self.data[idx]
            self.data[idx] = self.data[ridx]
            self.data[ridx] = tmp

            self.__heapify_down(ridx)

    def __heapify_up(self, idx: int) -> None:
        if idx == 0:
            return

        parent = self._parent(idx)
        if self.data[parent] > self.data[idx]:
            tmp = self.data[idx]
            self.data[idx] = self.data[parent]
            self.data[parent] = tmp

            self.__heapify_up(parent)

        return

    def insert(self, item: int) -> None:
        self.data.append(item)
        self.__heapify_up(self.length)
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return None

        out = self.data[0]
        if self.length == 1:
            self.data = []
            self.length = 0
            return out

        self.length -= 1
        self.data[0] = self.data[self.length]
        self.__heapify_down(0)
        self.data.pop()

        return out


class MaxHeap(PriorityQue):
    def __init__(self):
        self.length = 0

    def heapify_down(self):
        pass

    def heapify_up(self):
        pass


def minheap_tests():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(69)
    heap.insert(420)
    heap.insert(4)
    heap.insert(1)
    heap.insert(8)
    heap.insert(7)

    assert heap.length == 8, f"Got: {heap.length}"
    assert heap.pop() == 1, f"Got: {heap.pop()}"
    assert heap.pop() == 3, f"Got: {heap.pop()}"
    assert heap.pop() == 4, f"Got: {heap.pop()}"
    assert heap.pop() == 5, f"Got: {heap.pop()}"
    assert heap.length == 4, f"Got: {heap.length}"
    assert heap.pop() == 7, f"Got: {heap.pop()}"
    assert heap.pop() == 8, f"Got: {heap.pop()}"
    assert heap.pop() == 69, f"Got: {heap.pop()}"
    assert heap.pop() == 420, f"Got: {heap.pop()}"
    assert heap.length == 0, f"Got: {heap.length}"

    print("All tests passed!")


if __name__ == "__main__":
    print(" -- Test MinHeap ---")
    minheap_tests()
