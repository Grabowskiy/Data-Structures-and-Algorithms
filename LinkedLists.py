class Node:

    def __init__(self, item=None):
        self.value = item
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head = self.tail = None

    def __getitem__(self, index: int) -> Node or None:
        if index > self.length or index < 0:
            raise IndexError("index is out of bounds")
        node = self.__get_at(index)
        return node.value if node is not None else None

    def prepend(self, item: any) -> None:
        new_node = Node(item)
        self.length += 1

        if not self.head:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, item: any) -> None:
        new_node = Node(item)
        self.length += 1

        if not self.tail:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, item: any) -> any or None:
        curr = self.head
        while curr:
            if curr.value == item:
                break
            curr = curr.next

        if not curr:
            return None

        return self.__remove_node(curr)

    def insert_at(self, item: any, index: int) -> None:
        if index > self.length or index < 0:
            raise IndexError("index is out of bounds")
        elif index == self.length:
            self.append(item)
        elif index == 0:
            self.prepend(item)
        else:
            curr = self.__get_at(index)

            self.length += 1
            new_node = Node(item)

            new_node.prev = curr.prev
            new_node.next = curr
            curr.prev = new_node
            if new_node.prev:
                new_node.prev.next = new_node
                curr.prev = new_node

    def remove_at(self, index: int) -> any or None:
        node = self.__get_at(index)

        if not node:
            return None

        return self.__remove_node(node)

    def __remove_node(self, node: Node) -> any or None:
        self.length -= 1

        if self.length == 0:
            out = self.head.value
            self.head = self.tail = None
            return out

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        node.prev = node.next = None

        return node.value

    def __get_at(self, index: int) -> Node or None:
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def print_out_all_values(self) -> None:
        node = self.head
        for i in range(self.length):
            print(node.value, end=' ')
            node = node.next
