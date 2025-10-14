Given the root of a Binary Search Tree and two integers l and r, the task is to find the sum of all nodes that lie between l and r, including both l and r.
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""
class Solution:
    def nodeSum(self, root, l, r):
        if not root:
            return 0

        if root.data < l:
            return self.nodeSum(root.right, l, r)
        elif root.data > r:
            return self.nodeSum(root.left, l, r)
        else:
            return (root.data +
                    self.nodeSum(root.left, l, r) +
                    self.nodeSum(root.right, l, r))
