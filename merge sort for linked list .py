You are given the head of a linked list. You have to sort the given linked list using Merge Sort
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        def merge(l, r):
            dummy = tail = Node(0)
            while l and r:
                if l.data < r.data:
                    tail.next, l = l, l.next
                else:
                    tail.next, r = r, r.next
                tail = tail.next
            tail.next = l or r
            return dummy.next

        def sort(h):
            if not h or not h.next:
                return h
            slow, fast = h, h.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            mid, slow.next = slow.next, None
            return merge(sort(h), sort(mid))

        return sort(head)
