# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = ListNode() # dummy
        output = prev

        while fast and fast.next:
            prev.next = slow
            slow = slow.next
            fast = fast.next.next
            prev = prev.next

        if not prev:
            return prev

        prev.next = slow.next

        return output.next
"""
slow = [7,1,2,6]
fast = null
prev = 4 
"""
