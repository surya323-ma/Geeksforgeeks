Given a binary tree and the task is to find the spiral order traversal of the tree and return the list containing the elements.
Spiral order Traversal mean: Starting from level 0 for root node, for all the even levels we print the node's value from right to left and for all the odd levels we print the node's value from left to right.
For below tree, function should return [1, 2, 3, 4, 5, 6, 7]

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''        
class Solution:
    def findSpiral(self, root):
        
        d = {}
        def traverse(node, level):
            if not node:
                return
            if level not in d:
                d[level] = []
            d[level].append(node.data)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
            
        traverse(root, 0)
        ans = []
        for i in d:
            if i % 2:
                ans.extend(d[i])
            else:
                ans.extend(d[i][::-1])
        return ans
