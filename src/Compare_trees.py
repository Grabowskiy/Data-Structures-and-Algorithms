from Trees import BinaryNode


def compare(a: BinaryNode, b: BinaryNode) -> bool:
    # Structural checks
    if a is None and b is None:
        return True

    if a is None or b is None:
        return False

    # Value check
    if a.value != b.value:
        return False

    return compare(a.left, b.left) and compare(a.right, b.right)


if __name__ == "__main__":
    tree1 = BinaryNode(0,
                      BinaryNode(1,
                                 BinaryNode(3),
                                 BinaryNode(4)),
                      BinaryNode(2,
                                 BinaryNode(5),
                                 BinaryNode(6))
                      )

    tree2 = BinaryNode(0,
                       BinaryNode(1,
                                  BinaryNode(3),
                                  BinaryNode(4)),
                        BinaryNode(2,
                                   BinaryNode(5),
                                   BinaryNode(6))
    )

    print(f"The trees are the same: {compare(tree1, tree2)}")
