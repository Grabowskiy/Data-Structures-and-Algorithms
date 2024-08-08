class BinaryNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __search(self, item:int, node: BinaryNode) -> bool:
        if not node:
            return False

        if node.value == item:
            return True

        if item < node.value:
            return self.__search(item, node.left)
        return self.__search(item, node.right)

    # O(log_n) - O(n) -> O(height_of_tree)
    def find(self, item: int, node: BinaryNode) -> bool:
        return self.__search(item, node)

    def insert(self, item: int, node: BinaryNode) -> bool:
        if not node:
            return BinaryNode(item)
        if item <= node.value:
            node.left = self.insert(item, node.left)
        if item > node.value:
            node.right = self.insert(item, node.right)

        return node


def bst_test():
    bst_tree = BinaryNode(7,
                          BinaryNode(5,
                                     BinaryNode(3,
                                                BinaryNode(2), BinaryNode(7))),
                          BinaryNode(15,
                                     BinaryNode(9,
                                                BinaryNode(8)),
                                     BinaryNode(16))
                          )

    bst = BST()
    number = 9
    print(f"Is there {number} in the binary search tree? {'Yes' if bst.find(number, bst_tree) else 'No'}")

    number = 46
    print(f"Is there {number} in the binary search tree? {'Yes' if bst.find(number, bst_tree) else 'No'}")
    print(f"Add number {number}.")
    bst_tree = bst.insert(number, bst_tree)
    print(f"Is there {number} in the binary search tree? {'Yes' if bst.find(number, bst_tree) else 'No'}")


# Trie implementation in the future
'''
class TrieNode:
    def __init__(self, char: str, is_word=False):
        self.is_word = is_word
        self.c = char
        # Because we only have 26 letters, using list instead of a set is faster regarding lookup speed
        self.chars = []
        self.next = None
        self.prev = None

    def add_char(self, char: str):
        self.chars.add(char)


# Retrieval tree / Try tree
def Trie():
    def add(self, word: list[str]):
        pass
'''


if __name__ == "__main__":
    # BST test
    bst_test()
