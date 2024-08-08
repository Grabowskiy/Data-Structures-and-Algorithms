from Trees import BinaryNode
from _Queue import Queue


def bfs(root: BinaryNode, needle: int) -> bool:
    q = Queue()
    q.enqueu(root)

    while q.length:
        curr = q.deque()

        if curr.value == needle:
            return True

        if curr.left:
            q.enqueu(curr.left)
        if curr.right:
            q.enqueu(curr.right)

    return False


if __name__ == "__main__":
    tree = BinaryNode(0,
                      BinaryNode(1,
                                 BinaryNode(3),
                                 BinaryNode(4)),
                      BinaryNode(2,
                                 BinaryNode(5),
                                 BinaryNode(6))
                      )

    number = 5
    print(f"Is there {number} in the tree? {"Yes" if bfs(tree, number) else "No"}")

