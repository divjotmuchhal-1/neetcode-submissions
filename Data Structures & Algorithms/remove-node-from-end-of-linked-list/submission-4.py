# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 1: Calculate the length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Find the node before the node to be removed
        current = dummy
        for i in range(length - n):
            current = current.next
        
        # Step 3: Remove the N-th node from the end
        current.next = current.next.next
        
        return dummy.next
