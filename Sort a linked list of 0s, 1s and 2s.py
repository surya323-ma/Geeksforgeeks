Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only. Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def segregate(self, head):
        def insert(curr,count,n):
            for i in range(count):
                curr.data = n
                curr = curr.next
            return curr
        count_zero = 0
        count_one = 0
        count_two = 0
        curr = head
        while curr:
            if curr.data==0:
                count_zero +=1
            elif curr.data==1:
                count_one +=1
            else:
                count_two += 1
            curr = curr.next
        
        curr = head
        curr = insert(curr,count_zero,0)
        curr = insert(curr,count_one,1)
        curr = insert(curr,count_two,2)
        return head
