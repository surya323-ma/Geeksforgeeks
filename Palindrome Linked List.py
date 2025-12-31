You are given the head of a singly linked list of positive integers. You have to check if the given linked list is palindrome or not.
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class Solution:
    def isPalindrome(self, head: Node) -> bool:
        if not head or not head.next: return True

        # Find middle (slow/fast pointers)
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Reverse second half
        prev, cur = None, slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        # Compare halves
        first, second = head, prev
        while second:
            if first.data != second.data: return False
            first, second = first.next, second.next
        return True
