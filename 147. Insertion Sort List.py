# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        # Create a dummy node to act as a placeholder for the head of the sorted list.
        dummy = ListNode(0)
        # `prev` is a pointer that helps iterate through the sorted portion to find the correct insertion spot.
        # It is reset to `dummy` whenever the current `head` node's value is not in natural order.
        prev = dummy

        while head:
            # Cache the next node in the original list before modifying the current 'head' node's pointers
            next_node = head.next
            
            # If the current node's value is smaller than the last node in the "naturally" sorted section,
            # we must restart the search from the beginning of the *entire* sorted list (dummy).
            if prev.val >= head.val:
                prev = dummy
            
            # Find the correct position to insert the current node (`head`) within the sorted list (starting from `prev`)
            while prev.next and prev.next.val < head.val:
                prev = prev.next
            
            # Insert the current node into the found position
            head.next = prev.next
            prev.next = head
            
            # Move to the next node in the original unsorted list
            head = next_node
            
        return dummy.next
