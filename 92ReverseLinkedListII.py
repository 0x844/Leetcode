# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if (head == None or left == right):
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for i in range(left - 1): # iterates til first starting node that needs to be reversed
            prev = prev.next

        curr = prev.next 
        for i in range(right - left):
            old_node = curr.next
            curr.next = old_node.next
            old_node.next = prev.next
            prev.next = old_node

        return dummy.next
        

            
        
        
