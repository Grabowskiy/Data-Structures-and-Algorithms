class Node:
    value = None
    prev = None

    def __init__(self, item: any):
        self.value = item


class Stack:
    length = 0
    head = None

    def __init__(self):
        self.head = None
        self.length = 0

    def push_back(self, item: any) -> None:
        node = Node(item)

        self.length += 1
        if not self.head:
            self.head = node
            return None

        node.prev = self.head
        self.head = node

    def pop(self) -> any or None:
        self.length = max(0, self.length - 1)
        if self.length == 0:
            head = self.head
            self.head = None
            return head.value

        head_popped = self.head
        self.head = self.head.prev

        return head_popped.value

    def peek(self) -> Node.value or None:
        if self.head.value:
            return self.head.value
        return None
