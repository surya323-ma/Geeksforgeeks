You are given the head of a Singly linked list. You have to reverse every k node in the linked list and return the head of the modified list.
Note: If the number of nodes is not a multiple of k then the left-out nodes at the end, should be considered as a group and must be reversed.

"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
    
        def reverse(head):
            prev, node = None, head
            for _ in range(k):
                node.next, node, prev = prev, node.next, node
                if node is None:
                    return prev
            head.next = reverse(node)
            return prev
        
        return reverse(head)
