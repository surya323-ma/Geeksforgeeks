Given the root of a binary search tree and a number k, find the greatest number in the binary search tree that is less than or equal to k.
#code here
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findMaxFork(self, root, k):
        #code here
        res = None
        while(root):
            if root.data <= k:
                res = root.data
                root = root.right
            else:
                root = root.left
        return res if res != None else -1
