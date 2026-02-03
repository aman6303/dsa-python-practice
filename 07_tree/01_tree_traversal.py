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


# preorder traversal


def PreOrder(root):
    if root is not None:
        print(root.data, end=" ")
        PreOrder(root.left)
        PreOrder(root.right)


# def preorder_traversal(node):
#     if not node:
#         return

#     print(node.data, end=" ")
#     preorder_traversal(node.left)
#     preorder_traversal(node.right)  -- getting the same answer


# print(PreOrder(A))
PreOrder(A)
print()


def PostOrder(root):
    if root is not None:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data, end=" ")


PostOrder(A)
print()


def InOrder(root):
    if root is not None:
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)


InOrder(A)
print()


# level order traversal
