Given two arrays pre[] and post[] that represent the preorder and postorder traversals of a full binary tree. Your task is to construct the binary tree and return its root.

Note:  Full Binary Tree is a binary tree where every node has either 0 or 2 children. The preorder and postorder traversals contain unique values, and every value present in the preorder traversal is also found in the postorder traversal.
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def constructTree(self, pre, post):
        n = len(pre)
        post_to_i = {p: i for i, p in enumerate(post)}
        
        def build(pre_i=0, post_lo=0, post_hi=n - 1):
            node = Node(pre[pre_i])
            pre_i += 1
            if post_lo == post_hi:
                return node, pre_i
            post_mid = post_to_i[pre[pre_i]]
            node.left, pre_i = build(pre_i, post_lo, post_mid)
            node.right, pre_i = build(pre_i, post_mid + 1, post_hi - 1)
            return node, pre_i
        
        return build()[0]
   
