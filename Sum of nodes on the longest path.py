Given a binary tree root[], you need to find the sum of the nodes on the longest path from the root to any leaf node. If two or more paths have the same length, the path with the maximum sum of node values should be considered.
#Code here
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        return self.solve(root, 0, 0)[1]

    def solve(self, root, length, path_sum):
        if not root:
            return (length, path_sum)
        
        path_sum += root.data
        
        if not root.left and not root.right:
            return (length + 1, path_sum)
        
        left_length, left_sum = self.solve(root.left, length + 1, path_sum)
        right_length, right_sum = self.solve(root.right, length + 1, path_sum)

        if left_length > right_length:
            return (left_length, left_sum)
        elif right_length > left_length:
            return (right_length, right_sum)
        else:
            return (left_length, max(left_sum, right_sum))
