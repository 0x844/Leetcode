"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

n = length of linked list
random can point to null
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if (head == None):
            return head
        
        hasmp = {None:None} # init hash map to None, since random pointers can be null

        curr = head

        while curr: 
            hasmp[curr] = Node(curr.val, None, None) # init new node with just val
            curr = curr.next

        curr = head

        while curr:
            copy = hasmp[curr] # get copied node from hash map
            copy.next = hasmp[curr.next] # set values from hash map
            copy.random = hasmp[curr.random]
            curr = curr.next
        return hasmp[head]
