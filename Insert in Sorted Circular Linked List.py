Given a sorted circular linked list, the task is to insert a new node in this circular linked list so that it remains a sorted circular linked list.

/*
class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
} */

class Solution {
    public Node sortedInsert(Node head, int data) {
        Node newNode = new Node(data);
        
        // Inserting element at the start while retaining circular list
        if (head.data >= data) {
            newNode.next = head;
            
            Node ptr = head;
            while (ptr.next != head) {
                ptr = ptr.next;
            }
            ptr.next = newNode;
            
            return newNode;
        }
        
        Node ptr = head;
        while (ptr.next != head && ptr.next.data <= data) {
            ptr = ptr.next;
        }
        
        newNode.next = ptr.next;
        ptr.next = newNode;
        
        return head;
    }
}
python 3

#User function Template for python3

'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
        0 7 43 57 71 81
7
  '''
class Solution:
    
    
    def sortedInsert(self, head, data):
        new_node = Node(data)
        if not head:
            new_node.next = new_node
            return new_node
            
        if data < head.data:
            last = head
            node = head
            while node:
                last = node
                node = node.next
                if node == head:
                    break
                
            new_node.next = head
            last.next = new_node
            return new_node
        
        tail = None
        node = head
        while node:
            if node.data > data:
                break
            last = node
            node = node.next
            if node == head:
                break
        
        last.next = new_node
        new_node.next = node
        
        
        # print(f"at {node.data} with last={last.data} and tail={tail.data if tail else 'None'}")
        
        return head
        
