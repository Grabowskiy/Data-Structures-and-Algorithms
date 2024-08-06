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
