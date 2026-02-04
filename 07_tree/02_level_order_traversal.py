# level order traversal

from collections import deque

# creating the tree


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")

# edges
A.left = B
A.right = C

B.left = D
B.right = E

C.left = F


def level_order_traversa(node):
    if not node:
        return

    q = deque([node])

    while q:
        curr = q.popleft()
        print(curr.data, end=" ")

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)


level_order_traversa(A)
