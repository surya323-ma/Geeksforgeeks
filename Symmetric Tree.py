Given the root of a binary tree, check whether it is symmetric, i.e., whether the tree is a mirror image of itself.


A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.
#code here
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            a, b = queue.popleft()

            if not a and not b:
                continue
            if not a or not b or a.data != b.data:
                return False

            queue.append((a.left, b.right))
            queue.append((a.right, b.left))

        return True
