from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree
from typing import collections

# Solution: https://www.youtube.com/watch?v=gs2LMfuOR9k


def lca(root, v1, v2):
    # Enter your code here
    if (v1 > root.info and v2 < root.info):
        return root
    elif (v1 < root.info and v2 > root.info):
        return root
    elif (v1 == root.info or v2 == root.info):
        return root

    else:
        if (v1 < root.info and v2 < root.info):
            return lca(root.left, v1, v2)
        elif (v1 > root.info and v2 > root.info):
            return lca(root.right, v1, v2)


if __name__ == "__main__":
    testTree = BinarySearchTree()
    items_to_insert = [4, 2, 3, 1, 7, 6]

    for i in items_to_insert:
        testTree.insert(i)

    lowest_common_ancestor = lca(testTree.root, 2, 3)
    print(lowest_common_ancestor.info)
