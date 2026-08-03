"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        currToNew = {None: None}
        curr = head
        while curr:
            currToNew[curr] = Node(curr.val,curr.next,curr.random)
            curr = curr.next
        curr = head
        while curr:
            copy = currToNew[curr]
            copy.next = currToNew[curr.next]
            copy.random = currToNew[curr.random]
            curr = curr.next
        return currToNew[head]