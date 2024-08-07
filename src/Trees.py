class BinaryNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder_walk(curr: BinaryNode or None, path: list[int]) -> list[int]:
    if not curr:
        return path

    # Recursion
    # pre
    path.append(curr.value)
    # recurse
    preorder_walk(curr.left, path)
    preorder_walk(curr.right, path)
    # post
    return path


def bt_preorder(root: BinaryNode) -> list[int]:
    return preorder_walk(root, [])


def inorder_walk(curr: BinaryNode or None, path: list[int]) -> list[int]:
    if not curr:
        return path

    # Recursion
    # pre
    # recurse
    inorder_walk(curr.left, path)
    path.append(curr.value)
    inorder_walk(curr.right, path)
    # post
    return path


def bt_inorder(root: BinaryNode) -> list[int]:
    return inorder_walk(root, [])

def postorder_walk(curr: BinaryNode or None, path: list[int]) -> list[int]:
    if not curr:
        return path

    # Recursion
    # pre
    # recurse
    postorder_walk(curr.left, path)
    postorder_walk(curr.right, path)
    # post
    path.append(curr.value)

    return path


def bt_postorder(root: BinaryNode) -> list[int]:
    return postorder_walk(root, [])

if __name__ == "__main__":
    tree = BinaryNode(0,
                       BinaryNode(1,
                                  BinaryNode(3),
                                  BinaryNode(4)),
                        BinaryNode(2,
                                   BinaryNode(5),
                                   BinaryNode(6))
    )

    print(" --- PREORDER --- ")
    preorder = bt_preorder(tree)
    for n in preorder:
        print(n, end=' ')

    print("\n\n --- INORDER --- ")
    inorder = bt_inorder(tree)
    for n in inorder:
        print(n, end=' ')

    print("\n\n --- POSTORDER --- ")
    postorder = bt_postorder(tree)
    for n in postorder:
        print(n, end=' ')