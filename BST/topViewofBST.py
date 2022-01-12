from binarySearchTree import TreeNode
from binarySearchTree import BinarySearchTree
from typing import collections


def topView(root):
    # Write your code here
    axis_to_values = dict()  # {x-axis of Node : Value of Node}
    x_axis = 0

    queue = collections.deque()
    queue.append((x_axis, root))  # (x-axis of Node, Node)

    while (len(queue) != 0):
        current = queue.popleft()
        if (current[0] not in axis_to_values):
            axis_to_values[current[0]] = current[1].info

        if (current[1].left != None):
            queue.append((current[0] - 1, current[1].left))
        if (current[1].right != None):
            queue.append((current[0] + 1, current[1].right))

    for i in sorted(axis_to_values):
        print(axis_to_values[i], end=" ")


if __name__ == '__main__':
    myTree = BinarySearchTree()
    nodes = [1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]

    for node in nodes:
        myTree.insert(node)

    # Expected: 2 1 14 15 12
    topView(myTree.root)
