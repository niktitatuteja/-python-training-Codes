# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head or not head.next or k == 0:
            return head

        
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        
       
        tail.next = head
        
       
        effective_k = k % length
        
        
        new_tail_position = length - effective_k - 1 
        current = head
        for _ in range(new_tail_position):
            current = current.next
        
        
        new_head = current.next
        current.next = None
        
        return new_head
